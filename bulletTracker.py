from objects.dynamic.boss_classes.boss_skills.firebolt import Firebolt
from objects.dynamic.boss_classes.boss_skills.frostbolt import Frostbolt
from objects.dynamic.boss_classes.boss_skills.bolt import Bolt
from objects.dynamic.bullets.boltBullet import BoltBullet
from objects.dynamic.bullets.fireboltBullet import FireboltBullet
from objects.dynamic.bullets.frostboltBullet import FrostboltBullet


class BulletTracker(object):

    bullets = []
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
        for initiator in self.targets:
            data = initiator.shoot()
            if data != False:
                for object in self.targets:
                    if type(object) == data['target']:
                        bullet = self.skill_to_bullet[data['bullet_type']](data['speed'], initiator, object, data['damage'])
                        self.bullets.append(bullet)
        for bullet in self.bullets:
            bullet.display()
            bullet.move()