"""
This module contains very useful variables for the game.
"""

import os
import arcade

# List of different pipe images (Green / Red) (Choose one)
PIPES = ["assets" + os.sep + "sprites" + os.sep + "pipe-green.png", "assets" + os.sep + "sprites" + os.sep + "pipe-red.png"]
# Image of the base floor
BASE = "assets" + os.sep + "sprites" + os.sep + "base.png"
# List of different background images (Day / Night) (Choose one)
PLAY_BUTTON = "assets" + os.sep + "sprites" + os.sep + "play.png"
BACKGROUNDS = ["assets" + os.sep + "sprites" + os.sep + "background-day.png", "assets" + os.sep + "sprites" + os.sep + "background-night.png"]
# Dict holding the animation images for different birds colors (Choose one)
BIRDS = {'yellow': ["assets" + os.sep + "sprites" + os.sep + "yellowbird-downflap.png", "assets" + os.sep + "sprites" + os.sep + "yellowbird-midflap.png",
                    "assets" + os.sep + "sprites" + os.sep + "yellowbird-upflap.png"],
         'red': ["assets" + os.sep + "sprites" + os.sep + "redbird-downflap.png", "assets" + os.sep + "sprites" + os.sep + "redbird-midflap.png",
                    "assets" + os.sep + "sprites" + os.sep + "redbird-upflap.png"],
         'blue': ["assets" + os.sep + "sprites" + os.sep + "bluebird-downflap.png", "assets" + os.sep + "sprites" + os.sep + "bluebird-midflap.png",
                    "assets" + os.sep + "sprites" + os.sep + "bluebird-upflap.png"]}
# Start screen (Tap tap!)
GET_READY_MESSAGE = "assets" + os.sep + "sprites" + os.sep + "message.png"
# Game over logo
GAME_OVER = "assets" + os.sep + "sprites" + os.sep + "gameover.png"
# dict mapping sound name to arcade sound object
SOUNDS = {'wing': arcade.load_sound("assets" + os.sep + "audio" + os.sep + "wing.wav"),
          'die': arcade.load_sound("assets" + os.sep + "audio" + os.sep + "die.wav"),
          'hit': arcade.load_sound("assets" + os.sep + "audio" + os.sep + "hit.wav"),
          'point': arcade.load_sound("assets" + os.sep + "audio" + os.sep + "point.wav"),
          'swoosh': arcade.load_sound("assets" + os.sep + "audio" + os.sep + "swoosh.wav")}
# TODO: Better variables names :)

# Minimum height for a pipe
MIN_HEIGHT = 50
# Minimum gap between two pipes (The gap that a bird can go through)
# MIN_GAP = 100

GAP_SIZE = 120

# How many pixels per jump
JUMP_DY = 60
# How many pixels per frame
JUMP_STEP = 4
DY = 2
# Gravity pixels
GRAVITY = 2

ANGLEP = 15
ANGLEM = -1.5

# Images for the score board.
SCORE = {
    '0': 'assets' + os.sep + 'sprites' + os.sep + '0.png',
    '1': 'assets' + os.sep + 'sprites' + os.sep + '1.png',
    '2': 'assets' + os.sep + 'sprites' + os.sep + '2.png',
    '3': 'assets' + os.sep + 'sprites' + os.sep + '3.png',
    '4': 'assets' + os.sep + 'sprites' + os.sep + '4.png',
    '5': 'assets' + os.sep + 'sprites' + os.sep + '5.png',
    '6': 'assets' + os.sep + 'sprites' + os.sep + '6.png',
    '7': 'assets' + os.sep + 'sprites' + os.sep + '7.png',
    '8': 'assets' + os.sep + 'sprites' + os.sep + '8.png',
    '9': 'assets' + os.sep + 'sprites' + os.sep + '9.png',
}
