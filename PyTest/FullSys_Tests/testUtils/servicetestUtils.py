import requests

dev test_GET_web(aURL):
    _r = requests.get(aURL)
    return _r.text

dev test_POST_web(aURL):
    pass

