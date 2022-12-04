import os

from api import Pets

pt = Pets()


def test_get_token():
    token = pt.get_token()[0]
    status = pt.get_token()[2]
    assert token
    assert status == 200


def test_get_user_id():
    status = pt.get_user_id()[0]
    user_id = pt.get_user_id()[1]
    assert status == 200
    assert user_id


def test_add_pet():
    pet_id = pt.add_pet()[0]
    status_add_pet = pt.add_pet()[1]
    assert pet_id
    assert status_add_pet == 200


def test_add_pet_photo(pet_photo='tests\\photo\\pet.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status = pt.add_pet_photo()
    assert status == 200
    assert pet_photo


def test_delete_pet():
    status = pt.delete_pet()
    assert status == 200


def test_add_like():
    status = pt.add_like()
    assert status == 200


def test_add_comment():
    status = pt.add_comment()
    assert status == 200


def test_register_new_user():
    status = pt.register_new_user()
    assert status == 200


def test_delete_new_user():
    status = pt.delete_user()
    assert status == 200


def test_login_as_deleted_user():
    status = pt.login_as_deleted_user()
    assert status == 400
