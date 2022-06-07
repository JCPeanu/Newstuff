#adapted from this example
#https://coderslegacy.com/python/python-pygame-tutorial/
 
import pygame #pip install pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, QUIT, KEYDOWN)
import random
import sys
 
#initialize the game!
pygame.init()
 
#FPS stands for frames per second
FPS = 60
FramePerSec = pygame.time.Clock()
 
#define (R, G, B) colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (190, 190, 190)
 
# Screen information
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
 
#set "screen" as the game's main display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(GRAY)
 
#window title
pygame.display.set_caption("Unstoppable highway")
 
#Enemy is going to be a type of sprite of PyGame
class Enemy(pygame.sprite.Sprite):
    #Defines what to do when you create a new Enemy
    def __init__(self):
        super().__init__()
        #load the image and convert to a format that facilitates efficiency of execution
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        #resize the image
        self.image = pygame.transform.scale(self.image, (300, 149))
        #flip the image horizontally
        self.image = pygame.transform.flip(self.image, True, False)
        #get a bounding rectangle for that image
        self.rect = self.image.get_rect()
        #set the center of the image as a coordinate
        self.rect.center = (SCREEN_WIDTH, random.randint(40, SCREEN_HEIGHT - 40))
 
    #Every Enemy object can move
    def move(self):
        #Move 10 pixels to the left
        self.rect.move_ip(-10, 0)
        #If the sprite moves beyond the screen limits then move it back to the start
        if (self.rect.left < -300):
            self.rect.right = SCREEN_WIDTH+300
            self.rect.center = (SCREEN_WIDTH+300, random.randint(80, SCREEN_HEIGHT - 80))
 
    #draw is necessary to show it on the screen
    def draw(self, surface):
        #blit is used to draw a surface on top of another
        surface.blit(self.image, self.rect) #draw the image of the object onto the screen
 
#Even though our game is single player, it has a sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (300, 149))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    #This method is used to read if one of the keys is pressed and move the sprite
    def update(self):
        #This will return a list
        pressed_keys = pygame.key.get_pressed()
        #move the car up but not above pixel 0
        if self.rect.top > 0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        #move the car down but not below the bottom of the screen
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)
 
#Create both Player and Enemy
P1 = Player()
E1 = Enemy()
 
#An infinite loop to run the game endlessly
while True:
    #pygame is continually reading events
    for event in pygame.event.get():
        #if the user clicks the x on the top bar, quit the game safely
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #otherwise, update the player's and enemy's position
    P1.update()
    E1.move()
 
    # The screen is filled again to reset the previous positions visually
    screen.fill(GRAY)
 
    #draw on the screen the cars with updated positions
    P1.draw(screen)
    E1.draw(screen)
    
    #commit changes
    pygame.display.update()
    FramePerSec.tick(FPS)
