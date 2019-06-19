from tests.test_suit_04_reset_password.reset_password_test_data import *
from helpers.user_helpers import *
from models.reset_password_models import *
import pytest

RESET_PASSWORD_URI = '/Account/ResetPassword'


@pytest.fixture(scope="function", params=invalid_creds)
def invalid_credentials(request):
    return request.param


def test_01_reset_password_with_correct_email():
    url = BASE_URL + RESET_PASSWORD_URI
    r = requests.post(url, data=json.dumps(valid_creds), headers=BASE_HEADERS)
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE
    assert ResetPasswordSuccess(r.json()).data.message == valid_creds["message"]


def test_02_reset_password_with_incorrect_email(invalid_credentials):
    url = BASE_URL + RESET_PASSWORD_URI
    r = requests.post(url, data=json.dumps({"email": invalid_credentials["email"]}), headers=BASE_HEADERS)
    print(r.status_code)
    assert ErrorResponse(r.json()).code == invalid_credentials["status_code"]
    assert ErrorResponse(r.json()).errors[0].message == invalid_credentials["expected_error"]



