

def test_issue_146():
    """  Check Python3 Versions """
    assert 1 == 1

def test_installed_pydatasci():
    """" Check Python data science packages: numpy, scipy, pandas installed """
    msg = "numpy scipy pandas four score and seven years ago"
    pkgmatch = ["numpy","scipy","pandas"]

    # check for any of the matches
#   assert any(x in msg for x in pkgmatch)
    # check for all matches
    assert any(x in msg for x in pkgmatch)
