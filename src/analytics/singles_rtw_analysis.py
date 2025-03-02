import polars as pl
import matplotlib.pyplot as plt
import src.database as database
import modules.utils as utils

def dartboardVis():
    query:str = """ 
                    SELECT target, SUM(attempts) AS total_attempts 
                    FROM singles_rtw
                    GROUP BY target
                """
    df:pl.DataFrame = database.queryDatabase(query=query)

    fig:plt.Figure = plt.figure()
    ax:plt.Axes = fig.add_subplot()
    values:list[int] = [360 / 20 for i in range(20)]
    labels:list[str] = ['S20', 'S5', 'S12', 'S9', 'S14', 'S11', 'S8', 'S16', 'S7', 'S19',
                        'S3', 'S17', 'S2', 'S15', 'S10', 'S6', 'S13', 'S4', 'S18', 'S1']
    
    ax.pie(x=values, labels=labels, startangle=81, radius=1.2)
    plt.show()
    
if __name__ == '__main__':
    dartboardVis()