import sqlite3

def testDatabaseTables() -> None:
    """ Test function for checking tables have been created """
    try:
        conn:sqlite3.Connection = sqlite3.connect('practice_data.db')
        cursor:sqlite3.Cursor = conn.cursor()
        cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'""")
        print(cursor.fetchall())
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    testDatabaseTables()