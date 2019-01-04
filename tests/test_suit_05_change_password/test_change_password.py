import requests
import json
from config import *
from helpers.user_helpers import *
from tests.test_suit_05_change_password.change_password_test_data import *

CHANGE_PASSWORD_URI = '/Account/ChangePassword'


def test_01_change_password_with_correct_creds():
    url = BASE_URL + CHANGE_PASSWORD_URI
    token = login(LOGIN_CREDS)
    for el in valid_creds:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_02_change_password_with_incorrect_creds():
    url = BASE_URL + CHANGE_PASSWORD_URI
    token = login(LOGIN_CREDS)
    for el in invalid_creds:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == BAD_REQUEST_STATUS_CODE


def test_03_change_password_with_unauthorized_user():
    url = BASE_URL + CHANGE_PASSWORD_URI
    r = requests.post(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


