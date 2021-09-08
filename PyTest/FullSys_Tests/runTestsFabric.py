import os
import shutil
from fabric import Connection

_hostname = "wdcreeodl02"
_uid = "deploy"
_hoststring = _uid + "@" + _hostname
_tmpPath = "/tmp/autocheck"

# check if /tmp/autocheck exists, then remove
if os.path.exists(_tmpPath):
  try:
    shutil.rmtree(_tmpPath)
  except OSError as e:
    print("Error: %s : %s" % (_tmpPath, e.strerror))

cmdClone = "git clone https://github.com/lel99999/dev_AutomationChecks.git " + _tmpPath
testresult = Connection(_hoststring).run(cmdClone,hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
outfile = open("/tmp/testRun.txt","w")
outfile.write(msg)
outfile.close()
