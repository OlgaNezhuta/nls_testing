from jsonobject import *


class CreateNoteModel(JsonObject):
    id = IntegerProperty(name="id", required=False)
    text = StringProperty(name="text")
    timetable_id = IntegerProperty(name="timetableId", required=False)
    activity_id = IntegerProperty(name="activityId", required=False)


class CreateNote(JsonObject):
    id = IntegerProperty(name="id", required=True)
    text = StringProperty(name="text")
    timetable_id = IntegerProperty(name="timetableId", required=False)
    activity_id = IntegerProperty(name="activityId", required=False)


class CreateNoteModelResponse(JsonObject):
    v = StringProperty(name="__v", required=True)
    data = ObjectProperty(CreateNote)


class Errors(JsonObject):
    key = StringProperty(name="key")
    message = StringProperty(name="message")


class ErrorResponse(JsonObject):
    v = StringProperty(name="__v", required=True)
    code = IntegerProperty(name="code")
    message = StringProperty(name="message")
    errors = ListProperty(Errors)



