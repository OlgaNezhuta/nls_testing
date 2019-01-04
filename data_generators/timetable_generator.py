import requests
import json
import random
import string
import copy
from data_generators.timetable_test_data import my_json
from config import *
from helpers import *


TIMETABLE_URI = '/Timetable/Run'


def run_timetable(token):
    url = BASE_URL + TIMETABLE_URI
    headers = BASE_HEADERS
    headers.update({'Authorization': token})
    r = requests.post(url, data=json.dumps(my_json), headers=headers)
    print(r.status_code)
    assert r.status_code == 200
    return r.json()


token = login(LOGIN_CREDS)
run = run_timetable(token)
print(run)



