class LifeTracker(object):

    objects = []

    def register_object(self, object):
        if not object in self.objects:
            self.objects.append(object)
        return self

    def unregister_object(self, object):
        if object in self.objects:
            self.objects.remove(object)
        return self

    def check_health(self):
        for object in self.objects:
            if object.get_health <= 0:
                object.death()