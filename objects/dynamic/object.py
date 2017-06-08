from abc import abstractmethod
from utilities.position import Position


class Object(object):

    position = None # type: Position
    width = None
    height = None
    speed = None

    @abstractmethod
    def spawn(self, position):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def collision(self, object):
        pass

    @abstractmethod
    def death(self):
        pass

    @abstractmethod
    def get_health(self):
        pass