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
  "email": "olga2@example.com",
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
  "password": "string"
},
{
  "email": "",
  "password": "string"
},
{
  "email": "         ",
  "password": "string"
},
{
  "email": "olga olga@example.com",
  "password": "string"
},
{
  "email": "olga@example.com",
  "password": "strin"
},
{
  "email": "olga@example.com",
  "password": "qwertyuiopqwertyu"
},
{
  "email": "olga@example.com",
  "password": "      "
},
{
  "email": "olga@example.com",
  "password": "string string"
},
{
  "email": "olga@example.com",
  "password": ""
}
]

email_is_not_confirmed_creds = {
  "email": "olgaemailisnotconfirmed@example.com",
  "password": "string"
}


