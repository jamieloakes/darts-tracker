import sqlite3
import os
import polars as pl

def setupDatabase() -> None:
    """
        Create database with required tables and fields\n
        See docs/ folder for more info on schema and fields
    """
    if os.path.exists('practice_data.db'):
        return

    try:
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
    except Exception as e:
        print(e)
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
        conn:sqlite3.Connection = sqlite3.connect('practice_data.db')
        cursor:sqlite3.Cursor = conn.cursor()

        # Create dynamic placeholders to support with inserting across tables with differing columns
        field_placeholder:str = ','.join(fields)
        value_placeholder:str = ','.join('?' * len(fields))
        cursor.executemany(f'INSERT INTO {table} ({field_placeholder}) VALUES ({value_placeholder})', data)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def queryDatabase(query:str) -> pl.DataFrame:
    """ 
        Perform SQL query against database and return data as Polars DataFrame\n
        Params:
            query - SQL query to run
    """
    try:
        conn:sqlite3.Connection = sqlite3.connect('practice_data.db')
        return pl.read_database(query=query, connection=conn)
    except Exception as e:
        print(e)
    finally:
        conn.close()