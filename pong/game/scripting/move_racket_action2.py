from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction2(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP_2)
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        y = position.get_y()
        
        position = position.add(velocity)

        if y < 0:
            position = Point(0, position.get_x())
        elif y > (SCREEN_WIDTH - RACKET_WIDTH):
            position = Point(SCREEN_WIDTH - RACKET_WIDTH, position.get_x())
            
        body.set_position(position)
        