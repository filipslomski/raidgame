from utilities.text import Text
from utilities.position import Position


class Score:
    points = 0
    init = None
    text = None
    objects = []

    def __init__(self, init, points=0, *args):
        self.points = points
        self.init = init
        self.text = Text(init)
        for arg in args:
            self.objects.append(arg)

    def increase_points(self):
        for object in self.objects:
            self.points += object.update_score()

    def display(self):
        self.text.message_display("Points: " + str(self.points), Position(0, 0))