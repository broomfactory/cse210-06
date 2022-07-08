from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._point = 1
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)
                
        if x < FIELD_LEFT:
            stats = cast.get_first_actor(STATS_GROUP)
            stats.add_points_2(self._point)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            stats = cast.get_first_actor(STATS_GROUP)
            stats.add_points_1(self._point)

        if y < FIELD_TOP:
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            ball.bounce_x()
            self._audio_service.play_sound(bounce_sound)
            
            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)