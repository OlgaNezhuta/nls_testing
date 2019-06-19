from helpers.user_helpers import *
from tests.test_suit_10_save_note.save_note_test_data import *
import pytest
from models.create_notes_models import *

SAVE_NOTE_URI = '/Note/Save'


@pytest.fixture(scope="function", params=invalid_creds)
def invalid_credentials(request):
    return request.param


@pytest.fixture(scope="function", params=valid_creds)
def valid_credentials(request):
    return request.param


@pytest.fixture(scope="function", params=invalid_creds_for_updating)
def invalid_credentials_for_updating(request):
    return request.param


@pytest.fixture(scope="function", params=valid_creds_for_updating)
def valid_credentials_for_updating(request):
    return request.param


def test_01_save_note_with_correct_creds(valid_credentials):
    url = BASE_URL + SAVE_NOTE_URI
    token = login(LOGIN_CREDS)
    r = requests.post(url, data=json.dumps({"text": valid_credentials["text"]}), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE
    assert CreateNoteModelResponse(r.json()).data.text == valid_credentials["text"]


def test_02_save_note_with_incorrect_creds(invalid_credentials):
    url = BASE_URL + SAVE_NOTE_URI
    token = login(LOGIN_CREDS)
    r = requests.post(url, data=json.dumps({"text": invalid_credentials["text"]}), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == BAD_REQUEST_STATUS_CODE
    assert ErrorResponse(r.json()).errors[0].message == invalid_credentials["expected_error"]


def test_03_update_note_with_correct_creds(valid_credentials_for_updating):
    url = BASE_URL + SAVE_NOTE_URI
    token = login(LOGIN_CREDS)
    r = requests.post(url, data=json.dumps({"id": valid_credentials_for_updating["id"], "text": valid_credentials_for_updating["text"]}), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE
    assert CreateNoteModelResponse(r.json()).data.text == valid_credentials_for_updating["text"]


def test_04_update_note_with_incorrect_creds(invalid_credentials_for_updating):
    url = BASE_URL + SAVE_NOTE_URI
    token = login(LOGIN_CREDS)
    r = requests.post(url, data=json.dumps({"id": invalid_credentials_for_updating["id"], "text": invalid_credentials_for_updating["text"]}), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == BAD_REQUEST_STATUS_CODE
    assert ErrorResponse(r.json()).errors[0].message == invalid_credentials_for_updating["expected_error"]


def test_05_save_note_with_unauthorized_user():
    url = BASE_URL + SAVE_NOTE_URI
    r = requests.post(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE



