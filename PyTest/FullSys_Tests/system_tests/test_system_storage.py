import os.path
from os import path
# get storage mounts from /etc/fstab, check if valid
# run basic latency test of read/write
testpaths = ["/tmp","/Users"]
def checkpath(_path):
#   isFile = os.path.isfile(path)
#   isDir = os.path.isdir(path)
    Path_exists = path.isdir(_path)
    return Path_exists

_mounts = ["/home/data","/home/work","/home/work2"]
def test_storage_mounts():
    """ Check mounts /home/data, /home/work, /home/work2 """
#   assert 1 == 1 
    for ckmount in _mounts:
#       print(ckmount)
        print(ckmount + " : " + str(checkpath(ckmount)))
        assert checkpath(ckmount) == True,"Mount Error: " + ckmount + " possibly not mounted correctly"

if __name__ == "__main__":
    test_storage_mounts()
