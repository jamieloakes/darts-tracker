import polars as pl
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

import src.database as database
import src.utils as utils


def summaryTable() -> None:
    """ Provide summary stats of 501 performance """
    query:str = """
                SELECT n_darts,
                ROUND((501.0 / (n_darts - checkout_attempts))*3,2) AS scoring_avg,
                checkout_attempts,
                win
                FROM legs_stats
                """
    df:pl.DataFrame = database.queryDatabase(query=query)

    aggregated:pl.DataFrame = df.select(
        pl.count('n_darts').alias('legs'),
        pl.median('n_darts', 'scoring_avg'),
        (pl.sum('win') / pl.sum('checkout_attempts')).round(2).alias('checkout_percentage'),
        (pl.sum('win') / pl.count('n_darts')).round(2).alias('win_percentage')
    )

    fig = go.Figure(
         data=[go.Table(
            header=dict(
                values=aggregated.columns,
                line_color='darkslategrey',
                fill_color='#90E0EF',
                align='center',
                font={'size':18, 'color':'black'},
                height=50
            ),
            cells=dict(values=[aggregated['legs'],
                                aggregated['n_darts'],
                                aggregated['scoring_avg'],
                                aggregated['checkout_percentage'],
                                aggregated['win_percentage']],
                        line_color='darkslategrey',
                        fill_color='#CAF0F8',
                        align='center',
                        font={'size':16, 'color':'black', 'style':'italic'},
                        height=30
            )
         )]
    )

    fig.update_layout(width=1200, height=275)
    fig.write_image('./src/analytics/charts/501_summary_table.png')


def timeSeriesAnalysis() -> None:
    """ Plot median scoring_avg and checkout percentage per week """
    query:str = """
                SELECT DATE(event_date, 'weekday 0', '-6 day') AS week_commencing,
                ROUND((501.0 / (n_darts - checkout_attempts))*3,2) AS scoring_avg,
                checkout_attempts,
                win
                FROM legs_stats
                """
    df:pl.DataFrame = database.queryDatabase(query=query)

    aggregated:pl.DataFrame = df.group_by('week_commencing').agg(
        pl.median('scoring_avg'),
        (pl.sum('win') / pl.sum('checkout_attempts')).round(2).alias('checkout_percentage')
    ).sort(by='week_commencing')

    fig = make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(
         go.Scatter(x=aggregated.get_column('week_commencing'),
                    y=aggregated.get_column('scoring_avg'),
                    mode='lines+markers+text',
                    line={'dash':'dash'},
                    name='scoring_avg'),
         secondary_y=False
    )
    fig.add_trace(
         go.Scatter(x=aggregated.get_column('week_commencing'),
                    y=aggregated.get_column('checkout_percentage'),
                    mode='lines+markers+text',
                    name='checkout_percentage'),
         secondary_y=True
    )
    

    # Set legend and plot area formatting
    fig.update_layout(legend={'x':0.5,
                              'y':1.2,
                              'orientation':'h',
                              'xanchor':'center',
                              'yanchor': 'top',
                            },
                        plot_bgcolor='#E1E0E0'
                    )
    fig.update_xaxes(title_text='week_commencing', type='category', tickangle=-45) # Convert x-axis to categorical to avoid date interpolation
    fig.update_traces(texttemplate='%{y}', textposition='bottom center') # Add data labels

    ax1_top:float = utils.scaleYAxis(x=aggregated.get_column('scoring_avg').max(), base=10)
    fig.update_yaxes(title_text='scoring_avg',
                     range=[0,ax1_top],
                     showgrid=False,
                     secondary_y=False)
    
    ax2_top:float = utils.scaleYAxis(x=aggregated.get_column('checkout_percentage').max(), base=0.1)
    fig.update_yaxes(title_text='checkout_percentage',
                     range=[0,ax2_top],
                     secondary_y=True)

    fig.write_image('./src/analytics/charts/501_timeseries.png')