from objects.dynamic.boss_classes.boss_being import BossBeing
import random


class FrostBoss(BossBeing):
    image_path = "images/units/bosses/frost_boss.png"
    width = 150
    height = 111
    speed = 4
    health = 400
    experience = 200
    level = 4
    firepower = 12

    def move(self, position):
        self.behavior.move(position, self.speed)

    def shoot(self):
        if random.randint(0, 100) < self.firepower:
            return self.boss_skills[random.randint(0, len(self.boss_skills) - 1)]().shoot(self.level)
        else:
            return False