from jsonobject import *


class SaveAdditionalInfoModel(JsonObject):
    first_name = StringProperty(name="firstName")
    last_name = StringProperty(name="lastName")
    age = IntegerProperty(name="age")
    gender = StringProperty(name="gender")
    weight = IntegerProperty(name="weight")
    lifestyle = StringProperty(name="lifestyle")
    sleeping_trouble = BooleanProperty(name="sleepingTrouble")


class SaveAdditionalInfoResponse(JsonObject):
    v = StringProperty(name="__v", required=True)
    data = ObjectProperty(SaveAdditionalInfoModel)


class Errors(JsonObject):
    key = StringProperty(name="key")
    message = StringProperty(name="message")


class ErrorResponse(JsonObject):
    v = StringProperty(name="__v", required=True)
    code = IntegerProperty(name="code")
    message = StringProperty(name="message")
    errors = ListProperty(Errors)

