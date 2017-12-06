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

def cursor_open():
    print("starting function cursor_open")
    db_connection = pyodbc.connect(param)
    db_connection.autocommit = True
    db_cursor = db_connection.cursor()
    i=0
    while i < 1000:
        sql_command =   ("""DECLARE db_cursor"""+str(i)+""" CURSOR FOR
                            SELECT NAME
                            FROM MASTER.dbo.sysdatabases
                            OPEN db_cursor"""+str(i))
        db_cursor.execute(sql_command)
        i = i + 1
        print ('opening cursor#'+str(i))
        #time.sleep(1)
    db_cursor.execute("select 'Open cursors' as METRIC_NAME, count(cursor_id) as CNT from sys.dm_exec_cursors(0) where is_open != 0")
    for row in db_cursor.fetchall():
        print (row)
    print('waiting 100')
    time.sleep(100)
    
    db_cursor.close()
    del db_cursor
    db_connection.close()

cursor_open()

