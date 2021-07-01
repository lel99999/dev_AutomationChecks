# dev_AutomationChecks
Exploratory Development with Automated System Checks and Reporting
#### Frameworks to Review
- [ ] BATS (Bash Automated Testing System) - [https://github.com/sstephenson/bats](https://github.com/sstephenson/bats) 
- [ ] Ansible RSpec = [https://github.com/volanja/ansible_spec](https://github.com/volanja/ansible_spec)
- [ ] Spock = [https://spockframework.org/](https://spockframework.org/)
- [ ] PyTest = [https://pytest.org](https://pytest.org) 
      <li>with Selenium [https://www.lambdatest.com/blog/pytest-report-generation-for-selenium-automation-scripts/](https://www.lambdatest.com/blog/pytest-report-generation-for-selenium-automation-scripts/)</li> <br/> 
      <li> Add PyTest-html for reports [https://pytest-html.readthedocs.io/en/latest/user_guide.html](https://pytest-html.readthedocs.io/en/latest/user_guide.html) </li><br/>

#### Add Environment Specific Checks
- Check Python 2.x, 3.x versions
- Check SCL Python 3.x
- Check VirtualEnv 
- Check if Python Packages have been installed
  - numpy
  - scipy
  - pandas

#### Add User Specific Checks
- User Exists <br/>
- User Creation <br/>
  - in correct AD groups <br/>
  - getfacl/setfacl has correct ACLs <br/>
- User .bashrc and other information created/exits <br/>
  - within .bashrc STATATMP and crk variables are set <br/>
  - within .bash_profile include correct PATH additions <br/>

Issue #142 <br/>
- Confirm STATA serers are running<br/>
- Confirm <org>, data,work,work2 mounts are function on _adml06<br/>
- Check no 0kb duplicate files exists<br/>
- Check SASStudio is funcioning correctly<br/>
- Check RStudio is functioning correctly<br/>
- Check mounts on _adml06'<br/>

Issue #159 <br/>
- Check .bashrc for existence/defined crk and STATATMP <br/>


#### Add Directory Checks
- Check mounts from /etc/fstab <br/>

#### Headless Client Testing
https://docs.travis-ci.com/user/gui-and-headless-browsers/

#### Add HTML Output

#### Add Selenium Testing
  
#### Add Infrastructure Code

#### BDD Frameworks in Python
Behave - [http://pythonhosted.org/behave](http://pythonhosted.org/behave) <br/>
Lettuce = [http://lettuce.it/intro/overview.html](http://lettuce.it/intro/overview.html) <br/>

Largely modeled after cucumber, the BDD framework in Ruby which was the first story-based framework in RSpec <br/>

#### Add ODBC Testing
Using pyodbc: <br/>

Installing pyodbc <br/>
```
$sudo yum install epel-release
$sudo yum install python3-pip gcc-c++ python3-devel unixODBC-devel
$pip3 install --user pyodbc
```

Connect to a Database:
```
import pyodbc

# Specifying the ODBC driver, server name, database, etc. directly
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

```
MS SQL Server Test:
```
#BASIC MS SQL Server
conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=<servername>;PORT=5432;DATABASE=<databasename>;UID=<uid>;PWD=<pwd>;')
cursor = conn.cursor()
for row in cursor.execute('select 2 * 2 as [Result];'):
    print row.Result
 
```

PostgreSQL Test:
```
#BASIC PostgreSQL
conn = pyodbc.connect('DRIVER=/usr/pgsql/lib/psqlodbc.so;SERVER=<servername>;PORT=5432;DATABASE=<databasename>;UID=<uid>;PWD=<pwd>;')
cursor = conn.cursor()
for row in cursor.execute('select 2 * 2 as [Result];'):
    print row.Result
```
