from objects.car import Car
from objects.obstacle import Obstacle


class ObjectFactory():

    objects = [Car, Obstacle]

    init = None

    def __init__(self, init):
        self.init = init

    def create_object(self, objectType):
        return eval(objectType.title())(self.init)
