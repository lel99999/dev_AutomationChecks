import pytest
import os.path

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
