#!/usr/bin/python
#
# Test World v0.1
# Created by Sohil876 (Arsh Khan)
# Requirements: Python 2.x, PyGame 1.9.1 and PygAnim
#
# The animation images come from POW Studios, and are available under an
# Attribution-only license. Check them out, they're really nice.
# http://powstudios.com/
#
# The walking sprites are shamelessly taken from the excellent SNES game
# Chrono Trigger.
# http://www.videogamesprites.net/ChronoTrigger

# Import libraries
import pygame
from pygame.locals import *
import sys
import time
import libs.pyganim as pyganim

# initialize the game
pygame.init()

# initialize mixer for sound
#pygame.mixer.init()

# set mouse visibility
pygame.mouse.set_visible(False)

# define some constants
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

# set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Test World!')
backgroundImage = pygame.image.load('images/swamp.png').convert()

# load and set bgm
#bgm = pygame.mixer.Sound('sounds/SETMUSIC.wav')
#bgm.play()

# load the "standing" sprites (these are single images, not animations)
front_standing = pygame.image.load('images/characterimages/crono_front.gif')
back_standing = pygame.image.load('images/characterimages/crono_back.gif')
left_standing = pygame.image.load('images/characterimages/crono_left.gif')
right_standing = pygame.transform.flip(left_standing, True, False)

playerWidth, playerHeight = front_standing.get_size()

# creating the PygAnimation objects for walking/running in all directions
animTypes = 'back_run back_walk front_run front_walk left_run left_walk'.split()
animObjs = {}
for animType in animTypes:
    imagesAndDurations = [('images/characterimages/crono_%s.%s.gif' % (animType, str(num).rjust(3, '0')), 0.1) for num in range(6)]
    animObjs[animType] = pyganim.PygAnimation(imagesAndDurations)

# create the right-facing sprites by copying and flipping the left-facing sprites
animObjs['right_walk'] = animObjs['left_walk'].getCopy()
animObjs['right_walk'].flip(True, False)
animObjs['right_walk'].makeTransformsPermanent()
animObjs['right_run'] = animObjs['left_run'].getCopy()
animObjs['right_run'].flip(True, False)
animObjs['right_run'].makeTransformsPermanent()

# have the animation objects managed by a conductor.
# With the conductor, we can call play() and stop() on all the animtion
# objects at the same time, so that way they'll always be in sync with each
# other.
moveConductor = pyganim.PygConductor(animObjs)

direction = DOWN # player starts off facing down (front)

BASICFONT = pygame.font.Font('fonts/Roboto/Roboto-Light.ttf', 18)
WHITE = (255, 255, 255)

mainClock = pygame.time.Clock()

# x and y are the player's position
x = 350
y = 285
WALKRATE = 3
RUNRATE = 6

instructionSurf = BASICFONT.render('Arrow keys to move. Hold shift to run.', True, WHITE)
instructionRect = instructionSurf.get_rect()
instructionRect.bottomleft = (10, WINDOWHEIGHT - 10)
running = moveUp = moveDown = moveLeft = moveRight = False

while True:
    windowSurface.fill(0)
    windowSurface.blit(backgroundImage, [0, 0])
    windowSurface.blit(instructionSurf, instructionRect)

    for event in pygame.event.get(): # event handling loop

        # handle ending the program
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key in (K_LSHIFT, K_RSHIFT):
                # player has started running
                running = True

            if event.key == K_UP:
                moveUp = False
                moveDown = False
                if not moveLeft and not moveRight:
                    # only change the direction to up if the player wasn't moving left/right
                    direction = UP
            elif event.key == K_DOWN:
                moveDown = False
                moveUp = False
                if not moveLeft and not moveRight:
                    direction = DOWN
            elif event.key == K_LEFT:
                moveLeft = True
                moveRight = False
                if not moveUp and not moveDown:
                    direction = LEFT
            elif event.key == K_RIGHT:
                moveRight = True
                moveLeft = False
                if not moveUp and not moveDown:
                    direction = RIGHT
            
        elif event.type == KEYUP:
            if event.key in (K_LSHIFT, K_RSHIFT):
                # player has stopped running
                running = False
                
            if event.key == K_UP:
                moveUp = False
                # if the player was moving in a sideways direction before, change the direction the player is facing.
                if moveLeft:
                    direction = LEFT
                if moveRight:
                    direction = RIGHT
            elif event.key == K_DOWN:
                moveDown = False
                if moveLeft:
                    direction = LEFT
                if moveRight:
                    direction = RIGHT
            elif event.key == K_LEFT:
                moveLeft = False
                if moveUp:
                    direction = UP
                if moveDown:
                    direction = DOWN
            elif event.key == K_RIGHT:
                moveRight = False
                if moveUp:
                    direction = UP
                if moveDown:
                    direction = DOWN
            
    if moveUp or moveDown or moveLeft or moveRight:
        # draw the correct walking/running sprite from the animation object
        moveConductor.play() # calling play() while the animation objects are already playing is okay; in that case play() is a no-op
        if running:
            if direction == UP:
                animObjs['back_run'].blit(windowSurface, (x, y))
            elif direction == DOWN:
                animObjs['front_run'].blit(windowSurface, (x, y))
            elif direction == LEFT:
                animObjs['left_run'].blit(windowSurface, (x, y))
            elif direction == RIGHT:
                animObjs['right_run'].blit(windowSurface, (x, y))
        else:
            # walking
            if direction == UP:
                animObjs['back_walk'].blit(windowSurface, (x, y))
            elif direction == DOWN:
                animObjs['front_walk'].blit(windowSurface, (x, y))
            elif direction == LEFT:
                animObjs['left_walk'].blit(windowSurface, (x, y))
            elif direction == RIGHT:
                animObjs['right_walk'].blit(windowSurface, (x, y))


        # actually move the position of the player
        if running:
            rate = RUNRATE
        else:
            rate = WALKRATE

        if moveUp:
            y -= rate
        if moveDown:
            y += rate
        if moveLeft:
            x -= rate
        if moveRight:
            x += rate

    else:
        # standing still
        moveConductor.stop() # calling stop() while the animation objects are already stopped is okay; in that case stop() is a no-op
        if direction == UP:
            windowSurface.blit(back_standing, (x, y))
        elif direction == DOWN:
            windowSurface.blit(front_standing, (x, y))
        elif direction == LEFT:
            windowSurface.blit(left_standing, (x, y))
        elif direction == RIGHT:
            windowSurface.blit(right_standing, (x, y))

    # make sure the player does move off the screen
    if x < 0:
        x = 0
    if x > WINDOWWIDTH - playerWidth:
        x = WINDOWWIDTH - playerWidth
    if y < 0:
        y = 0
    if y > WINDOWHEIGHT - playerHeight:
        y = WINDOWHEIGHT - playerHeight

    pygame.display.update()
    mainClock.tick(30) # Feel free to experiment with any FPS setting.

