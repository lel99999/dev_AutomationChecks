import requests

def test_GET_web(aURL):
    _r = requests.get(aURL)
    return _r.text

def test_POST_web(aURL):
    pass

print(test_GET_web("https://www.google.com"))

