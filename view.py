'''
View for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Main Window for Pick-and-Place
'''

import pygame as pg
from model import CircuitModel as model

class PyGameWindowView:
    def __init__(self, model, size):
        self.model = model
        self.screen = pg.display.set_mode(size)
        self.grid_image = pg.image.load("./images/grid.png")
        self.grid_image = pg.transform.scale(self.grid_image, (1420, 1080))
    def draw(self):
        self.screen.fill(pg.Color(255,255,255))
        pg.display.set_caption('Test Window')
        screen = self.screen
        screen.blit(self.grid_image, (0,0))
        self.model.components.draw(self.screen)
        pg.display.flip()
