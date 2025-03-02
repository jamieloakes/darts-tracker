import polars as pl
import matplotlib.pyplot as plt
import src.database as database
import modules.utils as utils

query:str = """ 
            SELECT target, SUM(attempts) AS total_attempts 
            FROM singles_rtw
            GROUP BY target
            ORDER BY total_attempts
            """


def showTable():
    """
        Show table view of total attempts per target
    """
    df:pl.DataFrame = database.queryDatabase(query=query)
    with pl.Config(tbl_rows=20):
        print(df)


def dartboardVis():
    """
        Show dartboard and colour each target segment based on total attempts\n
        Darker colour means more attempts at target
    """
    df:pl.DataFrame = database.queryDatabase(query=query)

    values:list[int] = [360 / 20 for i in range(20)]
    labels:list[str] = ['S20', 'S5', 'S12', 'S9', 'S14', 'S11', 'S8', 'S16', 'S7', 'S19',
                        'S3', 'S17', 'S2', 'S15', 'S10', 'S6', 'S13', 'S4', 'S18', 'S1']
    colours:list[tuple[int,int,int]] = utils.conditionalFormatter(df=df, y_col='total_attempts', labels=labels)
    
    fig, ax = plt.subplots()
    fig.set_size_inches(12,8)
    # Set each segment to 18 as this is the area for each target on the dartboard
    # Set startangle=81 so that segments line up with 20 at the top
    ax.pie(x=values, labels=labels, colors=colours, startangle=81, textprops={'fontsize':16}) 
    ax.set_title(label='Singles Round the World Performance', fontdict={'fontsize':18, 'weight':'bold'})
    plt.show()
    

if __name__ == '__main__':
    dartboardVis()