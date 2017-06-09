from objects.dynamic.boss_classes.boss_skills.skill import Skill
from bullets_state import BulletsState
from objects.dynamic.boss import Boss
from objects.dynamic.player import Player

class Bolt(Skill):

    image_path = "images/bullets/bolt.jpg"
    skill_base_damage = 6
    speed = 40

    def shoot(self, creature_level):
        return {
            'speed': self.speed,
            'damage': self.skill_base_damage * creature_level,
            'initiator': Boss,
            'target': Player
        }