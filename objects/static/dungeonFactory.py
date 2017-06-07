from objects.static.dungeon import Dungeon
from objects.static.dungeon_interior import DungeonInterior
from objects.static.dungeons.frostDungeon import FrostDungeon
from objects.static.dungeons.lavaDungeon import LavaDungeon
from utilities.consts.dungeons import Dungeons


class DungeonFactory(object):

    dungeon_types = {
        Dungeons.LAVA_DUNGEON : LavaDungeon,
        Dungeons.FROST_DUNGEON : FrostDungeon
    }

    @classmethod
    def create_object(self, dungeon, dungeon_type):
        return Dungeon(self.dungeon_types[dungeon_type]) if dungeon.lower() == "dungeon" \
            else DungeonInterior(self.dungeon_types[dungeon_type])