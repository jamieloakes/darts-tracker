import datetime as dt
import polars as pl


def getTodaysDate() -> str:
    """ Returns today's date in YYYY-MM-DD format """
    today:dt.datetime = dt.datetime.today()
    return today.strftime("%Y-%m-%d")


def conditionalFormatter(df:pl.DataFrame, y_col:str, labels:list[str], reverse:bool) -> list[tuple[int,int,int,float]]:
    """ 
        Return list of colours based off values in array\n
        Use in charts to conditionally format labels\n
        Params:
            df - DataFrame containing raw query data
            y_col - Column name of numerical data in df
            labels - Labels to conditionally format for
            reverse - Flag for whether to reverse colours of list
        Returns:
            colours - RGB value of colour
    """
    # Rank total per target and calculate RGB alpha value for each
    df = df.with_columns((pl.col(y_col).rank('min') / 20).alias('alpha_value'))
    
    # Filter using list comprehension to maintain order relative to labels
    colours:list[tuple[int,int,int,float]] = [(1, 0, 0, df.filter(pl.col('target')==label).select('alpha_value').item()) for label in labels]

    return colours.reverse() if reverse else colours