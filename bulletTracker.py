from bullets_state import BulletsState


class BulletTracker(object):

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
            if object.shoot != False:
                pass
                #new bullet