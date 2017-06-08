from abc import abstractmethod
from objects.dynamic.boss_classes.boss_behavior.aggressive import AggressiveBehavior
from objects.dynamic.boss_classes.boss_behavior.teleporting import TeleportingBehavior
from objects.dynamic.boss_classes.boss_behavior.passive import PassiveBehavior
from objects.dynamic.boss_classes.boss_skills.bolt import Bolt
from objects.dynamic.boss_classes.boss_skills.firebolt import Firebolt
from objects.dynamic.boss_classes.boss_skills.frostbolt import Frostbolt
import random


class Boss(object):
    image_path = None
    width = None
    height = None
    speed = None
    health = None
    experience = None
    level = None
    behavior = None
    firepower = None
    boss_behaviors = [AggressiveBehavior, TeleportingBehavior, PassiveBehavior]
    boss_skills = [Bolt, Firebolt, Frostbolt]

    def select_boss_behavior(self, behavior=None):
        if behavior is None:
            self.behavior = self.boss_behaviors[random.randint(0, len(self.boss_behaviors) - 1)]
        else:
            self.behavior = behavior

    @abstractmethod
    def move(self, position):
        pass

    @abstractmethod
    def shoot(self, position):
        pass
