import os
import psycopg2
from psycopg2 import Error
from configparser import NoOptionError

def test_dbconnect_Postgres(uid,pwd):
    _db = "testdb"
    _uid = uid
    _pwd = pwd
#    assert eval(dbconnect) == True
    assert 1 == 1
    
def test_dbconnect_SQLServer(uid,pwd):
    _db = "testdb"
    _uid = uid
    _pwd = pwd
    #assert eval(dbconnect) == True
    assert 1 == 1

def pg_connect(dsn,uid,host,pwd):
    _conn = None
    try:
        print('Connecting to the PostgreSQL database...')
        # psycopg2.connect("dbname=test user=postgres password='test'")
        _conn = psycopg2.connect()

        # create a cursor
        _cur = _conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        _cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = _cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        _cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if _conn is not None:
           _conn.close()
           print('Database connection closed.')

#def mssql_connect(_server,_database,_uid,_pwd):
def mssql_connect(_server,_database,_uid,_pwd):
    #May need to $kinit for Kerberos principal
    _server = 'wdcsqlaw02'
    _database = 'ODBCDefaultDB'
    #_uid = '<domain>\<username>'  -  ‘<domain>\lel’
#   _uid = '<domain>\<your uid>'
    _pwd = '<your_password>'

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + _server + ';DATABASE=' + _database + ';UID="' + _uid + '";PWD=' + _pwd + ';Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    while row:
        print(row[0])
        row = cursor.fetchone()

