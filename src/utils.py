import datetime as dt
import sqlite3

def getTodaysDate() -> str:
    """ Returns today's date in YYYY-MM-DD format """
    today:dt.datetime = dt.datetime.today()
    return today.strftime("%Y-%m-%d")


def insertMany(table:str, fields:tuple[str], data:list[tuple]) -> None:
    """
        Insert multiple records into database at once\n
        Params:
            table - Name of table to insert data into
            fields - Fields of table to be inserted
            data - Record data to insert
        Returns:
            None
    """
    try:
        conn:sqlite3.Connection = sqlite3.connect('practice_data.db')
        cursor:sqlite3.Cursor = conn.cursor()

        field_placeholder:str = ','.join(fields)
        value_placeholder:str = ','.join('?' * len(fields))
        cursor.executemany(f'INSERT INTO {table} ({field_placeholder}) VALUES ({value_placeholder})', data)
    finally:
        conn.commit()
        cursor.close()