from helpers.user_helpers import *

REFRESH_TOKEN_URI = '/Account/RefreshToken'


def test_01_refresh_token_with_correct_creds():
    url = BASE_URL + REFRESH_TOKEN_URI
    refresh = refresh_token(LOGIN_CREDS)
    print(refresh)
    r = requests.post(url, data=json.dumps({"refreshToken": refresh}), headers=BASE_HEADERS)
    print(r.status_code)
    assert r.status_code == SUCCESS_STATUS_CODE


def test_02_refresh_token_with_incorrect_creds():
    url = BASE_URL + REFRESH_TOKEN_URI
    r = requests.post(url, data=json.dumps({"refreshToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1L"
                                           "zA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoib2xnYS5uZXpodXRhLmNyQGdtYWlsLmNvbSIsImlzUmVmcmVzaCI6IlRydW"
                                           "UiLCJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllc"
                                           "iI6IjExOTUiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJV"
                                           "c2VyIiwibmJmIjoxNTQ2NTM0OTk5LCJleHAiOjE1NDkxMjY5OTksImlzcyI6Ik5MU0F1dGhTZXJ2ZXIiLCJhdWQiOiJDbGllbnQifQ"
                                           ".KrCpQPj5ohTtj8Yx9dFwQSb4-C9_gBSsc__MB1zxZU8"}), headers=BASE_HEADERS)
    print(r.status_code)
    assert r.status_code == BAD_REQUEST_STATUS_CODE


