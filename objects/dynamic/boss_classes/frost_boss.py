from objects.dynamic.boss_classes.boss import Boss
import random


class FrostBoss(Boss):
    image_path = "images/units/bosses/frost_boss.jpg"
    width = 40
    height = 60
    speed = 4
    health = 400
    experience = 200
    level = 4
    firepower = 12

    def move(self, position):
        self.boss_behaviors[random.randint(0, len(self.boss_behaviors) - 1)].move(position, self.speed)

    def shoot(self, position):
        if random.randint(0, 100) < self.firepower:
            self.boss_skills[random.randint(0, len(self.boss_skills) - 1)].shoot(position)