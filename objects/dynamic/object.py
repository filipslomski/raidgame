from abc import abstractmethod
from utilities.position import Position


class Object(object):

    init = None
    position = None # type: Position
    width = None
    height = None

    def __init__(self, init):
        self.init = init

    @abstractmethod
    def spawn(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def collision(self):
        pass

    @abstractmethod
    def death(self):
        pass

    @abstractmethod
    def get_health(self):
        pass