from objects.dynamic.boss_classes.boss_skills.skill import Skill


class Frostbolt(Skill):

    image_path = "images/bullets/frostbolt.jpg"
    speed = 30
    skill_base_damage = 5

    def shoot(self, creature_level):
        from objects.dynamic.player import Player
        return {
            'speed': self.speed,
            'damage': self.skill_base_damage * creature_level,
            'target': Player,
            'bullet_type': type(self)
        }