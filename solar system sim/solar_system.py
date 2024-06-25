#libraries
import pygame as pg 
import math
from random import randint

# Initialize Pygame
pg.init()

# Creat a window
screen_info= pg.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h
WINDOW = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('Solar System Simulation')


#Colours
BLACK=(0,0,0)
YELLOW=(225,225,0)
GRAY = (128,128,128)
YELLOWISH_WHITE=(225,225,246)
BLUE= (0,0,225)
RED= (188,39,50)
# class solar system bodies
class SolarSystemBodies :
    
    AU = 1.496e11
    SCALE = 280/AU
    
    #constructor
    def __init__(self, name, color, x, y, mass, radius):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        
    #method 01- Draw the bodies on the simulator 
    def draw_body(self, WINDOW):
        x = self.x*SolarSystemBodies.SCALE + WIDTH//2 
        y = self.y*SolarSystemBodies.SCALE + HEIGHT//2
        pg.draw.circle(surface=WINDOW, color= self.color, center= (x,y), radius=self.radius)
           
    

# Star list with colour, center and radius information 
stars_list = [
    {
        'color' : (randint(190,255),randint(190,255),randint(190,255)),
        'center' : (randint(5,WIDTH-5),randint(5,HEIGHT-5)),
        'radius' : (randint(1,2))
    }
    for star in range (450)
]

print(stars_list)
#Function to draw stars on the pygame window 
def draw_stars(stars_list):
    for stars in stars_list:
        pg.draw.circle(WINDOW, stars['color'],stars['center'], stars['radius'])

#Create Simulation 
run = True

sun = SolarSystemBodies("SUN", YELLOW, 0,0, 1.9891e30, 30)
mercury = SolarSystemBodies("MERCURY", GRAY,0.39*SolarSystemBodies.AU, 0, 0.33e24, 6)
venus= SolarSystemBodies("VENUS",YELLOWISH_WHITE, 0.72*SolarSystemBodies.AU,0, 4.87e24,14)
earth= SolarSystemBodies("EARTH",BLUE, 1*SolarSystemBodies.AU,0, 5.97e24,15)
mars= SolarSystemBodies("MARS",RED, 1.52*SolarSystemBodies.AU,0, 0.642e24,8)
while run:
    
    WINDOW.fill(BLACK)
    draw_stars(stars_list)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            run = False        
    ss_bodies= [sun,mercury,venus,earth,mars]
    for body in ss_bodies:
        body.draw_body(WINDOW)        
    pg.display.update()          
#Quit the pygame
pg.quit()            