from objects.dynamic.boss_classes.boss_skills.skill import Skill


class Frostbolt(Skill):

    image_path = "images/bullets/frostbolt.jpg"
    speed = 30
    skill_base_damage = 5

    def shoot(self, position):
        pass