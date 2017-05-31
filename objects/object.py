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