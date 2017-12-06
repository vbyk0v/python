import sys
import pyodbc 
import os
import time
from time import gmtime, strftime

os.system('cls')
connection = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=192.168.0.205,20012;'
    r'DATABASE=master;'
    r'UID=sa;'
    r'PWD=1qaz@WSX3edc'
    )

connection_1 = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=192.168.0.205,20012;'
    r'DATABASE=master;'
    r'UID=sa;'
    r'PWD=1qaz@WSX3edc'
    )

connection_2 = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=192.168.0.205,20012;'
    r'DATABASE=master;'
    r'UID=sa2;'
    r'PWD=1qaz@WSX3edc'
    )


connection.autocommit = True
connection_1.autocommit = True
connection_1.autocommit = True

db_cursor = connection.cursor()
db_cursor_1 = connection_1.cursor()
db_cursor_2 = connection_2.cursor()



##################
## create database
##################
db_name = "database_" + str(strftime('%H_%M_%S_%Y',gmtime()))
print ("creating database =>",db_name)
time.sleep(1)
try:
    sql_create_db =("CREATE DATABASE " + db_name)
    db_cursor.execute(sql_create_db)
    print("database create ok")
    time.sleep(1)
except:
    print("database create fail")

##################
## select database
##################
try:
    sql_select_db = ("USE " + db_name +";")
    db_cursor.execute(sql_select_db)
    print("database selected ok")
    time.sleep(1)
except:
    print("database selected fail")




##################
##create table_1
##################
try:
    sql_create_table_1 = ("""CREATE TABLE ##Employees (
                        EmpId INT IDENTITY,
                        EmpName VARCHAR(16),
                        Phone VARCHAR(16)
                        )
                        """)
    db_cursor.execute(sql_create_table_1)
    print("table_1 created ok")
    time.sleep(1)
except:
    print("table_1 fail")

try:
    sql_insert_table_1 = ("""INSERT INTO ##Employees (EmpName, Phone)
                            VALUES ('Martha', '800-555-1212'), ('Jimmy', '619-555-8080')
                            """)
    db_cursor.execute(sql_insert_table_1)
    print("table_1 inserted ok")
    time.sleep(1)
except:
    print("table_1 inserted fail")


##################
##create_table_2
##################
try:
    sql_create_table_2 = ("""CREATE TABLE ##Suppliers(
                            SupplierId INT IDENTITY,
                            SupplierName VARCHAR(64),
                            Fax VARCHAR(16)
                            )
                            """)
    db_cursor.execute(sql_create_table_2)
    print("table_2 created ok")
    time.sleep(1)
except:
    print("table_2 fail")

try:
    sql_insert_table_2 = ("""INSERT INTO ##Suppliers (SupplierName, Fax)
                            VALUES ('Acme', '877-555-6060'), ('Rockwell', '800-257-1234')
                            """)
    db_cursor.execute(sql_insert_table_2)
    print("table_2 inserted ok")
    time.sleep(1)
except:
    print("table_2 inserted fail")


#################
#### begin tran
#################

try:
    sql_tran_table_1 = ("""BEGIN TRAN;""")
    db_cursor_1.execute(sql_tran_table_1)
    print("tran for table_1 ok")
    time.sleep(1)
except:
    print("tran for table_1 fail")


try:
    sql_tran_table_2 = ("""BEGIN TRAN;""")
    db_cursor_2.execute(sql_tran_table_2)
    print("tran for table_2 ok")
    time.sleep(1)
except:
    print("tran for table_2 fail")


##########################
##update1
##########################

try:
    sql_update_table_1 = ("""UPDATE ##Employees
                            SET EmpName = 'Mary'
                            WHERE empid = 1
                            """)
    db_cursor_1.execute(sql_update_table_1)
    print("table_1 updated ok")
    time.sleep(1)
except:
    print("table_1 updated fail")


try:
    sql_update_table_2 = ("""UPDATE ##Suppliers
                            SET Fax = N'555-1212'
                            WHERE supplierid = 1
                            """)
    db_cursor_2.execute(sql_update_table_2)
    print("table_2 updated ok")
    time.sleep(1)
except:
    print("table_2 updated fail")

######################
##deadlock
######################
print("trying to deadlock table_1")
time.sleep(1)

sql_deadlock_table_1 = (""" BEGIN TRANSACTION;
                            UPDATE ##Suppliers
                            SET Fax = N'555-1212'
                            WHERE supplierid = 1
                            COMMIT TRANSACTION;
                            """)

db_cursor_1.execute(sql_deadlock_table_1)
print("deadlock to table_1 ok")
time.sleep(1)
print("deadlock to table_1 fail")


print("trying to deadlock table_2")
time.sleep(5)


sql_deadlock_table_2 = ("""UPDATE ##Employees
                            SET phone = N'555-9999'
                            WHERE empid = 1
                            """)
while True:
    try:                            
        db_cursor_2.execute(sql_deadlock_table_2)
        print("deadlock to table_2 ok")
        time.sleep(1)
    except:
        print("deadlock to table_2 fail")

print("deadlock unlocked!!!")
time.sleep(5)


connection_1.autocommit = False
db_cursor.close()
del db_cursor
connection_1.close()