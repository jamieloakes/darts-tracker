import polars as pl
import plotly.graph_objects as go
import numpy as np

import src.database as database


def hitsTable():
    """ Create table view of total hits per target and save as .png """
    query:str = """
                SELECT target, hits
                FROM doubles_rtw
                """
    df:pl.DataFrame = database.queryDatabase(query=query)
    df = df.group_by('target').agg(
        pl.sum('hits').alias('total_hits'),
        pl.quantile(column='hits', quantile=0.25).alias('25th_perc'),
        pl.median('hits').alias('median'),
        pl.quantile(column='hits', quantile=0.75).alias('75th_perc'),
    ).sort(by='total_hits', descending=True)

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
                            df['total_hits'],
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
    fig.write_image('./src/analytics/charts/doubles_rtw_table.png')


def dartboardHeatmap() -> None:
    """
        Create dartboard visualsation and and save as .png\n
        More vibrant colour means less hits at target\n
    """
    query:str = """ 
                SELECT target, SUM(hits) AS total_hits 
                FROM doubles_rtw
                GROUP BY target
                ORDER BY total_hits
                """
    df:pl.DataFrame = database.queryDatabase(query=query)
    labels:list[str] = ['D20', 'D5', 'D12', 'D9', 'D14', 'D11', 'D8', 'D16', 'D7', 'D19',
                        'D3', 'D17', 'D2', 'D15', 'D10', 'D6', 'D13', 'D4', 'D18', 'D1']

    r:np.array = np.repeat(a=1,repeats=20)
    theta:np.array = np.arange(0,360,18)
    values:list[int] = [df.filter(pl.col('target')==label).select('total_hits').item() for label in labels]

    fig = go.Figure(
        go.Barpolar(
            r=r,
            theta=theta,
            marker={'color':values,'colorscale':'OrRd', 'showscale':True, 'reversescale':True, 'colorbar_title_text':'hits'},
        ),
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
        }
    )
    fig.write_image('./src/analytics/charts/doubles_rtw_heatmap.png')