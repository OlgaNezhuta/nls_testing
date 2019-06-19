from jsonobject import *


class UserLoginModel(JsonObject):
    email = StringProperty(required=True)
    password = StringProperty(required=True)


class UserAdditionalInfo(JsonObject):
    first_name = StringProperty(name="firstName")
    last_name = StringProperty(name="lastName")
    age = IntegerProperty(name="age")
    gender = StringProperty(name="gender")
    weight = IntegerProperty(name="weight")
    lifestyle = StringProperty(name="lifestyle")
    sleeping_trouble = BooleanProperty(name="sleepingTrouble")


class UserData(JsonObject):
    id = IntegerProperty(required=True)
    email = StringProperty(name="email")
    show_tutorial = BooleanProperty(name="showTutorial")
    is_basic_timetable_selected = BooleanProperty(name="isBasicTimetableSelected")
    current_timetable_id = IntegerProperty(name="currentTimetableId")
    additional_info = ObjectProperty(UserAdditionalInfo)


class UserToken(JsonObject):
    access_token = StringProperty(name="accessToken")
    refresh_token = StringProperty(name="refreshToken")
    expire_date = StringProperty(name="expireDate")
    type = StringProperty(name="type")


class UserModelResponse(JsonObject):
    v = StringProperty(name="__v", required=True)
    data = ObjectProperty(UserData)
    token = ObjectProperty(UserToken)


class Errors(JsonObject):
    key = StringProperty(name="key")
    message = StringProperty(name="message")


class ErrorResponse(JsonObject):
    v = StringProperty(name="__v", required=True)
    code = IntegerProperty(name="code")
    message = StringProperty(name="message")
    errors = ListProperty(Errors)



