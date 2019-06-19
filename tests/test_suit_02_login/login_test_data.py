valid_creds = [
{
  "email": "OlgaOlga@example.com",
  "password": "string"
},
{
  "email": "olga123@example.com",
  "password": "string"
},
{
  "email": "olga#olga@example.com",
  "password": "string"
},
{
  "email": "olga.olga@example.com",
  "password": "string"
},
{
  "email": "olga.olga.olga@example.com",
  "password": "string"
},
{
  "email": "olgaolga@example",
  "password": "string"
},
{
  "email": "olga7@example.com",
  "password": "qwertyuiopqwerty"
},
{
  "email": "olga3@example.com",
  "password": "STRING"
},
{
  "email": "olga4@example.com",
  "password": "String"
},
{
  "email": "olga5@example.com",
  "password": "string123"
},
{
  "email": "olga6@example.com",
  "password": "string#"
}
]


invalid_creds = [
{
  "email": "olgaexample.com",
  "password": "string",
  "expected_error": "Email address is not in valid format",
  "status_code": 400
},
{
  "email": "",
  "password": "string",
  "expected_error": "Email address is not in valid format",
  "status_code": 400
},
{
  "email": "         ",
  "password": "string",
  "expected_error": "Email address is not in valid format",
  "status_code": 400
},
{
  "email": "olga olga@example.com",
  "password": "string",
  "expected_error": "Email address is not in valid format",
  "status_code": 400
},
{
  "email": "olga@example.com",
  "password": "strin",
  "expected_error": "Password doesn’t meet length validation criteria",
  "status_code": 400
},
{
  "email": "olga@example.com",
  "password": "qwertyuiopqwertyu",
  "expected_error": "Password doesn’t meet length validation criteria",
  "status_code": 400
},
{
  "email": "olga@example.com",
  "password": "      ",
  "expected_error": "Password field is empty",
  "status_code": 400
},
{
  "email": "olga@example.com",
  "password": "string string",
  "expected_error": "Incorrect email or password",
  "status_code": 400
},
{
  "email": "olga@example.com",
  "password": "",
  "expected_error": "Password doesn’t meet length validation criteria",
  "status_code": 400
},
{
  "email": "olgaemailisnotconfirmed@example.com",
  "password": "string",
  "expected_error": "Email is not confirmed",
  "status_code": 405
}
]


