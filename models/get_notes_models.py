from jsonobject import *


class NotesPagination(JsonObject):
    next_offset = IntegerProperty(name="next_offset")
    total_count = IntegerProperty(name="total_count")


class NotesData(JsonObject):
    id = IntegerProperty(name="id")
    text = StringProperty(name="text")
    create_date = StringProperty(name="createDate")
    timetable_id = IntegerProperty(name="timetableId")
    activity_id = IntegerProperty(name="activityId")


class GetNotesMOdel(JsonObject):
    pagination = ObjectProperty(NotesPagination)
    v = StringProperty(name="__v", required=True)
    data = ListProperty(NotesData)


class Errors(JsonObject):
    key = StringProperty(name="key")
    message = StringProperty(name="message")


class ErrorResponse(JsonObject):
    v = StringProperty(name="__v", required=True)
    code = IntegerProperty(name="code")
    message = StringProperty(name="message")
    errors = ListProperty(Errors)


