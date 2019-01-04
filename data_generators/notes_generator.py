import requests
import json
import random
import string
from config import *
from helpers import *


NOTE_URI = '/Note/Save'
MAX_ALLOWED_TEXT_LEN = 500


def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return "".join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


def notes(token, text):
    url = BASE_URL + NOTE_URI
    payload = {"text": text}
    headers = BASE_HEADERS
    headers.update({'Authorization': token})
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    assert r.status_code == 200
    return r.json()


token = login(LOGIN_CREDS)
rand_text = random_string(MAX_ALLOWED_TEXT_LEN)
note_response = notes(token, rand_text)
text_from_resp = note_response['data']['text']
assert text_from_resp == rand_text
logout = logout(token)



