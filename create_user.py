import sys
import pyodbc 
import os
import time
from time import gmtime, strftime

os.system('cls')
db_connection = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=192.168.0.205,49189;'
    r'DATABASE=master;'
    r'UID=sa;'
    r'PWD=1qaz@WSX3edc'
    )

db_connection.autocommit = True
db_cursor = db_connection.cursor()
i=1
while i < 5:
    sql_command =("CREATE LOGIN user"+str(i)+" with password = '1qaz@WSX3edc';")
    sql_command1 =("CREATE USER user"+str(i)+" from login user"+str(i)+' with default_schema = master;')
    print ("creating user",str(i))
    time.sleep(1)
    db_cursor.execute(sql_command)
    db_cursor.execute(sql_command1)
    i = i + 1
db_connection.autocommit = False
db_cursor.close()
del db_cursor
db_connection.close()