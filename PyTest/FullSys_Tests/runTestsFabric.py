import os
#import shutil
from fabric import Connection

_hostname = "wdcreeodl02"
_uid = "deploy"
_hoststring = _uid + "@" + _hostname
_tmpPath = "/tmp/autocheck"

def cmdRun(_cmd):
  _tmpResult = Connection(_hoststring).run(_cmd,hide=True)
  msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
  #outfile = open("/tmp/testRun.txt","w")
  outfile = open("/tmp/testRun.txt","a")
  outfile.write(msg)
  outfile.close()

# check if /tmp/autocheck exists, then remove
#if os.path.exists(_tmpPath):
#  os.system("sudo rm -rf " + _tmpPath)
# try:
#   shutil.rmtree(_tmpPath)
# except OSError as e:
#   print("Error: %s : %s" % (_tmpPath, e.strerror))

cmdCleanDir = "rm -rf " + _tmpPath
cmdClone = "git clone https://github.com/lel99999/dev_AutomationChecks.git " + _tmpPath
cmdPyVenv = "python3 -m /tmp/venv3"
cmdPyVenv_Activate = "source /tmp/venv3/bin/activate"
cmdPipReq = "pip install -r " + _tmpPath + "/requirements.txt"
cmdPyTest = "pytest"
cmdPyTest_wReport = "pytest --html-report=/tmp/autocheck/report/testReport.html"

cmdRun(cmdCleanDir)
cmdRun(cmdClone)

#testCleanDir = Connection(_hoststring).run(cmdCleanDir,hide=True)
#testresult = Connection(_hoststring).run(cmdClone,hide=True)

#def cmdRun(_cmd):
#  _tmpResult = Connection(_hoststring).run(_cmd,hide=True)
#  msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
#  #outfile = open("/tmp/testRun.txt","w")
#  outfile = open("/tmp/testRun.txt","a")
#  outfile.write(msg)
#  outfile.close()
