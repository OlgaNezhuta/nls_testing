from helpers.user_helpers import *
from tests.test_suit_05_change_password.change_password_test_data import *
from models.change_password_models import *
import pytest


CHANGE_PASSWORD_URI = '/Account/ChangePassword'


@pytest.fixture(scope="function", params=invalid_creds)
def invalid_credentials(request):
    return request.param


# @pytest.fixture(scope="function", params=valid_creds)
# def valid_credentials(request):
#     return request.param
#
#
# def test_01_change_password_with_correct_creds(valid_credentials):
#     url = BASE_URL + CHANGE_PASSWORD_URI
#     token = login(LOGIN_CREDS)
#     r = requests.post(url, data=json.dumps({"oldPassword": valid_credentials["oldPassword"], "password": valid_credentials["password"],
#                                             "confirmPassword": valid_credentials["confirmPassword"]}), headers={"content-type": "application/json",
#                                                                  "Authorization": token})
#     print(r.status_code)
#     assert r.status_code == SUCCESS_STATUS_CODE
#     assert ChangePasswordSuccess(r.json()).data.message == valid_credentials["message"]


def test_02_change_password_with_incorrect_creds(invalid_credentials):
    url = BASE_URL + CHANGE_PASSWORD_URI
    token = login(LOGIN_CREDS)
    r = requests.post(url, data=json.dumps({"oldPassword": invalid_credentials["oldPassword"], "password": invalid_credentials["password"],
                                            "confirmPassword": invalid_credentials["confirmPassword"]}), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert ErrorResponse(r.json()).code == invalid_credentials["status_code"]
    assert ErrorResponse(r.json()).errors[0].message == invalid_credentials["expected_error"]


def test_03_change_password_with_unauthorized_user():
    url = BASE_URL + CHANGE_PASSWORD_URI
    r = requests.post(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE


