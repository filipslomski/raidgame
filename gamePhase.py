from utilities.position import Position
from init import Init


class GamePhase:
    phase = 1

    @classmethod
    def initiate_second_phase(cls, player, boss, dungeons, collisionDetector):
        player.position = Position(Init.display_width / 2, Init.display_height - player.height)
        for dungeon in dungeons:
            collisionDetector.unregister_object(dungeon)
            dungeon.remove()
        boss.position = Position(Init.display_width / 2, 50)
        collisionDetector.register_object(boss)
        cls.phase = 2