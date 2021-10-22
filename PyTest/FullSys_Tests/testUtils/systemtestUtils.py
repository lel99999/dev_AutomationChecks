import psutil

def show_all_svcs():
    # return list
    return [(
        psutil.Process(p).name(),
        psutil.Process(p).status(),
        ) for p in psutil.pids()]


print("all_svcs ----------------------------------------------------------")
print(show_all_svcs())

def show_all_kv_svcs():
    _kv_svcs = {}
    # return dict of key,value

    for p in psutil.pids():
        _tmpD = {psutil.Process(p).name():psutil.Process(p).status()}
        _kv_svcs.update(_tmpD)
    return _kv_svcs
#   return [{
#       psutil.Process(p).name():
#       psutil.Process(p).status()
#       } for p in psutil.pids()]

print("\n")
print("kv_svcs ----------------------------------------------------------")
print(show_all_kv_svcs())

def show_running_svcs():
    _runsvcs = {}
    for svc in show_all_svcs():
        if svc[1] == 'running':
            _tmpDic = {svc[0]:svc[1]}
            print(_tmpDic)
            _runsvcs.update(_tmpDic)
    return _runsvcs

print("\n")
print("running_svcs ----------------------------------------------------------")
print(show_running_svcs())

def show_running_svcs_DictComp():
    _dictTest = {'cron':'na','cups':'na'}
    for (k,v) in show_all_kv_svcs().items():
        if k in _dictTest.keys():
            print("key found")

show_running_svcs_DictComp()

def test_check_svc_status():
    _svcmatch = ["msedge","cron"]
    for _svc in show_all_svcs():
        if _svc[1] in _svcmatch:
            print("Match found: " + _svc[1])
#   assert any(y in _svcmatch for _svc[1] in show_all_svcs())

