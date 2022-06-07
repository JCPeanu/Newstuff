import pygame, sys
from pygame import *
import random
import time

pygame.init()
vec = pygame.math.Vector2 

FPS = 120
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (190, 190, 190)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700

mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(GRAY)
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Flappybird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (75, 100)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.pos = vec((75, 100))
        self.score = 0
        self.font = pygame.font.Font('flappy-bird-font/flappy-bird-font.ttf', 64)

    def show_Score(self, surface):
        score = self.font.render(str(self.score), True, (0, 0, 0))
        surface.blit(score, (SCREEN_WIDTH/2 - 20, 20))

    def move(self):
        self.acc = vec(0,0.15)

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos  
    
    def jump(self):
        mixer.music.load("Jump.wav")
        mixer.music.set_volume(0.7)
        mixer.music.play()
        self.vel.y = -4

    #This method is used to read if one of the keys is pressed and move the sprite
    def update(self):

        hits = pygame.sprite.spritecollide(P1 ,platforms, False)
        if hits:
            mixer.music.load("Hit.wav")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            self.pos.y = 300
            self.image = pygame.image.load("FlappybirdDead.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            return False
        return True

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class upperplatform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PipeDown.png")
        self.image = pygame.transform.scale(self.image, (75, 600))

        self.rect = self.image.get_rect()
        self.rand = random.randint(-150, 150)
        self.rect.center = (400, self.rand + 200)# min = -200

        self.pos = vec((400, self.rand + 200))
        self.vel = vec(-1,0)

    def move(self):
            self.pos += self.vel
            self.rect.midbottom = self.pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def getRand(self):
        return self.rand

class lowerplatform(pygame.sprite.Sprite):
    def __init__(self, rand):
        super().__init__()
        self.rand = rand
        self.image = pygame.image.load("Pipe.png")
        self.image = pygame.transform.scale(self.image, (75, 600))

        self.rect = self.image.get_rect()
        self.rect.center = (400, self.rand + 200 + 800)# min = -200

        self.pos = vec((400, self.rand + 800 + 150))
        self.vel = vec(-1,0)
        self.Drawn = False

    def move(self):
            self.pos += self.vel
            self.rect.midbottom = self.pos

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 10))
    def draw(self, surface):
        surface.blit(self.surf, self.rect)

class Button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Start-button-sprite.png")
        self.image = pygame.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 400
        self.clicked = False
        self.hasDrawn = False

    def draw(self, surface):
        action = False
        surface.blit(self.image, self.rect)
        pos = pygame.mouse.get_pos()
        
        if (self.rect.collidepoint(pos)):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                print("clicked")
                mixer.music.load("clicksond.wav")
                mixer.music.set_volume(0.7)
                mixer.music.play()
                self.clicked = True
                return True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.hasDrawn = True
        return action

P1 = Player()

Pipe1_Up = upperplatform()
Pipe1_Down = lowerplatform(Pipe1_Up.getRand())

Pipe2_Up = upperplatform()
Pipe2_Down = lowerplatform(Pipe2_Up.getRand())
Pipe2_Up.pos = vec((623, Pipe2_Up.rand + 200))
Pipe2_Down.pos = vec((623, Pipe2_Down.rand + 150 + 800))

Plat = platform()

B1 = Button()

platforms = pygame.sprite.Group()
platforms.add(Pipe1_Up)
platforms.add(Pipe1_Down)
platforms.add(Pipe2_Up)
platforms.add(Pipe2_Down)
platforms.add(Plat)

def reset():
    P1.image = pygame.image.load("Flappybird.png")
    P1.image = pygame.transform.scale(P1.image, (50, 50))
    P1.rect = P1.image.get_rect()
    P1.rect.center = (75, 100)
    P1.vel = vec(0,0)
    P1.acc = vec(0,0)
    P1.pos = vec((75, 100))
    P1.score = 0
    P1.font = pygame.font.Font('flappy-bird-font/flappy-bird-font.ttf', 64)

    Pipe1_Up.rand = random.randint(-150, 150)
    Pipe1_Up.rect.center = (400, Pipe1_Up.rand + 200)
    Pipe1_Up.pos = vec((400, Pipe1_Up.rand + 200))
    Pipe1_Up.vel = vec(-1,0)

    Pipe1_Down.rect.center = (400, Pipe1_Up.rand + 200 + 800)
    Pipe1_Down.pos = vec((400, Pipe1_Up.rand + 800 + 150))
    Pipe1_Down.vel = vec(-1,0)

    Pipe2_Up.rand = random.randint(-150, 150)
    Pipe2_Up.rect.center = (623, Pipe2_Up.rand + 200)
    Pipe2_Up.pos = vec((623, Pipe2_Up.rand + 200))
    Pipe2_Up.vel = vec(-1,0)

    Pipe2_Down.rect.center = (623, Pipe2_Up.rand + 200 + 800)
    Pipe2_Down.pos = vec((623, Pipe2_Up.rand + 800 + 150))
    Pipe2_Down.vel = vec(-1,0)

    P1.score = 0

    B1.hasDrawn = False

    P1.move()
    P1.update()
    Pipe1_Up.move()
    Pipe1_Down.move()
    Pipe2_Up.move()
    Pipe2_Down.move()

while True:
    #pygame is continually reading events
    for event in pygame.event.get():
        #if the user clicks the x on the top bar, quit the game safely
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump()
    screen.fill(GRAY)
 
    P1.draw(screen)
    Pipe1_Up.draw(screen)
    Pipe1_Down.draw(screen)
    Pipe2_Up.draw(screen)
    Pipe2_Down.draw(screen)
    Plat.draw(screen)
    P1.show_Score(screen)

    if B1.hasDrawn == True:
        if B1.clicked == False:
            B1.draw(screen)
            Pipe1_Up.vel = vec(0, 0)
            Pipe1_Down.vel = vec(0, 0)
            Pipe2_Up.vel = vec(0, 0)
            Pipe2_Down.vel = vec(0, 0)
            if P1.score <= 5:
                meme = pygame.image.load("YouSuck.jpeg")
                meme = pygame.transform.scale(meme, (300, 300))
                getrect = meme.get_rect(center = (200, 200))
                screen.blit(meme, getrect)
            elif P1.score < 50:
                meme = pygame.image.load("Meh.jpeg")
                meme = pygame.transform.scale(meme, (300, 300))
                getrect = meme.get_rect(center = (200, 200))
                screen.blit(meme, getrect)
            elif P1.score >= 50:
                meme = pygame.image.load("Welldone.jpeg")
                meme = pygame.transform.scale(meme, (300, 300))
                getrect = meme.get_rect(center = (200, 200))
                screen.blit(meme, getrect)
            Font = pygame.font.Font('freesansbold.ttf', 32)
            text = Font.render("Score: " + str(P1.score), True, (0,0,0))
            textRect = text.get_rect(center = (200, 375))
            screen.blit(text, textRect)
        else:
            reset()
    else:
        if P1.update() == True:
            P1.move()
            P1.update()
            Pipe1_Up.move()
            Pipe1_Down.move()
            Pipe2_Up.move()
            Pipe2_Down.move()
        else:
            B1.draw(screen)

    if (Pipe1_Up.pos.x < 0):
        rand = random.randint(-150, 150)
        Pipe1_Up.rand = rand
        Pipe1_Up.pos = vec((437, Pipe1_Up.rand + 200))
        Pipe1_Down.rand = rand
        Pipe1_Down.pos = vec((437, Pipe1_Down.rand + 150 + 800))

    if (Pipe2_Up.pos.x < 0):
        rand = random.randint(-150, 150)
        Pipe2_Up.rand = rand
        Pipe2_Up.pos = vec((437, Pipe2_Up.rand + 200))
        Pipe2_Down.rand = rand
        Pipe2_Down.pos = vec((437, Pipe2_Down.rand + 150 + 800))

    if (Pipe1_Up.pos.x == 75 or Pipe2_Up.pos.x == 75):
        P1.score += 1

    pygame.display.update()
    FramePerSec.tick(FPS)