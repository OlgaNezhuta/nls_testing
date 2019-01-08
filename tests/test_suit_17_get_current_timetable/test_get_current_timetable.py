from helpers.user_helpers import *
from config import *

GET_CURRENT_TIMETABLE_URI = '/Timetable/GetCurrentTimetable'


def test_01_get_current_timetable_with_valid_creds():
    url = BASE_URL + GET_CURRENT_TIMETABLE_URI
    token = login(LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_get_current_timetable_with_unauthorized_user():
    url = BASE_URL + GET_CURRENT_TIMETABLE_URI
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE




