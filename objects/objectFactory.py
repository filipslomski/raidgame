
class ObjectFactory():

    objects = []

    init = None

    def __init__(self, init):
        self.init = init

    def create_object(self, objectType):
        return eval(objectType.title())(self.init)
