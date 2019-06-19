from jsonobject import *


class UserRegisterModel(JsonObject):
    email = StringProperty(required=True)
    password = StringProperty(required=True)
    repeat_password = StringProperty(required=True, name="repeatPassword")


class UserDataRegister(JsonObject):
    email = StringProperty(required=True)
    email_sent = BooleanProperty(name="emailSent")


class UserRegisterSuccess(JsonObject):
    v = StringProperty(name="__v", required=True)
    data = ObjectProperty(UserDataRegister)


class Errors(JsonObject):
    key = StringProperty(name="key")
    message = StringProperty(name="message")


class ErrorResponse(JsonObject):
    v = StringProperty(name="__v", required=True)
    code = IntegerProperty(name="code")
    message = StringProperty(name="message")
    errors = ListProperty(Errors)


