from utilities.text import Text
from utilities.position import Position


class Score:
    points = 0
    init = None
    text = None
    objects = []

    def __init__(self, init, points=0):
        self.points = points
        self.init = init
        self.text = Text(init)

    def register_object(self, object):
        if not object in self.objects:
            self.objects.append(object)
        return self

    def unregister_object(self, object):
        if object in self.objects:
            self.objects.remove(object)
        return self

    def increase_points(self):
        for object in self.objects:
            self.points += object.update_score()

    def display(self):
        self.text.message_display("Points: " + str(self.points), Position(105, 35), 40)