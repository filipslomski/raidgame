from objects.static.dungeon import Dungeon
from objects.static.dungeon_interior import DungeonInterior


class DungeonFactory(object):

    @staticmethod
    def create_object(dungeon, dungeon_type):
        return Dungeon(dungeon_type) if dungeon == "Dungeon" else DungeonInterior(dungeon_type)