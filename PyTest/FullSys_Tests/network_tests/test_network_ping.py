from operator import truediv
from pickle import TRUE


import platform    # For getting the operating system name
import subprocess  # For executing a shell command

hostlist = ["127.0.0.1"]
def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def test_ping(hostlist=[],*args):
#    _host = "127.0.0.1" #localhost
#    assert ping(_host)
    for h in hostlist:
        print("host: " + h)
        assert ping(h)