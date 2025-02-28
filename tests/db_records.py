import sqlite3
import argparse

def checkRecords(table:str) -> None:
    """
        Test function for checking whether records added to table\n
        Params:
            table - Name of table to check records for
    """
    try:
        conn:sqlite3.Connection = sqlite3.connect('practice_data.db')
        cursor:sqlite3.Cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table}')
        print(cursor.fetchall())
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if  __name__ == '__main__':
    parser:argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('table', help='Name of table to check records for', type=str)
    args:argparse.Namespace = parser.parse_args()
    checkRecords(table=args.table)