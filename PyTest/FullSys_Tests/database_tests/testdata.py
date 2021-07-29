import json

class UserData:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self, name):
        for user in self.__data['users']:
            if user['name'] == name:
                return user

    def close(self):
        pass
