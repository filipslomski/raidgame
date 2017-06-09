from objects.dynamic.boss_classes.boss_skills.firebolt import Firebolt
from objects.dynamic.boss_classes.boss_skills.frostbolt import Frostbolt
from objects.dynamic.boss_classes.boss_skills.bolt import Bolt
from objects.dynamic.bullets.boltBullet import BoltBullet
from objects.dynamic.bullets.fireboltBullet import FireboltBullet
from objects.dynamic.bullets.frostboltBullet import FrostboltBullet


class BulletTracker(object):

    skill_to_bullet = {
        Firebolt: FireboltBullet,
        Frostbolt: FrostboltBullet,
        Bolt: BoltBullet
    }
    targets = []

    def register_target(self, object):
        if not object in self.targets:
            self.targets.append(object)
        return self

    def unregister_object(self, object):
        if object in self.targets:
            self.targets.remove(object)
        return self

    def manage_bullets(self):
        for object in self.targets:
            data = object.shoot()
            if data != False:
                self.skill_to_bullet[data['bullet_type']](data['speed'], data['initiator'], data['target'], data['damage'])