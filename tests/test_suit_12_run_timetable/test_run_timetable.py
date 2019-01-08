from tests.test_suit_12_run_timetable.run_timetable_test_data import *
from helpers.user_helpers import *

RUN_TIMETABLE_URI = '/Timetable/Run'


def test_01_run_timetable_with_correct_creds():
    url = BASE_URL + RUN_TIMETABLE_URI
    token = login(LOGIN_CREDS)
    r = requests.post(url, data=json.dumps(timetable_creds), headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_run_timetable_when_user_has_current_timetable():
    url = BASE_URL + RUN_TIMETABLE_URI
    token = login(LOGIN_CREDS)
    r = requests.post(url, data=json.dumps(timetable_creds), headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == EXISTING_ELEMENT_ERROR_STATUS_CODE


def test_03_run_timetable_with_unauthorized_user():
    url = BASE_URL + RUN_TIMETABLE_URI
    r = requests.post(url, data=json.dumps(timetable_creds), headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE

