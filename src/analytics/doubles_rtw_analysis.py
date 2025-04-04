import polars as pl
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

import src.database as database


def distribution():
    """ Show histogram of total attempts per game and save as .png """
    query:str = """
                SELECT game_id, SUM(hits) AS total_hits
                FROM doubles_rtw
                GROUP BY game_id
                """
    df:pl.DataFrame = database.queryDatabase(query=query)
    nbins:int = int(np.ceil(df.select(pl.max('total_hits') - pl.min('total_hits')).item() / 3))
    fig = px.histogram(data_frame=df, x='total_hits', nbins=nbins)

    median:int = df.select(pl.median('total_hits')).item()
    fig.add_vline(x=median, line_width=3, line_dash='solid', line_color='red')

    q1:float = df.select(pl.quantile('total_hits',0.25)).item()
    fig.add_vline(x=q1, line_width=3, line_dash='dash', line_color='red')

    q3:float = df.select(pl.quantile('total_hits',0.75)).item()
    fig.add_vline(x=q3, line_width=3, line_dash='dash', line_color='red')

    fig.update_xaxes(range=[30, 100])
    fig.update_layout(width=900, height=500, bargap=0.1)
    fig.write_image('./src/analytics/charts/doubles_rtw_dist.png')


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

    r:np.array = np.repeat(a=1,repeats=20) # Controls length of bar
    theta:np.array = np.arange(0,360,18) # Controls segments in graph
    # Order values in same order as labels to ensure correct colour scaling
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
    fig.write_image('./src/analytics/charts/doubles_rtw_heatmap.png')