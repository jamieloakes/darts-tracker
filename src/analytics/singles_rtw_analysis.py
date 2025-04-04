import polars as pl
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

import src.database as database


def distribution():
    """ Show histogram of total attempts per game and save as .png """
    query:str = """
                SELECT game_id, SUM(attempts) AS total_attempts
                FROM singles_rtw
                GROUP BY game_id
                """
    df:pl.DataFrame = database.queryDatabase(query=query)
    nbins:int = int(np.ceil(df.select(pl.max('total_attempts') - pl.min('total_attempts')).item() / 3))
    fig = px.histogram(data_frame=df, x='total_attempts', nbins=nbins)

    median:int = df.select(pl.median('total_attempts')).item()
    fig.add_vline(x=median, line_width=3, line_dash='solid', line_color='red')

    q1:float = df.select(pl.quantile('total_attempts',0.25)).item()
    fig.add_vline(x=q1, line_width=3, line_dash='dash', line_color='red')

    q3:float = df.select(pl.quantile('total_attempts',0.75)).item()
    fig.add_vline(x=q3, line_width=3, line_dash='dash', line_color='red')

    fig.update_xaxes(range=[30, 100])
    fig.update_layout(width=900, height=500, bargap=0.1)
    fig.write_image('./src/analytics/charts/singles_rtw_dist.png')


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

    r:np.array = np.repeat(a=1,repeats=20) # Controls length of bar
    theta:np.array = np.arange(0,360,18) # Controls segments in graph
    # Order values in same order as labels to ensure correct colour scaling
    values:list[int] = [df.filter(pl.col('target')==label).select('total_attempts').item() for label in labels]

    fig = go.Figure(
        go.Barpolar(
            r=r,
            theta=theta,
            marker={'color':values,'colorscale':'OrRd', 'showscale':True, 'colorbar_title_text':'attempts'}
        )
    )

    fig.update_layout(
            polar={'angularaxis':{
                'rotation':89, # Ensures that 20 is at top of board
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
    fig.write_image('./src/analytics/charts/singles_rtw_heatmap.png')