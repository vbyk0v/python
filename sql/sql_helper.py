import pyodbc
import time
import os
from time import gmtime, strftime


def create_connection():
    os.system('cls')
    i = 1
    myList = []

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
        print(str(i) + ' connection created')

    print('waiting for closing connection')
    time.sleep(500)
    db_connection.close()
    print('connection closed')

def cursor_open():
    os.system('cls')
    param = (
        r'DRIVER={ODBC Driver 13 for SQL Server};'
        r'SERVER=192.168.0.205,49177;'
        r'DATABASE=master;'
        r'UID=sa;'
        r'PWD=1qaz@WSX3edc'
    )
    print("starting function cursor_open")
    db_connection = pyodbc.connect(param)
    db_connection.autocommit = True
    db_cursor = db_connection.cursor()
    i = 0
    while i < 1000:
        sql_command = ("""DECLARE db_cursor""" + str(i) + """ CURSOR FOR
                            SELECT NAME
                            FROM MASTER.dbo.sysdatabases
                            OPEN db_cursor""" + str(i))
        db_cursor.execute(sql_command)
        i = i + 1
        print('opening cursor#' + str(i))
        # time.sleep(1)
    db_cursor.execute(
        "select 'Open cursors' as METRIC_NAME, count(cursor_id) as CNT from sys.dm_exec_cursors(0) where is_open != 0")
    for row in db_cursor.fetchall():
        print(row)
    print('waiting 100')
    time.sleep(100)

    db_cursor.close()
    del db_cursor
    db_connection.close()

def print_sql():
    os.system('cls')
    param = (
        r'DRIVER={ODBC Driver 13 for SQL Server};'
        r'SERVER=192.168.0.205,49177;'
        r'DATABASE=master;'
        r'UID=sa;'
        r'PWD=1qaz@WSX3edc'
    )

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

def create_user():
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
    i = 1
    while i < 5:
        sql_command = ("CREATE LOGIN user" + str(i) + " with password = '1qaz@WSX3edc';")
        sql_command1 = ("CREATE USER user" + str(i) + " from login user" + str(i) + ' with default_schema = master;')
        print("creating user", str(i))
        time.sleep(1)
        db_cursor.execute(sql_command)
        db_cursor.execute(sql_command1)
        i = i + 1
    db_connection.autocommit = False
    db_cursor.close()
    del db_cursor
    db_connection.close()

def raiserror():
    os.system('cls')
    param = (
        r'DRIVER={ODBC Driver 13 for SQL Server};'
        r'SERVER=192.168.0.252,1433;'
        r'DATABASE=ksm;'
        r'UID=sa;'
        r'PWD=1qaz@WSX3edc'
    )
    print("function begin!")
    db_connection = pyodbc.connect(param)
    db_connection.autocommit = True
    db_cursor = db_connection.cursor()
    i = 10
    while i < 25:
        try:
            sql_command = ("RAISERROR ('test severity " + str(i) + "'," + str(i) + ", 1) with log;")
            db_cursor.execute(sql_command)
            i = i + 1
        except:
            i = i + 1
            print('caught exception' + str(i))

    db_cursor.close()
    del db_cursor
    db_connection.close()


    # a = 0
    # while a < 10000:
    #     print("doing #" + str(a))
    #     raiserror()
    #     a = a + 1

def deadlock():
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
    db_name = "database_" + str(strftime('%H_%M_%S_%Y', gmtime()))
    print("creating database =>", db_name)
    time.sleep(1)
    try:
        sql_create_db = ("CREATE DATABASE " + db_name)
        db_cursor.execute(sql_create_db)
        print("database create ok")
        time.sleep(1)
    except:
        print("database create fail")

    ##################
    ## select database
    ##################
    try:
        sql_select_db = ("USE " + db_name + ";")
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

def create_db():
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

    i = 1
    while i < 10:
        db_name = "database_" + str(strftime('%H_%M_%S_%Y', gmtime()))
        print("creating database =>", db_name)
        time.sleep(1)
        sql_command = ("CREATE DATABASE " + db_name)
        db_cursor.execute(sql_command)
        i = i + 1

    db_connection.autocommit = False
    db_cursor.close()
    del db_cursor
    db_connection.close()


def create_db1():
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

    i = 1
    while i < 10:
        db_name = "database_" + str(strftime('%H_%M_%S_%Y', gmtime()))
        print("creating database =>", db_name)
        time.sleep(1)
        sql_command = ("CREATE DATABASE " + db_name)
        db_cursor.execute(sql_command)
        i = i + 1

    db_connection.autocommit = False
    db_cursor.close()
    del db_cursor
    db_connection.close()

def gen_time():
    a = strftime('%H%M%S%Y', gmtime())
    print(a)
    d = str(a)
    print(d)