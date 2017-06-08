from objects.dynamic.boss_classes.boss_behavior.behavior import Behavior
import random
from init import Init


class TeleportingBehavior(Behavior):

    def move(self, position, speed):
        if random.randint(1, 100) < speed:
            position.x = random.randint(10, Init.display_width - 100)
            position.y = random.randint(10, Init.display_height - 100)