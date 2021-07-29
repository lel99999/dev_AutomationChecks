from testdata import UserData
import pytest

@pytest.fixture(scope='module')
def db():
    print('\n*****SETUP*****\n')
    db = UserData()
    db.connect('userdata.json')
    yield db
    print('\n******TEARDOWN******\n')
    db.close()

def test_sally_data(db):
    print('... In test Sally')
    sally_data = db.get_data('Sally.Jones')
    assert sally_data['id'] == 1
    assert sally_data['name'] == 'Sally.Jones'
    assert sally_data['title'] == 'manager'

def test_joe_data(db):
    print('... In test Joe')
    joe_data = db.get_data('Joe.Smith')
    assert joe_data['id'] == 2
    assert joe_data['name'] == 'Joe.Smith'
    assert joe_data['title'] == 'employee'
