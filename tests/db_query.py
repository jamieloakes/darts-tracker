import sqlite3
import polars as pl


def testDatabaseQuery() -> None:
    conn:sqlite3.Connection = sqlite3.connect('practice_data.db')
    query:str = """ SELECT * FROM legs_stats """
    
    df:pl.DataFrame = pl.read_database(query=query, connection=conn).with_columns(pl.col('event_date').str.to_date())
    print(df)
    print(df.schema)


if __name__ == '__main__':
    testDatabaseQuery()
