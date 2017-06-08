from abc import abstractmethod


class Behavior(object):

    @abstractmethod
    def move(self, position, speed):
        pass