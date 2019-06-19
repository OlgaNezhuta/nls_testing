from jsonobject import *


class NoteModel(JsonObject):
    id = IntegerProperty(name="id")
    text = StringProperty(name="text")
    create_date = StringProperty(name="createDate")
    timetable_id = IntegerProperty(name="timetableId")
    activity_id = IntegerProperty(name="activityId")


class NoteDeleteModel(JsonObject):
    v = StringProperty(name="__v", required=True)
    data = ObjectProperty(NoteModel)


class Errors(JsonObject):
    key = StringProperty(name="key")
    message = StringProperty(name="message")


class ErrorResponse(JsonObject):
    v = StringProperty(name="__v", required=True)
    code = IntegerProperty(name="code")
    message = StringProperty(name="message")
    errors = ListProperty(Errors)


