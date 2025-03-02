import datetime as dt
import polars as pl


def getTodaysDate() -> str:
    """ Returns today's date in YYYY-MM-DD format """
    today:dt.datetime = dt.datetime.today()
    return today.strftime("%Y-%m-%d")


def conditionalFormatter(df:pl.DataFrame, y_col:str, labels:list[str]) -> list[tuple[int,int,int]]:
    """ 
        Return list of colours based off values in array\n
        Use in charts to conditionally format labels\n
        Params:
            df - DataFrame containing raw query data
            y_col - Column name of numerical data in df
            labels - Labels to conditionally format for
        Returns:
            colours - RGB value of colour
    """
    # Rank total per target and calculate Green value for RGB
    # Use 10 as multiplier as this is ((240-40) / 20)
    # Divide by 255 to convert RGB value into compatible format for matplotlib 
    df = df.with_columns((pl.col(y_col).rank('ordinal')).alias('rank'))
    df = df.with_columns(((250 - (pl.col('rank') * 10)) / 255).alias('colour_value'))

    # Filter using list comprehension to maintain order relative to labels
    return [(0, df.filter(pl.col('target')==label).select('colour_value').item(), 0) for label in labels]
