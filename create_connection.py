import sys
import pyodbc 
import time
import os

os.system('cls')
i=1
myList=[]

while i < 2000:
    db_connection = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=192.168.0.205,1433;'
    r'DATABASE=database_1;'
    r'UID=sa;'
    r'PWD=1qaz@WSX3edc'
    )
    myList.append(db_connection)
    i = i + 1
    time.sleep(1)
    print(str(i)+' connection created')


    
print('waiting for closing connection')
time.sleep(500)
db_connection.close()
print('connection closed')