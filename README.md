# dev_AutomationChecks
Exploratory Development with Automated System Checks and Reporting
#### Frameworks to Review
- [ ] BATS (Bash Automated Testing System) - [https://github.com/sstephenson/bats](https://github.com/sstephenson/bats) 
- [ ] Ansible RSpec = [https://github.com/volanja/ansible_spec](https://github.com/volanja/ansible_spec)
- [ ] Spock = [https://spockframework.org/](https://spockframework.org/)
- [ ] Unnittest - [https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)
- [ ] PyTest = [https://pytest.org](https://pytest.org) 
      <li>with Selenium [https://www.lambdatest.com/blog/pytest-report-generation-for-selenium-automation-scripts/](https://www.lambdatest.com/blog/pytest-report-generation-for-selenium-automation-scripts/)</li> <br/> 
      <li> Add PyTest-html for reports [https://pytest-html.readthedocs.io/en/latest/user_guide.html](https://pytest-html.readthedocs.io/en/latest/user_guide.html) </li><br/>
      <li> Docker Test Fixture [https://testinfra.readthedocs.io/en/latest/examples.html](https://testinfra.readthedocs.io/en/latest/examples.html) </li><br/>
   ___Pytest Exit Codes___ <br/>
   Possible exit codes <br/>
   Running pytest can result in six different exit codes: <br/>

   - Exit code 0 <br/>
     All tests were collected and passed successfully </br/>

   - Exit code 1 <br/>
     Tests were collected and run but some of the tests failed

   - Exit code 2 <br/>
     Test execution was interrupted by the user

   - Exit code 3 <br/>
     Internal error happened while executing tests

   - Exit code 4 <br/>
     pytest command line usage error

   - Exit code 5 <br/>
     No tests were collectedkkkk#### (1) Add Environment Specific Checks <br/>
     
- Check Python 2.x, 3.x versions
- Check SCL Python 3.x
- Check VirtualEnv 
- Check if Python Packages have been installed
  - numpy
  - scipy
  - pandas
- Check known Services
- Add Redis for caching capabilities


#### Visual Profiling
- Visual Profiler for Python [https://github.com/nvdv/vprof](https://github.com/nvdv/vprof) <br/>

#### Cookiecutter Templates for PyTest
- [https://github.com/pytest-dev/cookiecutter-pytest-plugin](https://github.com/pytest-dev/cookiecutter-pytest-plugin) <br/>
- [Common Patterns for Tests - from Scientific Cookiecutter](https://nsls-ii.github.io/scientific-python-cookiecutter/advanced-testing.html) <br/>

#### Python Based Agents and Agent Library/Frameworks/Projects
- [https://pypi.org/project/agent/](https://pypi.org/project/agent/)
- [https://pypi.org/project/spade/](https://pypi.org/project/spade/)
- [https://pade.readthedocs.io/en/latest/](https://pade.readthedocs.io/en/latest/)
- [https://mesa.readthedocs.io/en/stable/](https://mesa.readthedocs.io/en/stable/)

#### Add tox for Python vitualenv and pytest mgmt
- [https://tox.readthedocs.io/en/latest/index.html](https://tox.readthedocs.io/en/latest/index.html)

#### (2) Add User Specific Checks
- User Exists
- User Creation
  - in correct AD groups
  - getfacl/setfacl has correct ACLs
- User .bashrc and other information created/exits 
  - within .bashrc STATATMP and crk variables are set
  - within .bash_profile include correct PATH additions

Issue #142 <br/>
- Confirm STATA servers are running
- Confirm <org>, data,work,work2 mounts are function on _adml06
- Check no 0kb duplicate files exists
- Check SASStudio is funcioning correctly
- Check RStudio is functioning correctly
- Check mounts on _adml06'

Issue #159 <br/>
- Check .bashrc for existence/defined crk and STATATMP


#### Add Directory Checks
- Check mounts from /etc/fstab
```
$sudo systemctl list-units --type mount
```
      
#### Headless Client Testing
https://docs.travis-ci.com/user/gui-and-headless-browsers/

#### Add HTML Output
[x] Done
      
#### Add Selenium Testing
Example 1: <br/>
```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
_username = "testuser1"
_pwd = "test@bc"
driver = webdriver.Firefox()
driver.get("https://<some_Url_with_login")
element = driver.find_element_by_id("email")
element.send_keys(_username)
element = driver.find_element_by_id("pwd")
element.send_keys(_pwd)
element.send_keys(Keys.RETURN)
element.close()
```      
##### May need to install firefox-geckodriver
Error Messgae: WebDriverException: Message: 'geckodriver' executable needs to be in PATH. <br/>
```
$sudo yum install firefox-geckodriver
```
      
#### (3) Add Infrastructure Code
- TestSuite to possibly include:
      - Networking
      - Storage
      - Databases
      - System
      - User/IAM

#### BDD Frameworks in Python
Behave - [http://pythonhosted.org/behave](http://pythonhosted.org/behave) <br/>
Lettuce = [http://lettuce.it/intro/overview.html](http://lettuce.it/intro/overview.html) <br/>

Largely modeled after cucumber, the BDD framework in Ruby which was the first story-based framework in RSpec <br/>

#### (4) Add ODBC Testing
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

# Specifying the ODBC driver, server name, database, etc. directly; Add Trusted_Connection=yes for AD Secured kerberized access
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass;Trusted_Connection=yes')

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
Install Microsoft SQL Server ODBC Driver v17:

#Install packages-microsoft-prod.rpm: <br/>
`$sudo yum install https://packages.microsoft.com/config/rhel/7/packages-microsoft-prod.rpm` <br/>
Install msodbcsql17 rpm package: <br/>
`$sudo yum install msodbcsql17` <br/>

Add to odbc.ini:
```
[ODBC Driver 17 for SQL Server]
Description=Microsoft ODBC Driver 17 for SQL Server
Driver=$(ls /opt/microsoft/msodbcsql17/lib64/libmsodbc*)
UsageCount=1
```   
      
MS SQL Server Test:
```
#BASIC MS SQL Server 
# - Require Trusted_Connection parameter
# - May require $kinit for Kerberos principal
conn = pyodbc.connect('DRIVER=FreeTDS;SERVER=<servername>;PORT=5432;DATABASE=<databasename>;UID=<uid>;PWD=<pwd>;Trusted_Connection=yes;')
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
#### (5) Incorporate Fabric 
[http://www.fabfile.org/](http://www.fabfile.org/) <br/>
Example 1:<br/>

```
>>> from fabric import Connection
>>> result = Connection('web1.example.com').run('uname -s', hide=True)
>>> msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
>>> print(msg.format(result))
Ran 'uname -s' on web1.example.com, got stdout:
Linux
```

#### Incorporate Fabric Invocations (Invoke-only, locally-focused CLI tasks)
- [https://invocations.readthedocs.io/en/latest/](https://invocations.readthedocs.io/en/latest/) <br/>
- [Invocation Error/Error Handling](https://github.com/fabric/fabric/issues/1659) <br/>      
      
#### Use Python Selenium to functionally test web app
Can use basic wget/curl ... but multiple step process, may require more sophisticated functional test for validation

Example 1: <br/>
```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()```
```
***Using with remote webdriver*** <br/>
Example 2: <br/>
```
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.CHROME)

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.OPERA)

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)
```
#### Report Notes
      - Ensure report output directory has <filename>.html and output.json to build archive folder </br> 

#### SAS Testing Information
- [https://communities.sas.com/t5/SAS-Communities-Library/Test-Driven-Data-Science-Writing-Unit-Tests-for-SASPy-Python/ta-p/457065](https://communities.sas.com/t5/SAS-Communities-Library/Test-Driven-Data-Science-Writing-Unit-Tests-for-SASPy-Python/ta-p/457065) <br/>
- [https://github.com/sassoftware/saspy](https://github.com/sassoftware/saspy) <br/>

#### CURL Notes
- Return only HTTP headers of a URL
  ```
  $curl -I https://www.example.com
  ```

- Saving the result of a curl command
  ```
  $curl -o filename.ex1 https://www.example.com/filename.ex1

  # Save with original filename
  $curl -O https://www.example.com/filename.example
  ```

- Adding an additional HTTP request header
  ```
  $curl -H "X-Header: value" https://www.example.com
  ```

- Generating additional info (adding -v)
  ```
  $curl -H "X-Header: value" https://www.example.com -v
  ```
- Download Multiple files
  ```
  $curl -O http://mirrors.edge.kernel.org/archlinux/iso/2018.06.01/archlinux-2018.06.01-x86_64.iso  \
  $     -O https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-9.4.0-amd64-netinst.iso
  ```

- Curl with Proxy (using -x or -proxy switch)
  ```
  $curl -x "http://user:pwd@<proxy_ip>:<port>" "http://www.example.com/"
  
  or
  
  $curl -proxy "http://user:pwd@<proxy_ip>:<port>" "http://www.example.com/"
  
  ## For some curl versions, need to use following:
      
  $curl -x http://proxy_server:proxy_port --proxy-user username:password -L http://url
  ### If there are SSL certificate errors, add -k
  $curl -x "http://user:pwd@<proxy_ip>:<port>" "http://www.example.com/" -k
  ```
  - Use environment variables to set proxy
    ```
    $export http_proxy=http://your.proxy.server:port/
    $export https_proxy=https://your.proxy.server:port/
    ```
  - If using a SOCKS proxy instead of http/https, use --socks5 switch
    ```
    $curl --socks5 <proxy_ip>:<proxy_port> http://example.com/
    ```
  - Alias Proxyon / Proxyoff -switch by adding to .bashrc 
    ```
    $alias proxyon="export http_proxy='http://YOURPROXY:YOURPORT';export https_proxy='http://YOURPROXY:YOURPORT'"
    $alias proxyoff="export http_proxy='';export https_proxy=''"

    ```
- Using environment variables (will apply system-wide)
  - http_proxy: proxy will be used to access addresses that use http protocol
  - https_proxy: proxy will be used to access addresses that use https protocol
  ```
  $export http_proxy="http://user:pwd@127.0.0.1:1234"
  $export https_proxy="http://user:pwd@127.0.0.1:1234"

  # to unset or clear the environment variables
  $unset http_proxy
  $unset https_proxy
  ```

- Using a curl config file [https://everything.curl.dev/cmdline/configfile](https://everything.curl.dev/cmdline/configfile)
  - Tell curl to use command-line options from a specific file with the -K/--config options
  ```
  $curl -K cmdline_file.txt http://www.example.com
  ```
