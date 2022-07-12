from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
      stats = cast.get_first_actor(STATS_GROUP)
      if stats.get_score_1() >= GAME_POINT or stats.get_score_2() >= GAME_POINT:
        callback.on_next(GAME_OVER)