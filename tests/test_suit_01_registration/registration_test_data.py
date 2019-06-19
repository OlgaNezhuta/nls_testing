valid_creds = [
{
  "email": "OlgaOlga@example.com",
  "password": "string",
  "repeatPassword": "string"
},
{
  "email": "olga123@example.com",
  "password": "string",
  "repeatPassword": "string"
},
{
  "email": "olga#olga@example.com",
  "password": "string",
  "repeatPassword": "string"
},
{
  "email": "olga.olga@example.com",
  "password": "string",
  "repeatPassword": "string"
},
{
  "email": "olga.olga.olga@example.com",
  "password": "string",
  "repeatPassword": "string"
},
{
  "email": "olgaolga@example",
  "password": "string",
  "repeatPassword": "string"
},
{
  "email": "olga7@example.com",
  "password": "qwertyuiopqwerty",
  "repeatPassword": "qwertyuiopqwerty"
},
{
  "email": "olga3@example.com",
  "password": "STRING",
  "repeatPassword": "STRING"
},
{
  "email": "olga4@example.com",
  "password": "String",
  "repeatPassword": "String"
},
{
  "email": "olga5@example.com",
  "password": "string123",
  "repeatPassword": "string123"
},
{
  "email": "olga6@example.com",
  "password": "string#",
  "repeatPassword": "string#"
}
]


invalid_creds = [
{
  "email": "olgaexample.com",
  "password": "string",
  "repeatPassword": "string",
  "expected_error": "Email address is not in valid format",
  "status_code": 400
},
{
  "email": "",
  "password": "string",
  "repeatPassword": "string",
  "expected_error": "Email address is not in valid format",
  "status_code": 400
},
{
  "email": "         ",
  "password": "string",
  "repeatPassword": "string",
  "expected_error": "Email address is not in valid format",
  "status_code": 400
},
{
  "email": "olga olga@example.com",
  "password": "string",
  "repeatPassword": "string",
  "expected_error": "Email address is not in valid format",
  "status_code": 400
},
{
  "email": "olga@example.com",
  "password": "strin",
  "repeatPassword": "strin",
  "expected_error": "Password doesn’t meet length validation criteria",
  "status_code": 400
},
{
  "email": "olga@example.com",
  "password": "qwertyuiopqwertyu",
  "repeatPassword": "qwertyuiopqwertyu",
  "expected_error": "Password doesn’t meet length validation criteria",
  "status_code": 400
},
{
  "email": "olga@example.com",
  "password": "      ",
  "repeatPassword": "      ",
  "expected_error": "Password should not contain spaces",
  "status_code": 400
},
{
  "email": "olga@example.com",
  "password": "string string",
  "repeatPassword": "string string",
  "expected_error": "Password should not contain spaces",
  "status_code": 400
},
{
  "email": "olga@example.com",
  "password": "",
  "repeatPassword": "string",
  "expected_error": "Password doesn’t meet length validation criteria",
  "status_code": 400
},
{
  "email": "olga@example.com",
  "password": "string",
  "repeatPassword": "",
  "expected_error": "Repeat password doesn’t match password",
  "status_code": 400
},
{
  "email": "olga#olga@example.com",
  "password": "string",
  "repeatPassword": "stringqwertt",
  "expected_error": "Repeat password doesn’t match password",
  "status_code": 400
},
{
  "email": "olga.nezhuta.cr@gmail.com",
  "password": "qwerty",
  "repeatPassword": "qwerty",
  "expected_error": "Email address already registered",
  "status_code": 422
}
]

