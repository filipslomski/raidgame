from objects.dynamic.boss_classes.boss_skills.skill import Skill


class Firebolt(Skill):

    image_path = "images/bullets/firebolt.jpg"
    speed = 45
    skill_base_damage = 4

    def shoot(self, position):
        pass