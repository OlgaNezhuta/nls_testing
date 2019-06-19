from jsonobject import *


class ResetPasswordModel(JsonObject):
    email = StringProperty(required=True)


class MessageModel(JsonObject):
    message = StringProperty(name="message")


class ResetPasswordSuccess(JsonObject):
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

