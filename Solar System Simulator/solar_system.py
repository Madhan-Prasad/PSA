# Libraries
import pygame as pg
import math 
from random import randint 

# Initialize Pygame
pg.init()

# Creat window
screen_info= pg.display.Info()
WIDTH= screen_info.current_w
HEIGHT = screen_info.current_h
WINDOW = pg.display.set_mode((WIDTH-150,HEIGHT-150))


# Create simulation 
run=True
while run:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
         run = False    
         
pg.quit()         
         