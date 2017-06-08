from objects.dynamic.boss_classes.boss_behavior.behavior import Behavior
from init import Init
import random


class PassiveBehavior(Behavior):

    move_range_x_max = int(Init.display_width / 3 * 2)
    move_range_x_min = int(Init.display_width / 3)
    move_range_y_max = int(Init.display_height / 2)
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
