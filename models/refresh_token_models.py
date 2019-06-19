from jsonobject import *


class RefreshTokenModel(JsonObject):
    refresh_token = StringProperty(name="refreshToken")


class RefreshTokenData(JsonObject):
    access_token = StringProperty(name="accessToken")
    refresh_token = StringProperty(name="refreshToken")
    expire_date = StringProperty(name="expireDate")
    type = StringProperty(name="type")


class RefreshTokenSuccess(JsonObject):
    v = StringProperty(name="__v", required=True)
    data = ObjectProperty(RefreshTokenData)


class Errors(JsonObject):
    key = StringProperty(name="key")
    message = StringProperty(name="message")


class ErrorResponse(JsonObject):
    v = StringProperty(name="__v", required=True)
    code = IntegerProperty(name="code")
    message = StringProperty(name="message")
    errors = ListProperty(Errors)
