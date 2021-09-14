import os

testservices = """
proc-sys-fs-binfmt_misc.automount             static
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
dbus-org.freedesktop.Avahi.service            enabled
"""

def get_TestServices():
    return testservices

def get_KV_TestServices():
    _kv = {}
    for l in testservices.splitlines():
        print("line: " + l)
        k,v = l.split("  ",2)
        _kv.setdefault(k.strip(),v.strip())
        return _kv

print(get_KV_TestServices())
