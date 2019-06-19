from jsonobject import *


class ChangePasswordModel(JsonObject):
    old_password = StringProperty(name="oldPassword")
    password = StringProperty(name="password")
    confirm_password = StringProperty(name="confirmPassword")


class MessageModel(JsonObject):
    message = StringProperty(name="message")


class ChangePasswordSuccess(JsonObject):
    v = StringProperty(name="__v", required=True)
    data = ObjectProperty(MessageModel)


class Errors(JsonObject):
    key = StringProperty(name="key")
    message = StringProperty(name="message")


class ErrorResponse(JsonObject):
    v = StringProperty(name="__v", required=True)
    code = IntegerProperty(name="code")
    message = StringProperty(name="message")
    errors = ListProperty(Errors)
