import sqlite3
import os
import polars as pl

def connectToDatabase() -> sqlite3.Connection:
    """
        Centralised function for connecting to database\n
        Returns:
            conn - Connection object to database
    """
    return sqlite3.connect('practice_data.db')


def setupDatabase() -> None:
    """
        Create database with required tables and fields\n
        See docs/ folder for more info on schema and fields
    """
    if os.path.exists('practice_data.db'):
        return

    try:
        conn:sqlite3.Connection = connectToDatabase()
        cursor:sqlite3.Cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS singles_rtw (
            event_id INTEGER PRIMARY KEY,
            game_id TEXT NOT NULL,
            event_date TEXT NOT NULL,
            target TEXT NOT NULL,
            attempts INTEGER NOT NULL
        ); """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS doubles_rtw (
            event_id INTEGER PRIMARY KEY,
            game_id TEXT NOT NULL,
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
    finally:
        cursor.close()
        conn.close()


def insertRecords(table:str, fields:tuple[str], data:list[tuple]) -> None:
    """
        Insert record(s) into database\n
        Supports inserting either a single record, or multiple records\n
        Params:
            table - Name of table to insert data into
            fields - Fields to be inserted
            data - Record data to insert
    """
    try:
        conn:sqlite3.Connection = connectToDatabase()
        cursor:sqlite3.Cursor = conn.cursor()

        # Create dynamic placeholders to support with inserting across tables with differing columns
        field_placeholder:str = ','.join(fields)
        value_placeholder:str = ','.join('?' * len(fields))
        cursor.executemany(f'INSERT INTO {table} ({field_placeholder}) VALUES ({value_placeholder})', data)
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def queryDatabase(query:str) -> pl.DataFrame:
    """ 
        Perform SELECT query against database and return result\n
        Params:
            query - SQL query to run
        Returns:
            df - DataFrame containg result set of query
    """
    try:
        conn:sqlite3.Connection = connectToDatabase()
        return pl.read_database(query=query, connection=conn)
    finally:
        conn.close()