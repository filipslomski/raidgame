class CollisionDetector(object):

    objects = []

    def register_object(self, object):
        if not object in self.objects:
            self.objects.append(object)
        return self

    def unregister_object(self, object):
        if object in self.objects:
            self.objects.remove(object)
        return self

    def check_collisions(self):
        objects_in_collision = []
        for object_a in self.objects:
            for object_b in self.objects:
                if not object_a is object_b and self.check_collision(object_a, object_b):
                    objects_in_collision.extend([object_a, object_b])
                    object_a.collision(object_b)
                    object_b.collision(object_a)
        return objects_in_collision

    def check_collision(self, object_a, object_b):
        x_axis_collision = False
        y_axis_collision = False
        if (object_a.position.x >= object_b.position.x and
                object_a.position.x - object_b.position.x < object_b.width or
                object_b.position.x > object_a.position.x and
                object_b.position.x - object_a.position.x < object_a.width):
            x_axis_collision = True
        if x_axis_collision:
            if (object_a.position.y >= object_b.position.y and
                    object_a.position.y - object_b.position.y < object_b.height or
                    object_b.position.y > object_a.position.y and
                    object_b.position.y - object_a.position.y < object_a.height):
                y_axis_collision = True

        return y_axis_collision and x_axis_collision
