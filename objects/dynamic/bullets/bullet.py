from abc import abstractmethod


class Bullet(object):
    speed = None
    image_path = None
    start_positon = None
    target_position = None
    position = None
    damage = None
    image = None

    def __init__(self, speed, initiator, target, damage):
        self.speed = speed
        self.start_position = initiator.position
        self.position = initiator.position
        self.target_position = target.position
        self.damage = damage

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def destroy(self):
        pass