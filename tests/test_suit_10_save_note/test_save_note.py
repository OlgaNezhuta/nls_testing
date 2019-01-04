import requests
import json
from config import *
from helpers.user_helpers import *
from tests.test_suit_10_save_note.save_note_test_data import *

SAVE_NOTE_URI = '/Note/Save'


def test_01_save_note_with_correct_creds():
    url = BASE_URL + SAVE_NOTE_URI
    token = login(LOGIN_CREDS)
    for el in valid_creds:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_02_save_note_with_incorrect_creds():
    url = BASE_URL + SAVE_NOTE_URI
    token = login(LOGIN_CREDS)
    for el in invalid_creds:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == BAD_REQUEST_STATUS_CODE


def test_03_update_note_with_correct_creds():
    url = BASE_URL + SAVE_NOTE_URI
    token = login(LOGIN_CREDS)
    for el in valid_creds_for_updating:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == SUCCESS_STATUS_CODE


def test_04_update_note_with_incorrect_creds():
    url = BASE_URL + SAVE_NOTE_URI
    token = login(LOGIN_CREDS)
    for el in invalid_creds_for_updating:
        r = requests.post(url, data=json.dumps(el), headers={"content-type": "application/json",
                                                                 "Authorization": token})
        print(r.status_code)
        assert r.status_code == BAD_REQUEST_STATUS_CODE


def test_05_save_note_with_unauthorized_user():
    url = BASE_URL + SAVE_NOTE_URI
    r = requests.post(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE



