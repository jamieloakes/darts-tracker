import polars as pl
import matplotlib.pyplot as plt
import src.database as database
import src.utils as utils

query:str = """ 
            SELECT target, SUM(hits) AS total_hits 
            FROM doubles_rtw
            GROUP BY target
            ORDER BY total_hits DESC
            """


def hitsTable():
    """ Create table view of total hits per target and save as .png """
    df:pl.DataFrame = database.queryDatabase(query=query)
    fig, ax = plt.subplots()
    fig.set_size_inches(8,8)
    ax.axis('off')

    table = plt.table(cellText=df.to_pandas(), loc='center', cellLoc='center')
    table.set_fontsize(size=16)
    table.scale(1,2)

    plt.savefig('./src/analytics/charts/doubles_rtw_table.png')


def dartboardHeatmap():
    """
        Create dartboard visualsation and and save as .png\n
        More vibrant colour means less hits at target\n
    """
    df:pl.DataFrame = database.queryDatabase(query=query)

    values:list[int] = [360 / 20 for i in range(20)]
    labels:list[str] = ['D20', 'D5', 'D12', 'D9', 'D14', 'D11', 'D8', 'D16', 'D7', 'D19',
                        'D3', 'D17', 'D2', 'D15', 'D10', 'D6', 'D13', 'D4', 'D18', 'D1']
    colours:list[tuple[int,int,int]] = utils.conditionalFormatter(df=df, y_col='total_hits', labels=labels, reverse=True)
    
    fig, ax = plt.subplots()
    fig.set_size_inches(12,8)
    # Set each segment to 18 as this is the area for each target on the dartboard
    # Set startangle=81 so that segments line up with 20 at the top
    plt.pie(x=values, labels=labels, colors=colours, startangle=81, textprops={'fontsize':16}) 

    plt.savefig('./src/analytics/charts/doubles_rtw_heatmap.png')
    

if __name__ == '__main__':
    hitsTable()