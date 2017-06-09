from bullets_state import BulletsState


class BulletTracker(object):

    bullets = []
    targets = []

    def register_target(self, object):
        if not object in self.targets:
            self.targets.append(object)
        return self

    def unregister_object(self, object):
        if object in self.targets:
            self.targets.remove(object)
        return self

    def create_bullets(self):
        if BulletsState.shoot:
            pass

