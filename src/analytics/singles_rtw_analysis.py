import polars as pl
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np

import src.database as database
import src.utils as utils

query:str = """ 
            SELECT target, SUM(attempts) AS total_attempts 
            FROM singles_rtw
            GROUP BY target
            ORDER BY total_attempts
            """


def attemptsTable():
    """ Create table view of total attempts per target and save as .png """
    df:pl.DataFrame = database.queryDatabase(query=query)
    fig, ax = plt.subplots()
    fig.set_size_inches(8,8)
    ax.axis('off')

    table = plt.table(cellText=df.to_pandas(), loc='center', cellLoc='center')
    table.set_fontsize(size=16)
    table.scale(1,2)

    plt.savefig('./src/analytics/charts/singles_rtw_table.png')


def dartboardHeatmap() -> None:
    """
        Create dartboard visualsation and and save as .png\n
        More vibrant colour means more attempts at target\n
    """
    df:pl.DataFrame = database.queryDatabase(query=query)
    labels:list[str] = ['S20', 'S5', 'S12', 'S9', 'S14', 'S11', 'S8', 'S16', 'S7', 'S19',
                        'S3', 'S17', 'S2', 'S15', 'S10', 'S6', 'S13', 'S4', 'S18', 'S1']

    r:np.array = np.repeat(a=1,repeats=20)
    theta:np.array = np.arange(0,360,18)
    values:list[int] = [df.filter(pl.col('target')==label).select('total_attempts').item() for label in labels]

    fig = go.Figure(
        go.Barpolar(
            r=r,
            theta=theta,
            marker={'color':values,'colorscale':'OrRd', 'showscale':True}
        )
    )

    fig.update_layout(
        polar={'angularaxis':{
            'rotation':89,
            'direction':'counterclockwise',
            'tickmode':'array',
            'tickvals':theta,
            'ticktext':labels
        },
        'radialaxis':{
            'visible':False
        }
        },
    )

    fig.write_image('./src/analytics/charts/singles_rtw_heatmap.png')
    

if __name__ == '__main__':
    dartboardHeatmap()