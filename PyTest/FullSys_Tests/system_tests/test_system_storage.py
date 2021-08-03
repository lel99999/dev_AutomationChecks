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

def test_storage_mounts():
#   assert 1 == 1 
    for ckpath in testpaths:
        print(ckpath + " : " + str(checkpath(ckpath)))


if __name__ == "__main__":
    test_storage_mounts()
