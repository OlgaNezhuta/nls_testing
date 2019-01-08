from helpers.user_helpers import *
from config import *

GET_DAILY_INFO_URI = '/Result/GetDailyInfo/2019-01-08'


def test_01_get_daily_info_with_valid_token():
    url = BASE_URL + GET_DAILY_INFO_URI
    token = login(LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_get_daily_info_with_unauthorized_user():
    url = BASE_URL + GET_DAILY_INFO_URI
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


