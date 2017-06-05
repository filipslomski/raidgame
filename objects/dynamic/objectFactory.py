from objects.dynamic.boss import Boss
from objects.dynamic.player import Player


class ObjectFactory():

    objects = [Boss, Player]

    init = None

    def __init__(self, init):
        self.init = init

    def create_object(self, object_type):
        return eval(object_type.title())(self.init)
