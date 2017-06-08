from objects.dynamic.boss_classes.boss_skills.skill import Skill


class Bolt(Skill):

    image_path = "images/bullets/bolt.jpg"
    skill_base_damage = 6
    speed = 40

    def shoot(self, position):
        pass