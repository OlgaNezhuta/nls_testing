valid_creds = [
{
  "firstName": "s",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "qwertyuiopqwertyuiopqwertyuiop",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "String",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "s",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "qwertyuiopqwertyuiopqwertyuiop",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "String",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 13,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 99,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Female",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "string",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 0,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 1,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 999,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Very Unhealthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Unhealthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Average Health",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Very Healthy",
  "sleepingTrouble": True
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": False
}
]

invalid_creds = [
{
  "firstName": "",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "First name is not in valid format"
},
{
  "firstName": "qwertyuiopqwertyuiopqwertyuiopq",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "First name is not in valid format"
},
{
  "firstName": "@#$%",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "First name is not in valid format"
},
{
  "firstName": "123456",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "First name is not in valid format"
},
{
  "firstName": "     ",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "First name is not in valid format"
},
{
  "firstName": "string string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "First name is not in valid format"
},
{
  "firstName": "string-string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "First name is not in valid format"
},
{
  "firstName": "string",
  "lastName": "",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "Last name is not in valid format"
},
{
  "firstName": "string",
  "lastName": "qwertyuiopqwertyuiopqwertyuiopq",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "Last name is not in valid format"
},
{
  "firstName": "string",
  "lastName": "@#$",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "Last name is not in valid format"
},
{
  "firstName": "string",
  "lastName": "123456",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "Last name is not in valid format"
},
{
  "firstName": "string",
  "lastName": "      ",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "Last name is not in valid format"
},
{
  "firstName": "string",
  "lastName": "string string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "Last name is not in valid format"
},
{
  "firstName": "string",
  "lastName": "string-string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "Last name is not in valid format"
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 12,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "Age is not in valid format"
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 100,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "Age is not in valid format"
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 0,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "Age is not in valid format"
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 1000,
  "lifestyle": "Healthy",
  "sleepingTrouble": True,
  "expected_error": "Weight is not in valid format"
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "string",
  "sleepingTrouble": True,
  "expected_error": "Lifestyle is not in valid format"
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "67687",
  "sleepingTrouble": True,
  "expected_error": "Lifestyle is not in valid format"
},
{
  "firstName": "string",
  "lastName": "string",
  "age": 20,
  "gender": "Male",
  "weight": 100,
  "lifestyle": "#$%^&",
  "sleepingTrouble": True,
  "expected_error": "Lifestyle is not in valid format"
}
]
