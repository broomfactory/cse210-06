from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        if self._keyboard_service.is_key_down("w"): 
            racket.swing_up()
        elif self._keyboard_service.is_key_down("S"): 
            racket.swing_down()  
        else: 
            racket.stop_moving()    

            #changed the keyboard service from up and down to w and s for two player mode.