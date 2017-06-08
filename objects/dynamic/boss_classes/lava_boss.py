from objects.dynamic.boss_classes.boss import Boss
import random


class LavaBoss(Boss):
    image_path = "images/units/bosses/lava_boss.jpg"
    width = 50
    height = 50
    speed = 15
    health = 100
    experience = 100
    level = 1
    firepower = 2

    def move(self, position):
        self.boss_behaviors[random.randint(0, len(self.boss_behaviors) - 1)].move(position, self.speed)

    def shoot(self, position):
        pass