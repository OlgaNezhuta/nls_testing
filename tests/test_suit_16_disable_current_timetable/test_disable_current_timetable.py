from helpers.user_helpers import *


DISABLE_CURRENT_TIMETABLE_URI = '/Timetable/Disable'


def test_01_disable_current_timetable_with_valid_creds():
    url = BASE_URL + DISABLE_CURRENT_TIMETABLE_URI
    token = login(LOGIN_CREDS)
    r = requests.delete(url, headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_disable_current_timetable_with_invalid_token():
    url = BASE_URL + DISABLE_CURRENT_TIMETABLE_URI
    r = requests.delete(url, headers={"content-type": "application/json", "Authorization": "wretewrtwertw"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


def test_03_disable_current_timetable_with_no_current_timetable():
    url = BASE_URL + DISABLE_CURRENT_TIMETABLE_URI
    token = login(LOGIN_CREDS)
    r = requests.delete(url, headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == BAD_REQUEST_STATUS_CODE
