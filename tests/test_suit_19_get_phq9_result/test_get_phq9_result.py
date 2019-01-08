from helpers.user_helpers import *
from config import *

GET_PGQ9_RESULT_URI = '/testing/GetPHQ9Result'


def test_01_get_phq9_result_with_valid_creds():
    url = BASE_URL + GET_PGQ9_RESULT_URI
    token = login(LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_get_phq9_result_with_unauthorized_user():
    url = BASE_URL + GET_PGQ9_RESULT_URI
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


def test_03_get_phq9_user_has_no_result():
    url = BASE_URL + GET_PGQ9_RESULT_URI
    token = login(LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == NOT_FOUND_STATUS_CODE


def test_04_get_phq9_user_has_no_current_timetable():
    url = BASE_URL + GET_PGQ9_RESULT_URI
    token = login(LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == BAD_REQUEST_STATUS_CODE





