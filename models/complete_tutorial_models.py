from jsonobject import *


class ShowTutorialModel(JsonObject):
    show_tutorial = BooleanProperty(name="showTutorial")


class CompleteTutorialModel(JsonObject):
    v = StringProperty(name="__v", required=True)
    data = ObjectProperty(ShowTutorialModel)

