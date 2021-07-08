import os.path
import pyodbc

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

config = ConfigParser()


# Scan .odbc.ini for Datasources
odbcfile = "~/.odbc.ini"
if path.exists(odbcfile):
    config.read(odbcfile)
    for SECTION in config.sections(): 
        print("section: " + SECTION)
        
# BASIC SQL Server
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')

# Using a DSN, but providing a password as well
cnxn = pyodbc.connect('DSN=test;PWD=password')

# Create a cursor from the connection
cursor = cnxn.cursor()

cursor.execute("select user_id, user_name from users")
row = cursor.fetchone()
if row:
    print(row)

cursor.execute("select user_id, user_name from users"):
for row in cursor:
    print(row.user_id, row.user_name)

# BASIC PostgreSQL
conn = pyodbc.connect('DRIVER=/usr/pgsql/lib/psqlodbc.so;SERVER=<servername>;PORT=5432;DATABASE=<databasename>;UID=<uid>;PWD=<pwd>;')
cursor = conn.cursor()
for row in cursor.execute('select 2 * 2 as [Result];'):
    print row.Result
