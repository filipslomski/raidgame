from objects.static.dungeon import Dungeon

class DungeonFactory(object):

    init = None

    def __init__(self, init):
        self.init = init

    def create_object(self, dungeon_type):
        return Dungeon(dungeon_type)