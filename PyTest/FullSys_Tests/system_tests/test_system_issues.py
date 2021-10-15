import pytest
import os.path
from collections import defaultdict

_servers_svcs = [("server1","check port"),("server1","check path"),("server2","check service"),("server3","check path"),("server4","check path"),("server5","check path"),("server5","check service")]
_dictServersSvcs = defaultdict(list)

for k,v in _servers_svcs:
    _dictServersSvcs[k].append(v)

print("(1) Dictionary of servers and list of svcs to check: ", _dictServersSvcs)

_dict_servers_svcs = {}
_dict_servers_svcs["server1"] = ["check port","check path","check dir","check service"]
_dict_servers_svcs["server2"] = ["check port","check service"] 
_dict_servers_svcs["server3"] = ["check service"] 
_dict_servers_svcs["server4"] = ["check path","check dir"]
_dict_servers_svcs["server5"] = ["check service","check path","check port"] 

print("(2) Dictionary of servers/checks lists: ", _dict_servers_svcs)

_dictServers = {}
_dictServers["server1"] = ["check port","check path"]
_dictServers["server2"] = ["check port","check service","check path"]
_dictServers["server3"] = ["check service","check port"]
_dictServers["server4"] = ["check service"]
_dictServers["server5"] = ["check path","check service"]

_addSvcChecks1 = ["check user","check acl"]
_addSvcChecks2 = ["check service account","check enabled"]
_addSvcChecks3 = ["check fw type","check fw rule"]

_dictServers["server1"].append(_addSvcChecks2)
_dictServers["server3"].append(_addSvcChecks1)
_dictServers["server5"].append(_addSvcChecks3)

print("(3) Dictionary of servers/checks lists: ", _dictServers)


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
