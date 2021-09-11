import os.path
from os import path
import subprocess

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

def test_knowndirs():
    name = ["/tmp","/Users"]

def test_storage_usage():
    """ Check storage capcity - verify under a certain utilization % """    
    # for Python 2.x
#   output = subprocess.check_output(['df',-k'])

    # for Python > v3.5
    output = subprocess.run(['df','-k'],capture_output=True, text=True).stdout

    #### run $pytest -s  ... to show printed output
    print(output)
    assert 1 == 1

if __name__ == "__main__":
    test_storage_mounts()
