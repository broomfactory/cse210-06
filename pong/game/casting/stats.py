from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._player_1_score = 0
        self._player_2_score = 0

    def add_life(self):
        """Adds one life."""
        pass

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

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        pass

    def get_lives(self):
        """Gets the lives.

        Returns:
            A number representing the lives.
        """
        pass
  
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
        

    def lose_life(self):
        """Removes one life."""
        pass
    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._player_1_score = 0
        self._player_2_score = 0