from abc import abstractmethod


class Skill(object):
    skill_base_damage = None
    speed = None
    image_path = None

    @abstractmethod
    def shoot(self, creature_level):
        pass