from helpers.user_helpers import *
from config import *

GET_PGQ9_URI = '/testing/GetPHQ9'


def test_01_get_phq9_with_valid_creds():
    url = BASE_URL + GET_PGQ9_URI
    token = login(LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_get_phq9_with_unauthorized_user():
    url = BASE_URL + GET_PGQ9_URI
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


def test_03_get_phq9_user_has_no_active_timetable():
    url = BASE_URL + GET_PGQ9_URI
    token = login(LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == BAD_REQUEST_STATUS_CODE


