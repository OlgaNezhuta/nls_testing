from helpers.user_helpers import *
from tests.test_suit_20_add_result.add_result_test_data import *

ADD_RESULT_URI = '/Result/Add'


def test_01_add_result_with_correct_creds():
    url = BASE_URL + ADD_RESULT_URI
    token = login(LOGIN_CREDS)
    for el in valid_creds:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_02_add_result_with_incorrect_creds():
    url = BASE_URL + ADD_RESULT_URI
    token = login(LOGIN_CREDS)
    for el in invalid_creds:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == BAD_REQUEST_STATUS_CODE


def test_03_add_result_with_unauthorized_user():
    url = BASE_URL + ADD_RESULT_URI
    r = requests.post(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE
