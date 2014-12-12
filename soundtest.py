"""
Plays sound effect sword.mp3 in same file as code
"""

import pygame
import os
import sys


pygame.mixer.init()
throw = pygame.mixer.Sound('sword.wav')


gameloop = True
i = 0
while gameloop:
	throw.play()
