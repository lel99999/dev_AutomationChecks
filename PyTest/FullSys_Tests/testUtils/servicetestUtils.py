import requests
import pytest

@pytest.fixture
def aURL():
    return "https://www.google.com"

#aURL = "https://www.google.com"
def test_req_res(aURL):
    _res = requests.get(aURL)
    print(_res.ok)
    assert(_res.ok) == True

# API Tests
#def test_GET_web(aURL):
#    _res = requests.get(aURL)
#    return _res.text

#def test_POST_web(aURL):
#    pass

#print(test_req_res("https://www.google.com"))

#print(test_GET_web("https://www.google.com"))

