# content from kids can code: http://kidscancode.org/blog/
# guides from w3schools python tutorial
# import libraries and modules
# tkinter loader screen https://www.pythontutorial.net/tkinter/tkinter-progressbar/
# arrow keys for movement https://www.codespeedy.com/movement-of-object-when-arrow-keys-are-pressed-in-pygame/
# figured out background image from copying from https://bcpsj-my.sharepoint.com/personal/ccozort_bcp_org/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode%2Fper1game%2Fmain%5Fside%2Epy&parent=%2Fpersonal%2Fccozort%5Fbcp%5Forg%2FDocuments%2FDocuments%2F000%5FIntro%20to%20Programming%2F2022%5FFall%2FCode%2Fper1game
# text code for welcome message in game https://stackoverflow.com/questions/52856030/how-to-fade-in-and-out-a-text-in-pygame

# GOALS
# Create another class with Player 2
# increase playing ground with game settings
# add code where when each player hits a mob, another one spawns
# add competition goal, first to hit #points wins
# add ID to player, "P1" and "P2" to respective player

# Final Project
# add a starting screen
# add a sounds for each player, so that you can differentiate who hits a mob

from platform import platform
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from os import path
from tkinter import *
from tkinter.ttk import *
from tkinter import * 
from tkinter.messagebox import showinfo
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import time
from time import sleep
import sys
import pygame as pg1


vec = pg.math.Vector2

Computer_Science = os.path.dirname(__file__)
Final_Project_Images = os.path.join(Computer_Science, 'Final_Project_Images')

# # Setup asset folders here - images sounds etc.
# Computer_Science = os.path.dirname(__file__)
# Images = os.path.join(Computer_Science, 'images')

# game settings 
WIDTH = 700
HEIGHT = 400
FPS = 30

# player settings
PLAYER_FRIC = -0.1
PLAYER_GRAV = .9875
POINTS = 0 
TIME = 10

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
SAND = (139, 131, 120)

# start moving text
line_1 = "You've been abandoned by your country..."
line_2 = "Your current mission is to survive and make it back home..."
line_3 = "Good luck soldier. God Speed."

# images
background = pg.image.load(path.join(Final_Project_Images, 'Space_Background.png'))
background_rect = background.get_rect()
FighterJet = pg.image.load(path.join(Final_Project_Images, 'fighter_jet_not.png'))
FighterJet_rect = background.get_rect()
FighterJet.set_colorkey(SAND)
FighterJet = pg.transform.scale(FighterJet, (10,10))

# theBell = pg.image.load(path.join(img_folder, 'theBell.png'))
# theBell_rect = background.get_rect()
# theBell.set_colorkey(BLACK)
# theBell = pg.transform.scale(theBell, (200,200))

# self.image.set_colorkey(BLACK)

# fighter_Jet = pg.image.load(path.join(Final_Project_Images, 'Fighter_Jet.png'))
# fighter_Jet_rect = background.get_rect()
# fighter_Jet.set_colorkey(SAND)
# fighter_Jet = pg.transform.scale(fighter_Jet, (200,200))

# self.image.set_colorkey(SAND)

'''
# game_folder = os.path.dirname(__file__)
# img_folder = os.path.join(game_folder, 'images')
Computer_Science = os.path.dirname(__file__)
Final_Project_Images = os.path.join(Computer_Science, 'Final_Project_Images')

# img_folder = os.path.join(game_folder, 'images')
Final_Project_Images = os.path.join(Computer_Science, 'Final_Project_Images')

# background = pg.image.load(path.join(img_folder, 'starfield.png'))
# background_rect = background.get_rect()
background = pg.image.load(path.join(Final_Project_Images, 'Zombie_Apoc_Background.png'))
background_rect = background.get_rect()
'''

'''
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar: Press')


def update_progress_label():
    return f"Current Progress: {pb['value']}%"


def progress():
    if pb['value'] < 100:
        pb['value'] += 25
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')
    if pb['value'] == 100:
        root.quit() # if the progress bar reaches 100% then the window closes


def stop():
    pb.stop()
    value_label['text'] = update_progress_label()


# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)
# coordinates to place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# label
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

# shows start button and gives command to progress, moves
start_button = ttk.Button(
    root,
    text='Progress',
    command=progress
)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

stop_button = ttk.Button(
    root,
    text='Stop',
    command=stop
)
stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)


root.mainloop()
'''
# if 'value' == '100%':
#     root.quit()



def start_text():
    clock1 = pg.time.Clock()
    clock2 = pg.time.Clock()
    clock3 = pg.time.Clock()
    screen = pg.display.set_mode((1350, 480))
    font = pg.font.Font(None, 64)
    blue = pg.Color('red')
    orig_surf = font.render("You've been abandoned by your country.", True, blue)
    txt_surf = orig_surf.copy()
    orig_surf1 = font.render("Your current mission is to survive and make it back home.", True, blue)
    txt_surf1 = orig_surf1.copy()
    orig_surf2 = font.render("Good luck soldier. God Speed.", True, blue)
    txt_surf2 = orig_surf2.copy()

    # This surface is used to adjust the alpha of the txt_surf.
    alpha_surf = pg1.Surface(txt_surf.get_size(), pg1.SRCALPHA)
    alpha = 255  # The current alpha value of the surface.


    while True:
        for event in pg1.event.get():
            if event.type == pg1.QUIT:
                return

        if alpha > 0:
            # Reduce alpha each frame, but make sure it doesn't get below 0.
            alpha = max(alpha-4, 0)
            txt_surf = orig_surf.copy()  # Don't modify the original text surf.
            txt_surf1 = orig_surf1.copy()
            txt_surf2 = orig_surf2.copy()
            # Fill alpha_surf with this color to set its alpha value.
            alpha_surf.fill((255, 255, 255, alpha))
            # To make the text surface transparent, blit the transparent
            # alpha_surf onto it with the BLEND_RGBA_MULT flag.
            txt_surf.blit(alpha_surf, (0, 0), special_flags=pg1.BLEND_RGBA_MULT)

        screen.fill((30, 30, 30))
        screen.blit(txt_surf, (30, 60))
        pg1.display.flip()
        clock1.tick(100)
        
        screen.fill((30, 30, 30))
        screen.blit(txt_surf1, (30, 120))
        pg1.display.flip()
        clock2.tick(15)
        
        screen.fill((30, 30, 30))
        screen.blit(txt_surf2, (30, 180))
        pg1.display.flip()
        clock3.tick(15)

    
if __name__ == '__main__':
    pg1.init()
    start_text()
    pg1.quit()


time.sleep(.4) #stops going through the code for .2 second. Gives second window time to load up

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
        self.image = pg.Surface((20, 20))
        # self.image.set_colorkey(SAND)
        # self.image.fill(GREEN) #color of player
        # self.image.fill("ID1")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
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
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        if hits:
            # print("i've collided...")
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
        self2.image = pg.Surface((20, 20))
        self2.image.fill(BLUE2)# color of player2
        self2.rect = self2.image.get_rect()
        self2.rect.center = (WIDTH/2, HEIGHT/2) #
        self2.pos = vec(WIDTH/2, HEIGHT/4) # where player2 starts
        self2.vel = vec(0,0)
        self2.acc = vec(0,0)
    def controls(self2):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self2.acc.x = -3
        if keys[pg.K_RIGHT]:
            self2.acc.x = 3
        if keys[pg.K_UP]:
            self2.acc.y = -3
        if keys[pg.K_DOWN]:
            self2.acc.y = 3
    def jump(self2):
        hits = pg.sprite.spritecollide(self2, all_platforms, False)
        if hits:
            # print("i've collided...")
            self2.vel.y = -40
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
        self.image = pg.Surface((15,25))
        self.color = color #fills color
        self.image.fill(color) #chooses random color for each mob from defined colors at the top
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

'''
# Text code for message from game
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)
for x in line_2:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)
for x in line_3:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)
'''

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Space Survival...")
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
    hits = pg.sprite.spritecollide(player, all_platforms, False)
    # if hits:
    #     print("i've collided...with a plat")
    mobhits = pg.sprite.spritecollide(player, mobs, True) 
    if mobhits:
        POINTS += 20 # number of points added per each mob hit
        print(POINTS)
        # print("i've collided...with a mob")
        print(mobhits[0].color)

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
        # print("ive struck a mob")
        m = Mob(randint(0,WIDTH), randint(0,HEIGHT), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
        all_sprites.add(m)
        mobs.add(m)      # every time a player hits a mob, a new one spawns
    # if POINTS == GOAL:
    #     break #if GOAL # is met, game ends and player wins
        
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
        # print("i've collided...with a mob")
        print(mobhits[0].color)
    
    # if mobhits:
    if mobhits:
        m = Mob(randint(0,WIDTH), randint(0,HEIGHT), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
        all_sprites.add(m)
        mobs.add(m)
    if POINTS2 <= GOAL and POINTS <= GOAL:
        all_sprites.update()
    else:
        wins = True

        
    
        
 #all same code as above player rules and game rules

    ############ Draw ################
    # draw the background screen

    # screen.fill(BLACK)
    # screen.blit(background, background_rect)

    screen.fill(BLACK)
    screen.blit(background, background_rect)
    # draw all sprites
    all_sprites.draw(screen)
    draw_text("POINTS p1: " + str(POINTS), 22, GREEN, WIDTH / 2, HEIGHT / 15) #draws text, which is made possible by defining draw_text
    draw_text("POINTS P2: " + str(POINTS2), 22, BLUE2, WIDTH / 2, HEIGHT / 10)
    # draw_text("GOAL OF GAME: " + str(GOAL), 22, RED, WIDTH / 2, HEIGHT / 50)
    # draw_text("WASD: " + str(CONTROLS), 22, GREEN, WIDTH / 8, HEIGHT / 50)
    # draw_text("IJKL: " + str(CONTROLS2), 22, BLUE2, WIDTH / 8, HEIGHT / 10)
    # draw_text("hello:"+str(CONTROLS), 22, BLUE2, WIDTH / 8, HEIGHT / 10)



    # draw_text("HEALTH: " + str(HEALTH), 15, WHITE, WIDTH / 2, HEIGHT / 10)

    
    if wins == True:
        if POINTS2 >= GOAL:
            draw_text("P2 WINS", 144, WHITE, WIDTH / 2, HEIGHT / 2)
        if POINTS >= GOAL:
            draw_text("P1 WINS", 144, WHITE, WIDTH / 2, HEIGHT / 2)
    

    # draw_text("FPS: " + str(dt), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    # draw_text("asdfasdfasdfasdfasdf: " + str(dt), 22, WHITE, WIDTH / 2, HEIGHT / 24)

    # buffer - after drawing everything, flip display
    pg.display.flip()


pg.quit()