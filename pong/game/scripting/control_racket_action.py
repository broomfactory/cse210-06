from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP_1)
        if self._keyboard_service.is_key_down(W_KEY): 
            racket.swing_up()
        elif self._keyboard_service.is_key_down(S_KEY): 
            racket.swing_down()  
        else: 
            racket.stop_moving()    

            #changed the keyboard service from left and right to up and down arrows to align with game.    For single player mode.