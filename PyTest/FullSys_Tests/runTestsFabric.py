from fabric import Connection

cmdClone = "git clone https://github.com/lel99999/dev_AutomationChecks.git /tmp/autocheck"
testresult = Connection('wdcreeodl02').run(cmdClone,hide=True)
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
outfile = open("/tmp/testRun.txt","w")
outfile.write(msg)
outfile.close()
