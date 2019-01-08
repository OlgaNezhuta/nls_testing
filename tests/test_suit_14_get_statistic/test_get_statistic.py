from helpers import *
from config import *

GET_STATISTIC_URI = '/Result/GetDailyInfo/2019-01-08'


def test_01_get_statistic_with_valid_token():
    url = BASE_URL + GET_STATISTIC_URI
    token = login(LOGIN_CREDS)
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_get_statistic_with_unauthorized_user():
    url = BASE_URL + GET_STATISTIC_URI
    r = requests.get(url, headers={"content-type": "application/json", "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE
