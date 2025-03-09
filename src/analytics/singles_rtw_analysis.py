import polars as pl
import plotly.graph_objects as go
import numpy as np

import src.database as database


def attemptsTable():
    """ Create table view of total attempts per target and save as .png """
    query:str = """
                SELECT target, attempts
                FROM singles_rtw
                """
    df:pl.DataFrame = database.queryDatabase(query=query)
    df = df.group_by('target').agg(
        pl.sum('attempts').alias('total_attempts'),
        pl.quantile(column='attempts', quantile=0.25).alias('25th_perc'),
        pl.median('attempts').alias('median'),
        pl.quantile(column='attempts', quantile=0.75).alias('75th_perc'),
    ).sort(by='total_attempts', descending=False)

    fig = go.Figure(
        data=[go.Table(
        header=dict(
            values=df.columns,
            line_color='darkslategrey',
            fill_color='#90E0EF',
            align='center',
            font={'size':18, 'color':'black'},
            height=50
        ),
        cells=dict(values=[df['target'],
                            df['total_attempts'],
                            df['25th_perc'],
                            df['median'],
                            df['75th_perc']
                        ],
                    line_color='darkslategrey',
                    fill_color='#CAF0F8',
                    align='center',
                    font={'size':16, 'color':'black', 'style':'italic'},
                    height=27
        )
        )]
    )
    fig.update_layout(width=900, height=800)
    fig.write_image('./src/analytics/charts/singles_rtw_table.png')


def dartboardHeatmap() -> None:
    """
        Create dartboard visualsation and and save as .png\n
        More vibrant colour means more attempts at target\n
    """
    query:str = """ 
            SELECT target, SUM(attempts) AS total_attempts 
            FROM singles_rtw
            GROUP BY target
            ORDER BY total_attempts
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