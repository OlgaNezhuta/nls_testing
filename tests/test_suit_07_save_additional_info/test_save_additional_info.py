import requests
import json
from config import *
from helpers.user_helpers import *
from tests.test_suit_07_save_additional_info.save_additional_info_test_data import *

SAVE_ADDITIONAL_INFO_URI = '/Account/SaveAddititionalInfo'


def test_01_save_additional_info_with_correct_creds():
    url = BASE_URL + SAVE_ADDITIONAL_INFO_URI
    token = login(LOGIN_CREDS)
    for el in valid_creds:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_02_save_additional_info_with_incorrect_creds():
    url = BASE_URL + SAVE_ADDITIONAL_INFO_URI
    token = login(LOGIN_CREDS)
    for el in invalid_creds:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == BAD_REQUEST_STATUS_CODE


def test_03_save_additional_info_with_unauthorized_user():
    url = BASE_URL + SAVE_ADDITIONAL_INFO_URI
    r = requests.post(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE

