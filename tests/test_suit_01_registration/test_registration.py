import requests
import json
from config import *
from tests.test_suit_01_registration.registration_test_data import *
from models.registration_models import *
import pytest


REGISTRATION_URI = '/Account/Register'


@pytest.fixture(scope="function", params=invalid_creds)
def invalid_credentials(request):
    return request.param


@pytest.fixture(scope="function", params=valid_creds)
def valid_credentials(request):
    return request.param


def test_01_register_with_correct_creds(valid_credentials):
    url = BASE_URL + REGISTRATION_URI
    r = requests.post(url, data=json.dumps({"email": valid_credentials["email"], "password": valid_credentials["password"], "repeatPassword": valid_credentials["repeatPassword"]}), headers=BASE_HEADERS)
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE
    assert UserRegisterSuccess(r.json()).data.email == valid_credentials["email"]


def test_02_register_with_incorrect_creds(invalid_credentials):
    url = BASE_URL + REGISTRATION_URI
    r = requests.post(url, data=json.dumps({"email": invalid_credentials["email"], "password": invalid_credentials["password"], "repeatPassword": invalid_credentials["repeatPassword"]}), headers=BASE_HEADERS)
    print(r.status_code)
    assert ErrorResponse(r.json()).code == invalid_credentials["status_code"]
    assert ErrorResponse(r.json()).errors[0].message == invalid_credentials["expected_error"]















