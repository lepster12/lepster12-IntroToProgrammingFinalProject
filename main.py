# content from kids can code: http://kidscancode.org/blog/
# guides from w3schools python tutorial
# import libraries and modules
# tkinter loader screen https://www.pythontutorial.net/tkinter/tkinter-progressbar/
# arrow keys for movement https://www.codespeedy.com/movement-of-object-when-arrow-keys-are-pressed-in-pygame/
# figured out background image from copying from https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode%2Fper1game%2Fmain%5Fside%2Epy&parent=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode%2Fper1game
# text code for welcome message in game https://stackoverflow.com/questions/52856030/how-to-fade-in-and-out-a-text-in-pygame

from platform import platform
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from os import path
import time
from time import sleep
import sys
import pygame as pg1
from settings import *

vec = pg.math.Vector2

Computer_Science = os.path.dirname(__file__)

POINTS = 140

# HEALTH = 10 #start with 10 health
# YAY = 0 #start with no yay's

# start screen text
line_1 = "You've been abandoned by your country..."
line_2 = "Your current mission is to survive and make it back home..."
line_3 = "Good luck soldier. God Speed."

# images
background = pg.image.load('Space_Background.png')
background_rect = background.get_rect()

FighterJet = pg.image.load('Spaceship_red.png')
# FighterJet_rect = background.get_rect()
# FighterJet.set_colorkey(BLACK)
# FighterJet = pg.transform.scale(FighterJet, (5,5))


def start_text():
    
    screen = pg1.display.set_mode((1350, 480))
    font = pg1.font.Font(None, 64)
    blue = pg1.Color('red') # sets color of text that is displayed:
    orig_surf = font.render("Welcome to Run From Asteroids.", False, blue) # my message
    pg1.display.set_caption("Run From Asteroids...")
    txt_surf = orig_surf.copy()
    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pg1.Surface(txt_surf.get_size(), pg1.SRCALPHA) # ALPHA is the text surface, without ALPHA, the spot where text is supposed to be would just be white
    alpha = 200


    while True:
        for event in pg1.event.get():
            if event.type == pg1.QUIT:
                return

        if alpha > 0:
            alpha = max(alpha-4, 0)
            txt_surf = orig_surf.copy()  # calls txt_surf to display
            alpha_surf.fill((255, 255, 255, alpha)) # fills the area where text is supposed to be
            txt_surf.blit(alpha_surf, (0, 0), special_flags=pg1.BLEND_RGBA_MULT) # displays area (.blit)

        screen.fill((30, 30, 30))
        screen.blit(txt_surf, (30, 60)) 
        pg1.display.flip() # gives command to display this surface
    

    
if __name__ == '__main__': 
    pg1.init()
    start_text()
    pg1.quit()


time.sleep(.4) #stops going through the code for .2 second. Gives second window time to load up

def colorbyte():
    return random.randint(0,255) #defined for add mob in line #233

def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect) # this block of code is used to def "draw_text," which is used to insert text at the top of the game

class Banner(Sprite): # creates a platform on the screen
    def __init__(self, x, y, w, h): # gives this function parameters
        Sprite.__init__(self)
        self.image = pg.Surface((w,h)) # sets up image of surface
        self.image = pg.image.load('star_background.png') # loads this image to background of Banner
        self.rect = self.image.get_rect() # calls image that is loaded
        self.rect.x = x
        self.rect.y = y


# sprites...
class Player(Sprite): #player 1 settings
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((1, 1))
        # self.image.fill(BLACK) #color of player
        # self.image.fill("ID1")
        self.image = pg.image.load('Spaceship_red.png') #loads this image as Player
        # FighterJet.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2) # controls where player spawns
        self.vel = vec(0,0) #controls player starting velocity on x and y axis
        self.acc = vec(0,0) #controls player acc. on x and y axis
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -3 #controls where exactly player goes if key is pressed. If this was 2, then it would go the opposite dirreciton of pressed key
        if keys[pg.K_d]:
            self.acc.x = 3 #same as above, if this was -2, it would go in opposite direction of where key is pressed
        if keys[pg.K_w]:
            self.acc.y = -3
        if keys[pg.K_s]:
            self.acc.y = 3 #controls for player, WASD
    def jump(self):
        hits = pg.sprite.spritecollide(self, all_banners, False)
        if hits:
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
            
        

class Mob(Sprite): #class of mob
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((15,25))
        self.image = pg.image.load('Asteroid_Rock_PS1.png') # calls and displays image for asteroid
        self.color = color #fills color
        # self.image.fill(color) #chooses random color for each mob from defined colors at the top
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10 # speed of mobs
        self.speed2 = 1
      
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed2
        if self.rect.right > WIDTH or self.rect.x < 0: #makes it so that if borders of window are hit they rebound and go back
            self.speed *= -1.00 #this part creates it so that when it hits  in width section, it bounces off with # speed, the higher the number, the greater the bounce off speed is
        if self.rect.top > HEIGHT or self.rect.y < 0:
            self.speed2 *= -1.00 #this part creates it so that when it hits  in height section, it bounces off with # speed, the higher the number, the greater the bounce off speed is


# Text code for message from game that is displayed in terminal
for x in line_1:
    print(x, end='')
    sys.stdout.flush() # writes message out in a sentence
    sleep(0.1) # after each letter, it sleeps for .1 second and then goes onto the next one
for x in line_2:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)
for x in line_3:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1) # this block of code displays a message in the terminal


# init pygame and create a window
pg.init() # initiates the pygame window
# pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT)) # sets the screen
pg.display.set_caption("Run From Asteroids...") # sets name for the screen
clock = pg.time.Clock()

  
# create a group for all sprites
all_sprites = pg.sprite.Group()
all_banners = pg.sprite.Group()
mobs = pg.sprite.Group()


# instantiate classes
player = Player()
# player2 = Player2()
ban = Banner(100, 15, 600, 50)

#plat1 = Platform(75, 300, 100, 35)
# mob = Mob(25, 57, 25, 25)

# add instances to groups
all_sprites.add(ban)
all_banners.add(ban)
all_sprites.add(player)

for i in range(10): # number of mods that are spawned with the game when it opens
    # instantiate mob class repeatedly
    m = Mob(randint(0, WIDTH), randint(0,HEIGHT), 25, 25, (randint(0,255), randint(0,255) , randint(0,255)))
    all_sprites.add(m)
    mobs.add(m)
print(mobs)
# Game loop
running = True
wins = False
while running:
    # keep the loop running using clock
    dt = clock.tick(FPS)

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
    
    ############ Update ##############
    # update all sprites
    hits = pg.sprite.spritecollide(player, all_banners, False)
    mobhits = pg.sprite.spritecollide(player, mobs, True) 
    if mobhits:
        POINTS -= 20 # number of points removed per each mob hit
        print(POINTS)
        print(mobhits[0].color)
    if mobhits:
        m = Mob(randint(0,WIDTH), randint(0,HEIGHT), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
        all_sprites.add(m)
        mobs.add(m) # this part of the code add's another asteroid if one is hit, so the game remains the same level of difficulty        
    if POINTS >= 20:
        all_sprites.update() # this spot where all_sprites.update is above an else statement allows the code to stop everything if the players health reaches 0
    else:
        wins = True

        
    
        
 #all same code as above player rules and game rules

    ############ Draw ################
    # draw the background screen

    # screen.fill(BLACK)
    # screen.blit(background, background_rect)

    screen.fill(BLACK)
    screen.blit(background, background_rect)
    # drawing all sprites
    all_sprites.draw(screen)
    draw_text("Dodge All Asteroids and Make It Home Safe ", 22, BLUE2, 350, 15) #draws text, which is made possible by defining draw_text
    draw_text("Life:" + str(POINTS), 22, BLUE2, 350, 40) #draws text, which is made possible by defining draw_text
    
    if wins == True:
        if POINTS == 0:
            draw_text("You Died, Try Again.", 75, WHITE, WIDTH / 2, HEIGHT / 2) # this block of code makes it so that if life points = 0, then the text is drawn. This is made possible because of the if and when statement, when all_sprites.update() is above the else statement
            

    # buffer - after drawing everything, flip display
    pg.display.flip()


pg.quit()