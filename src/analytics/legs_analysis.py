import polars as pl
import matplotlib.pyplot as plt

import src.database as database
import src.utils as utils

query:str = """
            SELECT DATE(event_date, 'weekday 0', '-6 day') AS week_commencing,
            n_darts,
            avg AS three_dart_avg,
            ROUND((501.0 / (n_darts - checkout_attempts))*3,2) AS scoring_avg,
            checkout_attempts,
            win
            FROM legs_stats
            """


def timeSeriesAnalysis() -> None:
    df:pl.DataFrame = database.queryDatabase(query=query)

    aggregated:pl.DataFrame = df.group_by('week_commencing').agg(
        pl.median('scoring_avg'),
        (pl.sum('win') / pl.sum('checkout_attempts')).round(2).alias('checkout_percentage')
    ).sort(by='week_commencing')
    
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # Scoring average line
    ax1.plot(aggregated['week_commencing'], aggregated['scoring_avg'], 'g--o', label='scoring_avg')
    ax1_top:float = utils.scaleYAxis(x=aggregated.get_column('scoring_avg').max(), base=10)
    ax1.set_ylim(top=ax1_top, bottom=0)
    for x,y in zip(aggregated['week_commencing'], aggregated['scoring_avg']):
        ax1.annotate(text=y, xy=(x,y), textcoords='offset points', xytext=(0,-15), ha='center')

    # Checkout percentage line
    ax2.plot(aggregated['week_commencing'], aggregated['checkout_percentage'], 'b-o', label='checkout_percentage')
    ax2_top:float = utils.scaleYAxis(x=aggregated.get_column('checkout_percentage').max(), base=0.1)
    ax2.set_ylim(top=ax2_top, bottom=0)
    for x,y in zip(aggregated['week_commencing'], aggregated['checkout_percentage']):
            ax2.annotate(text=y, xy=(x,y), textcoords='offset points', xytext=(0,-15), ha='center')


    ax1.set_xlabel('week_commencing')
    ax1.set_ylabel('scoring_avg', color='g')
    ax2.set_ylabel('checkout_percentage', color='b')

    fig.legend(loc='upper center')
    plt.grid(linestyle='--')
    plt.savefig('./src/analytics/charts/501_timeseries.png', bbox_inches='tight', dpi=160)



if __name__ == '__main__':
    timeSeriesAnalysis()