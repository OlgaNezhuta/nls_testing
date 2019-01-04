import requests
import json
from config import *
from helpers.user_helpers import *

COMPLETE_TUTORIAL_URI = '/Account/CompleteTutorial'


def test_01_complete_tutorial_with_authorized_user():
    url = BASE_URL + COMPLETE_TUTORIAL_URI
    token = login(LOGIN_CREDS)
    r = requests.post(url, headers={"content-type": "application/json",
                                          "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_complete_tutorial_with_unauthorized_user():
    url = BASE_URL + COMPLETE_TUTORIAL_URI
    r = requests.post(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


