from helpers.user_helpers import *
from tests.test_suit_09_get_notes.get_notes_test_data import *

GET_NOTES_URI = '/Note/GetAll'


def test_01_get_notes_with_valid_token_and_pagination():
    url = BASE_URL + GET_NOTES_URI
    token = login(LOGIN_CREDS)
    for el in payload:
        r = requests.get(url, params=el, headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_02_get_notes_with_unauthorized_user():
    url = BASE_URL + GET_NOTES_URI
    r = requests.get(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE
