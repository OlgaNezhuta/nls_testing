valid_creds = {
    "email": "olga.nezhuta.cr@gmail.com",
    "message": "Reset password link has been sent on your email"
}


invalid_creds = [
{
  "email": "olgaexample.com",
  "expected_error": "Email address is not in valid format",
  "status_code": 400
},
{
  "email": "",
  "expected_error": "Email address field is empty",
  "status_code": 400
},
{
  "email": "         ",
  "expected_error": "Email address field is empty",
  "status_code": 400
},
{
  "email": "olga olga@example.com",
  "expected_error": "Email address is not in valid format",
  "status_code": 400
},
{
  "email": "olga@example",
  "expected_error": "Email doesn’t exist",
  "status_code": 400
},
{
  "email": "olgaemailisnotconfirmed@example.com",
  "expected_error": "Email is not confirmed",
  "status_code": 400
}
]


