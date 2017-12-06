import sys
import pyodbc 
import os
import time
from time import gmtime, strftime

os.system('cls')
param = (
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=192.168.0.252,1433;'
    r'DATABASE=ksm;'
    r'UID=sa;'
    r'PWD=1qaz@WSX3edc'
        )

#db_connection = pyodbc.connect(param)
#db_connection.autocommit = True
#db_cursor = db_connection.cursor()



def raiserror():
    print("function begin!")
    db_connection = pyodbc.connect(param)
    db_connection.autocommit = True
    db_cursor = db_connection.cursor()
    i=10
    while i < 25:
        try:
            sql_command =   ("RAISERROR ('test severity "+str(i)+"',"+str(i)+ ", 1) with log;")
            db_cursor.execute(sql_command)
            i = i + 1
        except:
            i = i + 1
            print ('caught exception'+str(i))
            
    db_cursor.close()
    del db_cursor
    db_connection.close()

a=0
while a < 10000:
    print("doing #" + str(a))
    raiserror()
    a = a + 1

#db_connection.autocommit = False
