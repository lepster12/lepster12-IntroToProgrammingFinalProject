# content from kids can code: http://kidscancode.org/blog/
# guides from w3schools python tutorial
# import libraries and modules
# help from Eric and Mark



# GOALS
# Create another class with Player 2
# increase playing ground with game settings
# add code where when each player hits a mob, another one spawns
# add competition goal, first to hit #points wins
# add ID to player, "P1" and "P2" to respective player
# add a starting screen
# add a sounds for each player, so that you can differentiate who hits a mob

from platform import platform
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from os import path

vec = pg.math.Vector2

# # Setup asset folders here - images sounds etc.
# Computer_Science = os.path.dirname(__file__)
# Images = os.path.join(Computer_Science, 'images')

# game settings 
WIDTH = 1450
HEIGHT = 875
FPS = 30

# player settings
PLAYER_FRIC = -0.1
PLAYER_GRAV = .9875
POINTS = 0 

PLAYER2_FRIC = -0.1
PLAYER2_GRAV =.9875
POINTS2 = 0
GOAL = 1000 #set goal that when reached ends game; "player beats other player"
CONTROLS = "Player1 Controls."
CONTROLS2 = "Player2 Controls."
ID1 = "Player1"

# HEALTH = 10 #start with 10 health
# YAY = 0 #start with no yay's

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE2 = (0, 255, 255)
BLUE = (0, 0, 255)


def colorbyte():
    return random.randint(0,255) #defined for add mob in line #233

# # images
# background = pg.image.load(path.join(Images, 'ocean'))
# background_rect = background.get_rect()

def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect) # this block of code is used to def "draw_text," which is used to insert text at the top of the game

# sprites...
class Player(Sprite): #player 1 settings
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN) #color of player
        # self.image.fill("ID1")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2) # controls where player spawns
        self.vel = vec(0,0) #controls player starting velocity on x and y axis
        self.acc = vec(0,0) #controls player acc. on x and y axis
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -2 #controls where exactly player goes if key is pressed. If this was 2, then it would go the opposite dirreciton of pressed key
        if keys[pg.K_d]:
            self.acc.x = 2 #same as above, if this was -2, it would go in opposite direction of where key is pressed
        if keys[pg.K_w]:
            self.acc.y = -2
        if keys[pg.K_s]:
            self.acc.y = 2 #controls for player, WASD
    def jump(self):
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        if hits:
            print("i've collided...")
            self.vel.y = -20
    def update(self):
        self.acc = vec(0,0) # controls set velocity from very begining, will move at #m/s for x or y axis for which is changed
        self.controls()
        
        # friction
        self.acc += self.vel * PLAYER_FRIC 
        # self.acc.x += self.vel.x * PLAYER_FRIC
        # self.acc.y += self.vel.y * PLAYER_FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.rect.midbottom = self.pos
    

class Player2(Sprite): #class of palyer 2, what adds player 2
    def __init__(self2):
        Sprite.__init__(self2)
        self2.image = pg.Surface((50, 50)) #
        self2.image.fill(BLUE2)# color of player2
        self2.rect = self2.image.get_rect()
        self2.rect.center = (WIDTH/2, HEIGHT/2) #
        self2.pos = vec(WIDTH/2, HEIGHT/4) # where player2 starts
        self2.vel = vec(0,0)
        self2.acc = vec(0,0)
    def controls(self2):
        keys = pg.key.get_pressed()
        if keys[pg.K_j]:
            self2.acc.x = -2
        if keys[pg.K_l]:
            self2.acc.x = 2
        if keys[pg.K_i]:
            self2.acc.y = -2
        if keys[pg.K_k]:
            self2.acc.y = 2 
    def jump(self2):
        hits = pg.sprite.spritecollide(self2, all_platforms, False)
        if hits:
            print("i've collided...")
            self2.vel.y = -20
    def update(self2):
        self2.acc = vec(0,0)
        self2.controls()

# this entire block has the same code for player1
        
        # friction
        self2.acc += self2.vel * PLAYER2_FRIC
        # self.acc.x += self.vel.x * PLAYER_FRIC
        # self.acc.y += self.vel.y * PLAYER_FRIC
        self2.vel += self2.acc
        self2.pos += self2.vel + 0.5 * self2.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self2.rect.midbottom = self2.pos

class Platform(Sprite): #creats a platform on the screen
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN) #color of platform
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Mob(Sprite): #class of mob
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.color = color #fills color
        self.image.fill(color) #chooses random color for each mob from defined colors at the top
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4 # speed of mobs
        self.speed2 = 1
      
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed2
        if self.rect.right > WIDTH or self.rect.x < 0: #makes it so that if borders of window are hit they rebound and go back
            self.speed *= -1.10 #this part creates it so that when it hits  in width section, it bounces off with # speed, the higher the number, the greater the bounce off speed is
        if self.rect.top > HEIGHT or self.rect.y < 0:
            self.speed2 *= -1.10 #this part creates it so that when it hits  in height section, it bounces off with # speed, the higher the number, the greater the bounce off speed is
        # if self.pos.x > WIDTH:
        #     self.pos.x = 0
        # if self.pos.x < 0:
        #     self.pos.x = WIDTH

        # if self.pos.y > HEIGHT:
        #     self.pos.x = 0
        # if self.pos.x < 0:
        #     self.pos.y = HEIGHT
        
        # self.rect.x = self.pos.x
        # self.rect.y = self.pos.y
        # def update(self):
    #     self.acc = vec(1,1) # controls set velocity from very begining, will move at #m/s for x or y axis for which is changed
    #     self.Mob()


# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
# create a group for all sprites
all_sprites = pg.sprite.Group()
all_platforms = pg.sprite.Group()
mobs = pg.sprite.Group()

# instantiate classes
player = Player()
player2 = Player2()
plat = Platform(WIDTH/1, HEIGHT/1, 1, 1)
#plat1 = Platform(75, 300, 100, 35)
# mob = Mob(25, 57, 25, 25)

# add instances to groups
all_sprites.add(player)
all_sprites.add(player2)
all_sprites.add(plat)
#all_sprites.add(plat1)
# all_sprites.add(mob)
all_platforms.add(plat)
#all_platforms.add(plat1)

for i in range(50): # number of mods that are spawned with the game when it opens
    # instantiate mob class repeatedly
    m = Mob(randint(0, WIDTH), randint(0,HEIGHT), 25, 25, (randint(0,255), randint(0,255) , randint(0,255)))
    all_sprites.add(m)
    mobs.add(m)
print(mobs)
# Game loop
running = True
while running:
    # keep the loop running using clock
    dt = clock.tick(FPS)

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
    
    ############ Update ##############
    # update all sprites
    hits = pg.sprite.spritecollide(player, all_platforms, False)
    # if hits:
    #     print("i've collided...with a plat")
    mobhits = pg.sprite.spritecollide(player, mobs, True) 
    if mobhits:
        POINTS += 20 # number of points added per each mob hit
        print(POINTS)
        print("i've collided...with a mob")
        print(mobhits[0].color)
    all_sprites.update()
    # if mobhits:
        # HEALTH -= 1
        # print ("You gained a health point")    # touching a mob takes a health point
        # if HEALTH == 5:
        #     print ("BE CAREFUL, YOU ONLY HAVE 5 HITPOINTS LEFT") # if you red 5 in health, the saying is printed
        # if POINTS == 90:
        #     print ("YOU WIN!") #if you reach 90 points you win
        # if HEALTH == 0:
        #     break #if you reach a health total of 0, the game ends
    if mobhits:
        print("ive struck a mob")
        m = Mob(randint(0,WIDTH), randint(0,HEIGHT), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
        all_sprites.add(m)
        mobs.add(m)      # every time a player hits a mob, a new one spawns
    if POINTS == GOAL:
        break #if GOAL # is met, game ends and player wins
        
    # if mobhits:
    #     YAY += 1
    #     print ("yay") #yay is printed every time you hit a mob
    hits = pg.sprite.spritecollide(player2, all_platforms, False)
    # if hits:
    #     print("i've collided...with a plat")
    mobhits = pg.sprite.spritecollide(player2, mobs, True)
    if mobhits:
        POINTS2 += 20
        print(POINTS2)
        print("i've collided...with a mob")
        print(mobhits[0].color)
    all_sprites.update()
    # if mobhits:
    if mobhits:
        m = Mob(randint(0,WIDTH), randint(0,HEIGHT), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
        all_sprites.add(m)
        mobs.add(m)
    if POINTS2 == GOAL:
        break
        
 #all same code as above player rules and game rules

    ############ Draw ################
    # draw the background screen

    # screen.fill(BLACK)
    # screen.blit(background, background_rect)

    screen.fill(BLACK)
    # draw all sprites
    all_sprites.draw(screen)
    draw_text("POINTS p1: " + str(POINTS), 22, GREEN, WIDTH / 2, HEIGHT / 15) #draws text, which is made possible by defining draw_text
    draw_text("POINTS P2: " + str(POINTS2), 22, BLUE2, WIDTH / 2, HEIGHT / 10)
    draw_text("GOAL OF GAME: " + str(GOAL), 22, RED, WIDTH / 2, HEIGHT / 50)
    draw_text("WASD: " + str(CONTROLS), 22, GREEN, WIDTH / 8, HEIGHT / 50)
    draw_text("IJKL: " + str(CONTROLS2), 22, BLUE2, WIDTH / 8, HEIGHT / 10)
    # draw_text("HEALTH: " + str(HEALTH), 15, WHITE, WIDTH / 2, HEIGHT / 10)
    

    # draw_text("FPS: " + str(dt), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    # draw_text("asdfasdfasdfasdfasdf: " + str(dt), 22, WHITE, WIDTH / 2, HEIGHT / 24)

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()