from objects.dynamic.boss_classes.boss_being import BossBeing
import random


class LavaBoss(BossBeing):
    image_path = "images/units/bosses/lava_boss.jpg"
    width = 197
    height = 200
    speed = 15
    health = 100
    experience = 100
    level = 1
    firepower = 2

    def move(self, position):
        self.behavior.move(position, self.speed)

    def shoot(self, position):
        if random.randint(0, 100) < self.firepower:
            self.boss_skills[random.randint(0, len(self.boss_skills) - 1)].shoot(position, self.level)