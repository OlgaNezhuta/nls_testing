valid_creds = [
{
  "oldPassword": "qwerty",
  "password": "string",
  "confirmPassword": "string",
  "message": "Password has been changed"
},
{
  "oldPassword": "string",
  "password": "qwertyuiopqwerty",
  "confirmPassword": "qwertyuiopqwerty",
  "message": "Password has been changed"
},
{
  "oldPassword": "qwertyuiopqwerty",
  "password": "QWERTY",
  "confirmPassword": "QWERTY",
  "message": "Password has been changed"
},
{
  "oldPassword": "QWERTY",
  "password": "Qwerty",
  "confirmPassword": "Qwerty",
  "message": "Password has been changed"
},
{
  "oldPassword": "Qwerty",
  "password": "qwerty@",
  "confirmPassword": "qwerty@",
  "message": "Password has been changed"
},
{
  "oldPassword": "qwerty@",
  "password": "qwerty123",
  "confirmPassword": "qwerty123",
  "message": "Password has been changed"
},
{
  "oldPassword": "qwerty123",
  "password": "qwerty",
  "confirmPassword": "qwerty",
  "message": "Password has been changed"
}
]

invalid_creds = [
{
  "oldPassword": "qwerty",
  "password": "qwert",
  "confirmPassword": "qwert",
  "expected_error": "Password doesn’t meet length validation criteria",
  "status_code": 400
},
{
  "oldPassword": "qwerty",
  "password": "qwertyuiopqwertyu",
  "confirmPassword": "qwertyuiopqwertyu",
  "expected_error": "Password doesn’t meet length validation criteria",
  "status_code": 400

},
{
  "oldPassword": "qwerty",
  "password": "      ",
  "confirmPassword": "      ",
  "expected_error": "Password field is empty",
  "status_code": 400

},
{
  "oldPassword": "qwerty",
  "password": "string string",
  "confirmPassword": "string string",
  "expected_error": "Password should not contain spaces",
  "status_code": 400
},
{
  "oldPassword": "qwerty",
  "password": "",
  "confirmPassword": "",
  "expected_error": "Password field is empty",
  "status_code": 400

},
{
  "oldPassword": "qwerty",
  "password": "string",
  "confirmPassword": "stringhjhkjhkjhkh",
  "expected_error": "Passwords don’t match",
  "status_code": 400
},
{
  "oldPassword": "qwertyertetet",
  "password": "string",
  "confirmPassword": "string",
  "expected_error": "Current password doesn’t match password",
  "status_code": 400

},
{
  "oldPassword": "",
  "password": "string",
  "confirmPassword": "string",
  "expected_error": " Old password field is empty",
  "status_code": 400
},
{
  "oldPassword": "qwerty",
  "password": "",
  "confirmPassword": "string",
  "expected_error": "Password field is empty",
  "status_code": 400

},
{
  "oldPassword": "qwerty",
  "password": "string",
  "confirmPassword": "",
  "expected_error": "Confirm password field is empty",
  "status_code": 400
}
]


