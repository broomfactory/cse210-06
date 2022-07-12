import random
from constants import *
from game.casting.actor import Actor



class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._player_1_score = 0
        self._player_2_score = 0
        self._serve = random.randint(1,2)

    def add_point_1(self):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._player_1_score += 1

    def add_point_2(self):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._player_2_score += 1
   
    def get_score_1(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._player_1_score

    def get_score_2(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._player_2_score

    def get_serve_player(self):
        """Gets the number of the player whose serve it is

        Returns: Either 1 or 2        
        """
        return self._serve

    def set_serve_player(self, player_number):
        """Gets the number of the player whose serve it is

        Returns: Either 1 or 2        
        """
        self._serve = player_number
    

    def reset(self):
        """Resets the stats back to their default values."""
        self._player_1_score = 0
        self._player_2_score = 0
        self._serve = random.randint(1,2)