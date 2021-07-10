import os
import psycopg2
from psycopg2 import Error

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

# instantiate
config = ConfigParser()

# read values from a section
#string_val = config.get('section_a', 'string_val')
#test_FileParser.pybool_val = config.getboolean('section_a', 'bool_val')
#int_val = config.getint('section_a', 'int_val')
#float_val = config.getfloat('section_a', 'pi_val')
odbcfile = "odbc.ini"
if os.path.isfile(odbcfile):
    config.read(odbcfile)
    for SECTION in config.sections():
    #    print("section: " + SECTION)
        if SECTION != "ODBC Data Sources":
            print("\n")
            print("section: " + SECTION)
            for key,value in config[SECTION].items():
                print(key,value)


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
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
    connect()

# update existing value
#config.set('section_a', 'string_val', 'world')

# add a new section and some values
#config.add_section('section_b')
#config.set('section_b', 'meal_val', 'spam')
#config.set('section_b', 'not_found_val', '404')

# save to a file
#with open('test_update.ini', 'w') as configfile:
#    config.write(configfile)
