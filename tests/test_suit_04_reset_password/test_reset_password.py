from tests.test_suit_04_reset_password.reset_password_test_data import *
from helpers.user_helpers import *

RESET_PASSWORD_URI = '/Account/ResetPassword'


def test_01_reset_password_with_correct_email():
    url = BASE_URL + RESET_PASSWORD_URI
    r = requests.post(url, data=json.dumps(correct_email), headers=BASE_HEADERS)
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_reset_password_with_incorrect_email():
    url = BASE_URL + RESET_PASSWORD_URI
    for el in incorrect_emails:
        r = requests.post(url, data=json.dumps(el), headers=BASE_HEADERS)
        print(r.status_code)
        assert r.status_code == BAD_REQUEST_STATUS_CODE


def test_03_reset_password_with_not_confirmed_email():
    url = BASE_URL + RESET_PASSWORD_URI
    r = requests.post(url, data=json.dumps(email_is_not_confirmed), headers=BASE_HEADERS)
    print(r.status_code)
    assert r.status_code == BAD_REQUEST_STATUS_CODE
