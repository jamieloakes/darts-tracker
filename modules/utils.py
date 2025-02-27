import datetime as dt
import sqlite3

def getTodaysDate() -> str:
    """ Returns today's date in YYYY-MM-DD format """
    today:dt.datetime = dt.datetime.today()
    return today.strftime("%Y-%m-%d")