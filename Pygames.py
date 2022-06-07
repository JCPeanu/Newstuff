import pygame, sys
from pygame.locals import *
 
# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()
 
# Setting up color objects with an (R,G,B)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((300, 300))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Example") #window title
 
# Creating Lines and Shapes examples
pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (130, 170))
pygame.draw.line(DISPLAYSURF, BLUE, (150, 130), (170, 170))
pygame.draw.line(DISPLAYSURF, GREEN, (130, 170), (170, 170))
pygame.draw.circle(DISPLAYSURF, BLACK, (100, 50), 30)
pygame.draw.circle(DISPLAYSURF, BLACK, (200, 50), 30)
pygame.draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
pygame.draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))
 
# Beginning Game Loop
while True: #This means the window will be forever displayed...
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT: #...except when the user closes it.
            pygame.quit()
            sys.exit()
 
    FramePerSec.tick(FPS)