from objects.dynamic.boss_classes.boss_skills.skill import Skill
from bullets_state import BulletsState

class Bolt(Skill):

    image_path = "images/bullets/bolt.jpg"
    skill_base_damage = 6
    speed = 40

    def shoot(self, position, creature_level):
        BulletsState.initiator