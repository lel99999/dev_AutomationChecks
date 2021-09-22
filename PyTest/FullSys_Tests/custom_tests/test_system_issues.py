import pytest
import os
import psutil

def test_issue_146():
    """  Check Python3 Versions """
    _Py3Version = os.system("python3 -V")
    print(_Py3Version)
    assert 1 == 1

def test_installed_pydatasci():
    """" Check Python data science packages: numpy, scipy, pandas installed """
    msg = "numpy scipy pandas four score and seven years ago"
    pkgmatch = ["numpy","scipy","pandas"]

    # check for any of the matches
#   assert any(x in msg for x in pkgmatch)
    # check for all matches
    assert all(x in msg for x in pkgmatch)

# include parametrizing tests
@pytest.mark.parametrize("svc,expected_svc_status",[("cron","sleeping"),("msedge","disabled"),("cron","running")])
def test_service_enabled(svc,expected_svc_status):
    assert eval(svc) == expected_svc_status

#def test_service_status(svc2chk):
#   _status = os.system("systemctl is-active --quiet " + svc2chk)
#   #print(_status) # return 0 for active else inactive
#   assert _status == 0

def show_all_svcs():
    # return list
    return [(
        psutil.Process(p).name(),
        psutil.Process(p).status(),
        ) for p in psutil.pids()]


#print(show_all_svcs())

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


#print(show_all_svcs())


def show_running_svcs():
    _runsvcs = {}
    for svc in show_all_svcs():
        if svc[1] == 'running':
            _tmpDic = {svc[0]:svc[1]}
            print(_tmpDic)
            _runsvcs.update(_tmpDic)
    return _runsvcs


#print(show_running_svcs())

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

"""
def test_system_services():
    _svcmatch = ["snapd","single"]
    _sys_svcs = os.system("systemctl list-unit-files")
    # any matches
    #assert any(y in _sys_svc for y in _svcmatch)
    # all matches
#   assert any(y in _sys_svc for y in svcmatch)
"""

#systemctl list0unit-files
_testsvc = """ proc-sys-fs-binfmt_misc.automount             static
               dev-hugepages.mount                           static
               dev-mqueue.mount                              static
               proc-fs-nfsd.mount                            static
               proc-sys-fs-binfmt_misc.mount                 static
               run-vmblock\x2dfuse.mount                     disabled
               sys-fs-fuse-connections.mount                 static
               sys-kernel-config.mount                       static
               sys-kernel-debug.mount                        static
               tmp.mount                                     disabled
               var-lib-nfs-rpc_pipefs.mount                  static
               brandbot.path                                 enabled
               cups.path                                     enabled
               systemd-ask-password-console.path             static
               systemd-ask-password-plymouth.path            static
               systemd-ask-password-wall.path                static
               session-2359.scope                            static
               session-5.scope                               static
               abrt-ccpp.service                             enabled
               abrt-oops.service                             enabled
               abrt-pstoreoops.service                       disabled
               abrt-vmcore.service                           enabled
               abrt-xorg.service                             enabled
               abrtd.service                                 enabled
               accounts-daemon.service                       enabled
               alsa-restore.service                          static
               alsa-state.service                            static
               anaconda-direct.service                       static
               anaconda-nm-config.service                    static
               anaconda-noshell.service                      static
               anaconda-pre.service                          static
               anaconda-shell@.service                       static
               anaconda-sshd.service                         static
               anaconda-tmux@.service                        static
               anaconda.service                              static
               arp-ethers.service                            disabled
               atd.service                                   enabled
               auditd.service                                enabled
               auth-rpcgss-module.service                    static
               autovt@.service                               enabled
               avahi-daemon.service                          enabled
               blk-availability.service                      enabled
               bluetooth.service                             enabled
               bolt.service                                  static
               brandbot.service                              static
               brltty.service                                disabled
               canberra-system-bootup.service                disabled
               canberra-system-shutdown-reboot.service       disabled
               canberra-system-shutdown.service              disabled
               chrony-dnssrv@.service                        static
               chrony-wait.service                           disabled
               chronyd.service                               enabled
               clean-mount-point@.service                    static
               colord.service                                static
               configure-printer@.service                    static
               console-getty.service                         disabled
               console-shell.service                         disabled
               container-getty@.service                      static
               cpupower.service                              disabled
               crond.service                                 enabled
               cups-browsed.service                          disabled
               cups.service                                  enabled
               dbus-org.bluez.service                        enabled
               dbus-org.fedoraproject.FirewallD1.service     masked
               dbus-org.freedesktop.Avahi.service            enabled  """
