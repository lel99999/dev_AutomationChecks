import os,sys
#import shutil
from fabric import Connection

_hostname = "wdcreancil01"
_uid = "deploy"
_hoststring = _uid + "@" + _hostname
_tmpPath = "/tmp/autocheck"
_tmpVenv3Path = "/tmp/venv3"

def cmdRun(runcmd):
    _cmd = runcmd
    try:
        _tmpStdOut = Connection(_hoststring).run(_cmd,hide=True).stdout.strip()
        msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
    except:
        print("Error: ", sys.exc_info()[0], "occurred.")
    print("--- " + _cmd)
# print("--- " + _tmpStdOut)
      
# outfile = open("/tmp/testRun.txt","w")
# outfile = open("/tmp/testRun.txt","a")
# outfile.write(msg)
# outfile.close()

# check if /tmp/autocheck exists, then remove
#if os.path.exists(_tmpPath):
#  os.system("sudo rm -rf " + _tmpPath)
# try:
#   shutil.rmtree(_tmpPath)
# except OSError as e:
#   print("Error: %s : %s" % (_tmpPath, e.strerror))

cmdCleanDir = "rm -rf " + _tmpPath
cmdCleanVenv = "rm -rf /tmp/venv3"
cmdClone = "git clone https://github.com/lel99999/dev_AutomationChecks.git " + _tmpPath
cmdPyVenv = "/bin/python3 -m venv /tmp/venv3"
#cmdVenv3Fix = "chmod -R 777 /tmp/venv3"
cmdPyVenv_Activate = "source /tmp/venv3/bin/activate"

# Pip has error: No module named 'setuptools_rust'
cmdPipRustFix = "/tmp/venv3/bin/pip3 install setuptools-rust"

cmdPipUpgrade = "/tmp/venv3/bin/pip3 install -U pip setuptools"

# Pip has error: Install psycopg2-binary instead
cmdPipPsycopg2Fix = "/tmp/venv3/bin/pip3 install psycopg2-binary"

# Explicit install of pytest via pip
cmdPipPytest = "/tmp/venv3/bin/pip3 install pytest pytest-html-reporter"

# Report Tmp Staging Location
cmdMkReportDir = "mkdir -p " + _tmpPath + "/report"
cmdModReportDirPerm = "chmod -R 777 " + _tmpPath + "/report"
cmdModCacheDirPerm = "chmod -R 777 " + _tmpPath + "/PyTest/FullSys_Tests"

cmdPipReq = "/tmp/venv3/bin/pip3 install -r " + _tmpPath + "/PyTest/FullSys_Tests/requirements.txt"
cmdPyTest = "pytest"
cmdPyTest_wReport = "/tmp/venv3/bin/pytest " + _tmpPath + "/PyTest/FullSys_Tests/system_tests/" + " --html-report=/tmp/autocheck/report/testReport.html" + " -rs -v"
cmdPyTest_wReport_Fixture = "/tmp/venv3/bin/pytest " + _tmpPath + "/PyTest/FullSys_Tests/system_tests/" + " --html-report=/tmp/autocheck/report/testReport.html" + " -rs -v -m custom"

from datetime import datetime
now = datetime.now()
_datetime = now.strftime("%m-%d-%Y--%H:%M:%S")
cmdReportStage = "cp /tmp/autocheck/report/testReport.html " + "/opt/pytest_stage/pytestReport_" + _datetime + ".html" 

cmdRun(cmdCleanDir)
cmdRun(cmdCleanVenv)
cmdRun(cmdClone)
cmdRun(cmdPyVenv)
#cmdRun(cmdVenv3Fix)
cmdRun(cmdPyVenv_Activate)
cmdRun(cmdPipRustFix)
cmdRun(cmdPipUpgrade)
cmdRun(cmdPipPsycopg2Fix)
cmdRun(cmdPipPytest)
cmdRun(cmdMkReportDir)
cmdRun(cmdModReportDirPerm)
cmdRun(cmdModCacheDirPerm)
cmdRun(cmdPipReq)

cmdRun(cmdPyTest_wReport)

cmdRun(cmdReportStage)

#testCleanDir = Connection(_hoststring).run(cmdCleanDir,hide=True)
#testresult = Connection(_hoststring).run(cmdClone,hide=True)

#def cmdRun(_cmd):
#  _tmpResult = Connection(_hoststring).run(_cmd,hide=True)
#  msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
#  #outfile = open("/tmp/testRun.txt","w")
#  outfile = open("/tmp/testRun.txt","a")
#  outfile.write(msg)
#  outfile.close()
