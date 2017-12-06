import sys
import pyodbc 
import os
import time
from time import gmtime, strftime

os.system('cls')
param = (
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=192.168.0.205,49177;'
    r'DATABASE=master;'
    r'UID=sa;'
    r'PWD=1qaz@WSX3edc'
        )

def print_sql():
    print("print query")
    db_connection = pyodbc.connect(param)
    db_connection.autocommit = True
    db_cursor = db_connection.cursor()
    db_cursor.execute("select 'Open cursors' as METRIC_NAME, count(cursor_id) as CNT from sys.dm_exec_cursors(0) where is_open != 0")
    for row in db_cursor.fetchall():
        print (row)

    time.sleep(1)
    db_cursor.close()
    del db_cursor
    print('waiting 100')
    time.sleep(100)
    db_connection.close()

print_sql()