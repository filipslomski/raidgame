class CollisionDetector(object):

    objects = []

    def __init__(self, *args):
        for arg in args:
            self.objects.append(arg)

    def check_collisions(self):
        pass

    def check_collision(self, position_a, position_b):
        pass