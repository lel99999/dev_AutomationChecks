import os, sys
import platform
#import distro

#stat = os.system('service sshd status')
#print("service: " + str(stat))

# Define various services

def getdistro():
    try:
        return distro.linux_distribution()
#       return platform.linux_distribution()
    except:
        return "N/A"

def service_check(_service):
#   _service_check_cmd = ""
    _service_check_cmd = "service sshd status"
    _osName = platform.platform()
    _osSystem = platform.system()
    _stat = os.system(_service_check_cmd)

#   print("platform os: " + _osName + " - " + _osSystem )
    print("Service check result: " + str(_stat))

#print("""Python version: %s
#dist: %s
#linux_distribution: %s
#system: %s
#machine: %s
#platform: %s
#uname: %s
#version: %s
#mac_ver: %s
#""" % (
#sys.version.split('\n'),
#str(distro.linux_distribution(full_distribution_name=False),
#getdistro(),
#platform.system(),
#platform.machine(),
#platform.platform(),
#platform.uname(),
#platform.version(),
#platform.mac_ver(),
#))

print("os name: " + os.name)
print("sys.platform: " + sys.platform)
