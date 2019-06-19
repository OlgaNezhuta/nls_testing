import pytest
from tests.test_suit_02_login.login_test_data import *
from helpers.user_helpers import *
from models.login_models import *

LOGIN_URI = '/Account/Login'


@pytest.fixture(scope="function", params=invalid_creds)
def invalid_credentials(request):
    return request.param


@pytest.fixture(scope="function", params=valid_creds)
def valid_credentials(request):
    return request.param


def test_01_login_with_correct_creds(valid_credentials):
    url = BASE_URL + LOGIN_URI
    r = requests.post(url, data=json.dumps({"email": valid_credentials["email"], "password": valid_credentials["password"]}), headers=BASE_HEADERS)
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE
    assert UserModelResponse(r.json()).data.email == valid_credentials["email"]


def test_02_login_with_incorrect_creds(invalid_credentials):
    url = BASE_URL + LOGIN_URI
    r = requests.post(url, data=json.dumps({"email": invalid_credentials["email"], "password": invalid_credentials["password"]}), headers=BASE_HEADERS)
    print(r.status_code)
    assert ErrorResponse(r.json()).code == invalid_credentials["status_code"]
    assert ErrorResponse(r.json()).errors[0].message == invalid_credentials["expected_error"]
