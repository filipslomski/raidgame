from objects.dynamic.boss_classes.boss_skills.skill import Skill


class Firebolt(Skill):

    image_path = "images/bullets/firebolt.jpg"
    speed = 45
    skill_base_damage = 4

    def shoot(self, creature_level):
        from objects.dynamic.boss import Boss
        from objects.dynamic.player import Player
        return {
            'speed': self.speed,
            'damage': self.skill_base_damage * creature_level,
            'initiator': Boss,
            'target': Player,
            'bullet_type': self
        }