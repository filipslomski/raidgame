from utilities.position import Position
from objects.static.dungeons.frostDungeon import FrostDungeon
from objects.static.dungeons.lavaDungeon import LavaDungeon
from objects.dynamic.boss_classes.frost_boss import FrostBoss
from objects.dynamic.boss_classes.lava_boss import LavaBoss
from dungeon_state import DungeonState
from init import Init


class GamePhase:
    phase = 1

    dungeon_boss = {
        LavaDungeon: LavaBoss,
        FrostDungeon: FrostBoss
    }

    @classmethod
    def initiate_second_phase(cls, player, boss, dungeons, collisionDetector, bulletTracker):
        player.position = Position(Init.display_width / 2, Init.display_height - player.height)
        for dungeon in dungeons:
            collisionDetector.unregister_object(dungeon)
            dungeon.remove()
        boss.position = Position(Init.display_width / 2, 50)
        boss.set_boss_type(cls.dungeon_boss[DungeonState.current_dungeon]())
        boss.boss_type.select_boss_behavior()
        collisionDetector.register_object(boss)
        bulletTracker.register_target(boss).register_target(player)
        cls.phase = 2

    @classmethod
    def initiate_third_phase(cls, player, boss, dungeons, collisionDetector):
        cls.phase = 3