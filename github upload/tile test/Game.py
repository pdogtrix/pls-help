import pygame, sys
from pygame.locals import *  # imports additional commands used for event handling
import os
from settings import *
from level import Level
from game_data import level_3

pygame.init()  # initializes the pygame library to be used

clock = pygame.time.Clock()  # use clock to set the framerate
screen = pygame.display.set_mode((screen_width, screen_height))  # creates the screen and sets the size 640 h, 480 
level = Level(level_3, screen)




################ main game loop ###################

while True:
    for event in pygame.event.get(): # manage events in the Pygame events que
        if event.type == QUIT:
            pygame.quit()
            os.sys.exit()

    screen.fill('black')
    level.run()

     

    clock.tick(60)          # set framerate (fps)
    pygame.display.update() # update the python display