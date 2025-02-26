import sqlite3
import os

def setupDatabase() -> None:
    """
        Create database with required tables and fields\n
        See docs/ folder for more info on schema and fields
    """
    if os.path.exists('practice_data.db'):
        return

    conn:sqlite3.Connection = sqlite3.connect('practice_data.db')
    cursor:sqlite3.Cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS singles_rtw (
        event_id INTEGER PRIMARY KEY,
        event_date TEXT NOT NULL,
        target TEXT NOT NULL,
        attempts INTEGER NOT NULL
    ); """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doubles_rtw (
        event_id INTEGER PRIMARY KEY,
        event_date TEXT NOT NULL,
        target TEXT NOT NULL,
        hits INTEGER NOT NULL
    ); """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS legs_stats (
        leg_id INTEGER PRIMARY KEY,
        event_date TEXT NOT NULL,
        n_darts INTEGER NOT NULL,
        avg REAL NOT NULL,
        checkout_attempts INTEGER NOT NULL,
        win INTEGER NOT NULL
    ); """)

    conn.close()


def __checkTables() -> None:
    conn:sqlite3.Connection = sqlite3.connect('practice_data.db')
    cursor:sqlite3.Cursor = conn.cursor()
    cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'""")
    print(cursor.fetchall())
    conn.close()


def __checkRecords(table:str) -> None:
    conn:sqlite3.Connection = sqlite3.connect('practice_data.db')
    cursor:sqlite3.Cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {table}')
    print(cursor.fetchall())
    conn.close()


if __name__ == '__main__':
    #setupDatabase()
    __checkRecords(table='singles_rtw')