import pygame, sys
from pygame import *
import random

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
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.surf = pygame.Surface((self.width, self.height))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = (pos, 100))
        self.pos = vec((pos, 100))
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 64)

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def move(self, dist):
        self.pos.y += dist
        self.rect.center = self.pos

    def update(self):
        hitsup = pygame.sprite.spritecollide(self ,platformup, False)
        hitsdown = pygame.sprite.spritecollide(self ,platformdown, False)
        if hitsup:
            self.pos.y = self.height
        if hitsdown:
            self.pos.y = SCREEN_HEIGHT - self.height

    def show_Score(self, surface):
        score = self.font.render(str(self.score), True, WHITE, (0, 0, 0))
        if (self.pos.x < SCREEN_WIDTH/2 and self.score > 9):
            surface.blit(score, (SCREEN_WIDTH/2 - 115, 20))
        elif (self.pos.x < SCREEN_WIDTH/2 and self.score <= 9):
            surface.blit(score, (SCREEN_WIDTH/2 - 105, 20))
        elif (self.pos.x > SCREEN_WIDTH/2 and self.score <= 9):
            surface.blit(score, (SCREEN_WIDTH/2 + 70, 20))
        else:
            surface.blit(score, (SCREEN_WIDTH/2 + 45, 20))
class Edge(pygame.sprite.Sprite):
    def __init__(self, side):
        super().__init__()
        if side == "up":
            self.surf = pygame.Surface((SCREEN_WIDTH, 15))
            self.surf.fill(WHITE)
            self.rect = self.surf.get_rect(center = (SCREEN_WIDTH / 2, 0))
            self.pos = vec((SCREEN_WIDTH / 2, 0))
        elif side == "down":
            self.surf = pygame.Surface((SCREEN_WIDTH, 15))
            self.surf.fill(WHITE)
            self.rect = self.surf.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 5))
            self.pos = vec((SCREEN_WIDTH / 2, SCREEN_HEIGHT - 5))

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

class Midline(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.surf = pygame.Surface((7, 7))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, pos))

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

class ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((14, 14))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.vel = vec(3, 3)
        self.pos = vec((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.win = 10

    def draw(self, surface):
        surface.blit(self.surf, self.rect)

    def move(self):
        self.pos += self.vel
        self.rect.center = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(self, platformup, False) or pygame.sprite.spritecollide(self, platformdown, False)
        if hits:
            self.vel.y = -self.vel.y

        if self.pos.y < P1.pos.y + 60 and self.pos.y > P1.pos.y - 60:
            if self.pos.x <= 65 and self.pos.x >= 60:
                diff = P1.pos.y - self.pos.y
                reduction_factor = (P1.pos.y/2) / 5
                if diff != 0:
                    if -1*round(diff/reduction_factor, 1) != 0:
                        self.vel.y = -1*round(diff/reduction_factor, 1)
                mixer.music.load("Pong/BallHit.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()

                self.vel.x = -self.vel.x
                if self.vel.x < 0 and self.vel.x > -6.75:
                    self.vel.x -= 0.25
                elif self.vel.x > 0 and self.vel.x < 6.75:
                    self.vel.x += 0.25
                # self.vel.x *= 1.05
                # self.vel.x = round(self.vel.x, 1)
                print(self.vel.x)

        if self.pos.y < P2.pos.y + 60 and self.pos.y > P2.pos.y - 60:
            if self.pos.x >= SCREEN_WIDTH - 65 and self.pos.x <= SCREEN_WIDTH - 60:
                diff = P2.pos.y - self.pos.y
                reduction_factor = (P2.pos.y/2) / 5
                if diff != 0:
                    if -1*round(diff/reduction_factor, 1) != 0:
                        self.vel.y = -1*round(diff/reduction_factor, 1)
                mixer.music.load("Pong/BallHit.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play()

                self.vel.x = -self.vel.x
                if self.vel.x < 0 and self.vel.x > -6.75:
                    self.vel.x -= 0.25
                elif self.vel.x > 0 and self.vel.x < 6.75:
                    self.vel.x += 0.25
                # self.vel.x *= 1.05
                # self.vel.x = round(self.vel.x, 1)
                print(self.vel.x)

        if self.pos.x < 0:
            P2.score += 1
            return True
        elif self.pos.x > SCREEN_WIDTH:
            P1.score += 1
            return False
        
    def reset(self):
        bo = self.update()
        if bo == True:
            self.pos = vec((SCREEN_WIDTH/2, random.randint(40, SCREEN_HEIGHT - 50)))
            self.vel = vec(3, 3)
        elif bo == False:
            self.pos = vec((SCREEN_WIDTH/2, random.randint(40, SCREEN_HEIGHT - 50)))
            self.vel = vec(-3, 3)

class Button(pygame.sprite.Sprite):
    def __init__(self, *args):
        super().__init__()
        self.hasImage = False
        self.clicked = False
        self.hasDrawn = False
        if (len(args) == 2):
            self.image = pygame.image.load(args[0])
            self.image = pygame.transform.scale(self.image, (100, 50))
            self.rect = self.image.get_rect()
            self.rect.x = SCREEN_WIDTH/2 - 50
            self.rect.y = args[1]
            self.hasImage = True
        elif (len(args) == 3):
            self.surf = pygame.Surface((args[0], args[0]))
            self.surf.fill(WHITE)
            self.rect = self.surf.get_rect(center = (args[1], args[2]))
        elif (len(args) == 5):
            self.image = pygame.image.load(args[0])
            self.image = pygame.transform.scale(self.image, (args[1], args[2]))
            self.rect = self.image.get_rect()
            self.rect.x = args[3]
            self.rect.y = args[4]
            self.hasImage = True

    def draw(self, surface):
        action = False
        if (self.hasImage):
            surface.blit(self.image, self.rect)
        else:
            surface.blit(self.surf, self.rect)
        
        pos = pygame.mouse.get_pos()
        
        if (self.rect.collidepoint(pos)):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                print("clicked")
                mixer.music.load("Pong/clicksond.wav")
                mixer.music.set_volume(0.7)
                mixer.music.play()
                self.clicked = True
                return True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        self.hasDrawn = True
        return action

P1 = Player(50, 16, 60)
P2 = Player(SCREEN_WIDTH - 50, 16, 60)

B1 = Button("Pong/PlayButton2.png", SCREEN_HEIGHT/2 - 55)
Menu = Button("Pong/Menu.png", SCREEN_HEIGHT/2 + 145)
Credits = Button("Pong/Credits.png", SCREEN_HEIGHT/2 + 5)
Settings = Button("Pong/Settings.png", SCREEN_HEIGHT/2 + 65)

BorderUP = Edge("up")
BorderDWN = Edge("down")
platformup = pygame.sprite.Group()
platformdown = pygame.sprite.Group()
platformup.add(BorderUP)
platformdown.add(BorderDWN)

Ball = ball()
def endGame():
    if P1.score >= Ball.win or P2.score >= Ball.win:
        return False
    return True

midline = pygame.sprite.Group()
for i in range(10, SCREEN_HEIGHT, 15):
    midline.add(Midline(i))

players = pygame.sprite.Group()
players.add(P1)
players.add(P2)

def play():
    P1.score = 0
    P2.score = 0
    while endGame():
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            P1.move(-5)
        if keys[pygame.K_s]:
            P1.move(5)
        if keys[pygame.K_DOWN]:
            P2.move(5)
        if keys[pygame.K_UP]:
            P2.move(-5)
        P1.draw(screen)
        P2.draw(screen)
        Ball.move()
        BorderDWN.draw(screen)
        BorderUP.draw(screen)
        for entity in midline:
            entity.draw(screen)
        Ball.draw(screen)
        Ball.reset()
        P1.update()
        P2.update()

        P1.show_Score(screen)
        P2.show_Score(screen)

        pygame.display.update()
        FramePerSec.tick(FPS)

def winningScreen():
    P1Win = pygame.image.load('Pong/P1Won.png')
    P1Win = pygame.transform.scale(P1Win, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
    P2Win = pygame.image.load('Pong/P2Won.png')
    P2Win = pygame.transform.scale(P2Win, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
    while Menu.clicked == False:
        screen.fill(BLACK)
        if P1.score > P2.score:
            screen.blit(P1Win, (SCREEN_WIDTH/2 - SCREEN_WIDTH/4, SCREEN_HEIGHT/4))
        else:
            screen.blit(P2Win, (SCREEN_WIDTH/2 - SCREEN_WIDTH/4, SCREEN_HEIGHT/4))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        Menu.draw(screen)
        pygame.display.update()
        FramePerSec.tick(FPS)

def CreditsScreen():
    RealCredits = pygame.image.load('Pong/RealCredits.png')
    RealCredits = pygame.transform.scale(RealCredits, (SCREEN_WIDTH/2, SCREEN_WIDTH/2))
    while Menu.clicked == False:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(RealCredits, (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 8 - 20))
        Menu.draw(screen)
        pygame.display.update()
        FramePerSec.tick(FPS)

def OptionsScreen():
    font = pygame.font.Font('freesansbold.ttf', 18)
    text1 = font.render("Ball Size", True, WHITE, BLACK)
    text1Rect = text1.get_rect(center = (SCREEN_WIDTH / 2, 30))
    text2 = font.render("Winning Score", True, WHITE, BLACK)
    text2Rect = text2.get_rect(center = (SCREEN_WIDTH / 2, 100))
    size1 = Button(7, (SCREEN_WIDTH / 2 - 50), 60)
    size2 = Button(14, (SCREEN_WIDTH / 2), 60)
    size3 = Button(24, (SCREEN_WIDTH / 2 + 50), 60)
    Five = Button("Pong/Five.png", 50, 50, 50, 125)
    Ten = Button("Pong/Ten.png", 100, 50, 150, 125)
    Fifteen = Button("Pong/Fifteen.png", 100, 50, 300, 125)
    Twenty = Button("Pong/Twenty.png", 100, 50, 450, 125)
    while Menu.clicked == False:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(text1, text1Rect)
        screen.blit(text2, text2Rect)
        size1.draw(screen)
        size2.draw(screen)
        size3.draw(screen)
        Five.draw(screen)
        Ten.draw(screen)
        Fifteen.draw(screen)
        Twenty.draw(screen)
        if size1.clicked == True:
            Ball.surf = pygame.Surface((7, 7))
            Ball.surf.fill(WHITE)
            size1.clicked = False
        elif size2.clicked == True:
            Ball.surf = pygame.Surface((14, 14))
            Ball.surf.fill(WHITE)
            size2.clicked = False
        elif size3.clicked == True:
            Ball.surf = pygame.Surface((24, 24))
            Ball.surf.fill(WHITE)
            size3.clicked = False
        if Five.clicked:
            Ball.win = 5
            Five.clicked = False
        elif Ten.clicked:
            Ball.win = 10
            Ten.clicked = False
        elif Fifteen.clicked:
            Ball.win = 15
            Fifteen.clicked = False
        elif Twenty.clicked:
            Ball.win = 20
            Twenty.clicked = False
        Menu.draw(screen)
        pygame.display.update()
        FramePerSec.tick(FPS)
     
def main_menu():
    pygame.display.set_caption("Menu")
    image = pygame.image.load('Pong/MainPage.png')
    image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT / 2))
    font = pygame.font.Font('freesansbold.ttf', 18)
    while True:
        screen.fill(BLACK)
        screen.blit(image, (0, SCREEN_HEIGHT/8))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        B1.draw(screen)
        Credits.draw(screen)
        Settings.draw(screen)
        text1 = font.render("'W' & 'S' for P1 and arrow keys for P2 to go up down", True, WHITE, BLACK)
        text2 = font.render(f"First to {Ball.win} wins", True, WHITE, BLACK)
        text1Rect = text1.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 60))
        text2Rect = text2.get_rect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 30))
        screen.blit(text1, text1Rect)
        screen.blit(text2, text2Rect)
        if B1.clicked == True:
            play()
            winningScreen()
            Menu.clicked = False
            B1.clicked = False
        if Credits.clicked == True:
            CreditsScreen()
            Credits.clicked = False
            Menu.clicked = False
        if  Settings.clicked == True:
            OptionsScreen()
            Settings.clicked = False
            Menu.clicked = False
        pygame.display.update()
        FramePerSec.tick(FPS)
main_menu()