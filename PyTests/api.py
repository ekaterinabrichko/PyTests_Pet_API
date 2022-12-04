import json

import requests

from settings import VALID_EMAIL, VALID_PASSWORD, REGISTER_EMAIL, REGISTER_PASS


class Pets:
    """ API library to http://34.141.58.52:8080/#/"""

    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """The function is used to get the unique token of the user via defined email and password"""
        data = {"email": VALID_EMAIL, "password": VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, my_id, status

    def get_user_id(self) -> json:
        """The function is used to get user's ID as logged-in user"""  # to be reviewed, should be list of users
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        user_id = res.text
        return status, user_id

    def add_pet(self) -> json:
        """The function is used to add new pet as logged-in user"""
        my_token = Pets().get_token()[0]
        user_id = Pets().get_user_id()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"name": 'Honey', "type": 'cat', "age": 15, "owner_id": user_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def add_pet_photo(self) -> json:
        """The function is used to add photo to already existing pet as logged-in user"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().add_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': ('test.png', open('tests\\Photo\\pet.png', 'rb'), 'image/png')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        return status

    def get_pet_info(self) -> json:
        """The function is used to get info about pet as logged-in user"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().add_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    def add_like(self) -> json:
        """The function is used to press like on any created pet as logged-in user"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().add_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', headers=headers)
        status = res.status_code
        return status

    def add_comment(self) -> json:
        """The function is used to add comment to any created pet as logged-in user"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().add_pet()[0]
        data = {"message": "hello new comment"}
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def delete_pet(self) -> json:
        """The function is used to delete already existing pet as logged-in user"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().add_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    def register_new_user(self) -> json:
        """The function is used to create new user"""
        data = {"email": REGISTER_EMAIL, "password": REGISTER_PASS, "confirm_password": REGISTER_PASS}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        status = res.status_code
        return status

    def delete_user(self) -> json:
        """The function is used to delete logged-in user"""
        data = {"email": REGISTER_EMAIL, "password": REGISTER_PASS}
        res_login = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res_login.json()['token']
        my_id = res_login.json()['id']
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers)
        status = res.status_code
        return status

    def login_as_deleted_user(self) -> json:
        data = {"email": REGISTER_EMAIL, "password": REGISTER_PASS}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        status = res.status_code
        return status


# Pets().get_token()
# Pets().get_user_id()
# Pets().add_pet()
# Pets().add_pet_photo()
# Pets().get_pet_info()
# Pets().delete_pet()
# Pets().add_like()
# Pets().add_comment()
# Pets().register_new_user()
# Pets().delete_user()
# Pets().login_as_deleted_user()
