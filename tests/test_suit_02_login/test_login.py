import requests
import json
from config import *
from tests.test_suit_02_login.login_test_data import *

LOGIN_URI = '/Account/Login'
EMAIL_IS_NOT_CONFIRMED_STATUS_CODE = 405


def test_01_login_with_correct_creds():
    url = BASE_URL + LOGIN_URI
    for el in valid_creds:
        r = requests.post(url, data=json.dumps(el), headers=BASE_HEADERS)
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_02_login_with_incorrect_creds():
    url = BASE_URL + LOGIN_URI
    for el in invalid_creds:
        r = requests.post(url, data=json.dumps(el), headers=BASE_HEADERS)
        print(r.status_code)
        assert r.status_code == BAD_REQUEST_STATUS_CODE


def test_03_login_with_not_confirmed_creds():
    url = BASE_URL + LOGIN_URI
    r = requests.post(url, data=json.dumps(email_is_not_confirmed_creds), headers=BASE_HEADERS)
    print(r.status_code)
    assert r.status_code == EMAIL_IS_NOT_CONFIRMED_STATUS_CODE

