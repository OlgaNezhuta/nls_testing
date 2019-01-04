import requests
import json
from config import *
from tests.test_suit_01_registration.registration_test_data import *

REGISTRATION_URI = '/Account/Register'


def test_01_register_with_correct_creds():
    url = BASE_URL + REGISTRATION_URI
    for el in valid_creds:
        r = requests.post(url, data=json.dumps(el), headers=BASE_HEADERS)
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_02_register_with_incorrect_creds():
    url = BASE_URL + REGISTRATION_URI
    for el in invalid_creds:
        r = requests.post(url, data=json.dumps(el), headers=BASE_HEADERS)
        print(r.status_code)
        assert r.status_code == BAD_REQUEST_STATUS_CODE


def test_03_register_with_existing_creds():
    url = BASE_URL + REGISTRATION_URI
    r = requests.post(url, data=json.dumps(existing_creds), headers=BASE_HEADERS)
    print(r.status_code)
    assert r.status_code == EXISTING_ELEMENT_ERROR_STATUS_CODE











