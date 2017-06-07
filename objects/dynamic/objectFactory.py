from objects.dynamic.boss import Boss
from objects.dynamic.player import Player


class ObjectFactory():

    objects = [Boss, Player]

    @staticmethod
    def create_object(object_type):
        return eval(object_type.title())()
