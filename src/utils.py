import datetime as dt
import math

def getTodaysDate() -> str:
    """ Returns today's date in YYYY-MM-DD format """
    today:dt.datetime = dt.datetime.today()
    return today.strftime("%Y-%m-%d")


def scaleYAxis(x:float, base:float) -> float:
    """
        Get max value for scaling y-axis\n
        Params:
            x - Max value of y-axis data
            base - Multiple to round nearest to
        Returns:
            y_scaler - Maximum value for y axis on plot
    """
    return round(base * math.ceil(x/base),2)
