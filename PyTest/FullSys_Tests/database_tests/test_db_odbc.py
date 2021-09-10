import os
import psycopg2
from psycopg2 import Error
from configparser import NoOptionError

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0
def parseODBC():
    print("in parseODBC()")
    # instantiate
    config = ConfigParser()
    
    # read values from a section
    #string_val = config.get('section_a', 'string_val')
    #test_FileParser.pybool_val = config.getboolean('section_a', 'bool_val')
    #int_val = config.getint('section_a', 'int_val')
    #float_val = config.getfloat('section_a', 'pi_val')
#   odbcfile = "~/.odbc.ini"
    odbcfile = "odbc.ini"
    if os.path.isfile(odbcfile):
        config.read(odbcfile)
        checkskip = ["ODBC Data Sources","default"]
        checkgood = []
        checkbad = []
        for SECTION in config.sections():
            print("section: " + SECTION)
            _msg = ""
            if SECTION not in checkskip:
    #        if SECTION != "ODBC Data Sources" or SECTION != "default":
    #           print("section: " + SECTION)
                try:
                    _database = config.get(SECTION,'database')
                except NoOptionError:
                    _msg = "no database defined"
                    checkbad.append(SECTION + ":" + _msg )
                else:

                    try:
                        _server = config.get(SECTION,'servername')
                    except NoOptionError:
                        try:
                            _server = config.get(SECTION,'server')
                        except NoOptionError:
                            _msg = "no server/servername defined"
                            checkbad.append(SECTION + ":" + _msg) 
                    try:
                   # if config.getboolean(SECTION,'encryption') != None:
                        _encryption = config.getboolean(SECTION,'encryption')
                    except NoOptionError:
                        _encryption=""
    
                    try:
                        _port = config.get(SECTION,'port')
#                       if + _port not in ["5432","1433"]:
#                           _msg = "port incorrectly defined flag"
#                           checkbad.append(SECTION + ":" + _msg) 
                    #       break
                            
                    except NoOptionError:
                        _msg="port undefined"
                        checkbad.append(SECTION + ":" + _msg)
                        _port = ""
                    checkgood.append(SECTION)

                print("database: " + _database + "\n")
                print("server: " + _server + "\n")
                print("encryption: " + str(_encryption) + "\n")
                print("port: " + _port + "\n")
#               checkgood.append(SECTION)
                print("\n")
### CHECK PostgreSQL Access
                if _port == "5432":
                    print("database access: " + _database + " - Postgresql")

### CHECK SQLServer Access
                if _port == "1433":
                    print("database access: " + _database + " - MSSQLServer")


    #           print("section: " + SECTION)
    #           for key,value in config[SECTION].items():
    #               print(key,value)
        print("checksgood:\n")
        print(*checkgood,sep="\n")
#       for x in range(len(checkgood)):
#           print(checkgood[x])
 
        print("\n")
        print("checksbad:\n")
        print(*checkbad,sep="\n")
#       for y in range(len(checkbad)):
#           print(checkbad[y])
        print("\n")

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

def baseconnect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        # psycopg2.connect("dbname=test user=postgres password='test'")
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    print("in main")
    parseODBC()
#   valconnect()

#def test_db_fail():
#    assert 1 == 0

#def test_db_success():
#    assert 1 == 1

# update existing value
#config.set('section_a', 'string_val', 'world')

# add a new section and some values
#config.add_section('section_b')
#config.set('section_b', 'meal_val', 'spam')
#config.set('section_b', 'not_found_val', '404')

# save to a file
#with open('test_update.ini', 'w') as configfile:
#    config.write(configfile)
