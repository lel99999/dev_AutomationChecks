import pytest
import os.path
from collections import defaultdict

_servers_svcs = [("server1","check port"),("server1","check path"),("server2","check service"),("server3","check path"),("server4","check path"),("server5","check path"),("server5","check service")]
_dictServersSvcs = defaultdict(list)

for k,v in _servers_svcs:
    _dictServersSvcs[k].append(v)

print("Dictionary of servers and list of svcs to check: ",_dictServersSvcs)


#@pytest.mark.sas
def test_checktmpdir():
    """ Check SAS Scratch Dir/Tmp Dir """
    _tmpdir = '/sastmp'
#    assert os.path.isdir(_tmpdir)
    assert 1 == 0

#@pytest.mark.custom
def test_issue_146():
    pass
#   assert 1 == 1

def test_issue_152():
    pass
