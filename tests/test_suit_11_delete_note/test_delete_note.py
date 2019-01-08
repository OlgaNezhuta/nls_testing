from helpers.user_helpers import *


DELETE_NOTE_URI = '/Note/Delete'


def test_01_gelete_note_with_valid_token():
    url = BASE_URL + DELETE_NOTE_URI
    token = login(LOGIN_CREDS)
    payload = create_some_note()
    r = requests.delete(url, params={"noteId": payload}, headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_gelete_note_with_invalid_token():
    url = BASE_URL + DELETE_NOTE_URI
    r = requests.delete(url, params={"noteId": 512}, headers={"content-type": "application/json",
                                                                 "Authorization": "wretewrtwertw"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


