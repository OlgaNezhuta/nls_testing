import requests
import json
import random
import string
from config import *


LOGIN_URI = '/Account/Login'
LOGIN_CREDS = {"email": "olga.nezhuta.cr@gmail.com",
               "password": "qwerty"}
LOGOUT_URI = '/account/logout'
SAVE_NOTE_URI = '/Note/Save'

def login(creds):
    url = BASE_URL + LOGIN_URI
    r = requests.post(url, data=json.dumps(creds), headers=BASE_HEADERS)
    assert r.status_code == SUCCESS_STATUS_CODE
    my_token = r.json()['data']['token']['accessToken']
    return 'Bearer {}'.format(my_token)


def refresh_token(creds):
    url = BASE_URL + LOGIN_URI
    r = requests.post(url, data=json.dumps(creds), headers=BASE_HEADERS)
    assert r.status_code == SUCCESS_STATUS_CODE
    my_refresh_token = r.json()['data']['token']['refreshToken']
    return my_refresh_token


def create_some_note():
    url = BASE_URL + SAVE_NOTE_URI
    token = login(LOGIN_CREDS)
    r = requests.post(url, data=json.dumps({"text": "string333"}), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE
    my_note_id = r.json()['data']['id']
    print(my_note_id)
    return my_note_id


def logout(token):
    url = BASE_URL + LOGOUT_URI
    headers = BASE_HEADERS
    headers.update({'Authorization': token})
    print(headers)
    r = requests.delete(url, headers=headers)
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


