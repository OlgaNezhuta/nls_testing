from helpers.user_helpers import *
from tests.test_suit_07_save_additional_info.save_additional_info_test_data import *
import pytest
from models.save_additional_info_models import *


SAVE_ADDITIONAL_INFO_URI = '/Account/SaveAddititionalInfo'


@pytest.fixture(scope="function", params=invalid_creds)
def invalid_credentials(request):
    return request.param


@pytest.fixture(scope="function", params=valid_creds)
def valid_credentials(request):
    return request.param


# def test_01_save_additional_info_with_correct_creds(valid_credentials):
#     url = BASE_URL + SAVE_ADDITIONAL_INFO_URI
#     token = login(LOGIN_CREDS)
#     r = requests.post(url, data=json.dumps({"firstName": valid_credentials["firstName"], "lastName": valid_credentials["lastName"],
#                                             "age": valid_credentials["age"], "gender": valid_credentials["gender"],
#                                             "weight": valid_credentials["weight"], "lifestyle": valid_credentials["lifestyle"],
#                                             "sleepingTrouble": valid_credentials["sleepingTrouble"]}),
#                       headers={"content-type": "application/json","Authorization": token})
#     print(r.status_code)
#     assert r.status_code == SUCCESS_STATUS_CODE
#     assert SaveAdditionalInfoResponse(r.json()).data.first_name == valid_credentials["firstName"]
#     assert SaveAdditionalInfoResponse(r.json()).data.last_name == valid_credentials["lastName"]
#     assert SaveAdditionalInfoResponse(r.json()).data.age == valid_credentials["age"]
#     assert SaveAdditionalInfoResponse(r.json()).data.gender == valid_credentials["gender"]
#     assert SaveAdditionalInfoResponse(r.json()).data.weight == valid_credentials["weight"]
#     assert SaveAdditionalInfoResponse(r.json()).data.lifestyle == valid_credentials["lifestyle"]
#     assert SaveAdditionalInfoResponse(r.json()).data.sleeping_trouble == valid_credentials["sleepingTrouble"]


def test_02_save_additional_info_with_incorrect_creds(invalid_credentials):
    url = BASE_URL + SAVE_ADDITIONAL_INFO_URI
    token = login(LOGIN_CREDS)
    r = requests.post(url, data=json.dumps({"firstName": invalid_credentials["firstName"], "lastName": invalid_credentials["lastName"],
                                            "age": invalid_credentials["age"], "gender": invalid_credentials["gender"],
                                            "weight": invalid_credentials["weight"], "lifestyle": invalid_credentials["lifestyle"],
                                            "sleepingTrouble": invalid_credentials["sleepingTrouble"]}), headers={"content-type": "application/json",
                                                                 "Authorization": token})
    print(r.status_code)
    assert r.status_code == BAD_REQUEST_STATUS_CODE
    assert ErrorResponse(r.json()).errors[0].message == invalid_credentials["expected_error"]


def test_03_save_additional_info_with_unauthorized_user():
    url = BASE_URL + SAVE_ADDITIONAL_INFO_URI
    r = requests.post(url, headers={"content-type": "application/json",
                                          "Authorization": "qwertyuiop"})
    print(r.status_code)
    assert r.status_code == UNAUTHORIZED_STATUS_CODE

