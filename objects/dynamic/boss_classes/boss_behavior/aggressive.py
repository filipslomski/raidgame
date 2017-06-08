from objects.dynamic.boss_classes.boss_behavior.behavior import Behavior
from init import Init
import random


class AggressiveBehavior(Behavior):

    move_range_x_max = Init.display_width - 100
    move_range_x_min = 10
    move_range_y_max = Init.display_height - 100
    move_range_y_min = 10

    def move(self, position, speed):
        while True:
            next_step = random.randint(-speed, speed)
            if random.randint(0, 1) == 0:
                if position.x + next_step in range(self.move_range_x_min, self.move_range_x_max):
                    position.x += next_step
                    break
            else:
                if position.y + next_step in range(self.move_range_y_min, self.move_range_y_max):
                    position.y += next_step
                    break