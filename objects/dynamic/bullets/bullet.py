from abc import abstractmethod


class Bullet(object):
    speed = None
    image_path = None
    start_position = None
    target_position = None
    current_position = None
    damage = None
    image = None

    def __init__(self, speed, start_position, target_position, damage):
        self.speed = speed
        self.start_position = start_position
        self.position = start_position
        self.target_position = target_position
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