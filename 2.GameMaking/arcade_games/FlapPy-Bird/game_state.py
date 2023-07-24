"""
This module contains the class representing the game state, A simple Enum.
"""
from enum import Enum


class State(Enum):
    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2
