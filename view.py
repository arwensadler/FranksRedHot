'''
View for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Main Window for Pick-and-Place
'''

import pygame as pg
from resistor import Resistor

class PyGameWindowView:
    """ Creates the window/grid for placing components """
    def __init__(self, size):
        self.screen = pg.display.set_mode(size)
        self.grid_image = pg.image.load("./images/grid.png")
        self.grid_image = pg.transform.scale(self.grid_image, (1440, 1080))

        self.controller = None #will be updated in circuit.py
        self.model = None
    def draw(self):
        """ Draws background and components on screen """
        self.screen.fill(pg.Color(255, 255, 255))
        pg.display.set_caption('Test Window')
        self.screen.blit(self.grid_image, (0, 0))
        self.model.components.draw(self.screen)
        #HARD-CODED, FIX LATER: mouse_pressed should depend on whether the mouse
        #has been clicked over a component
        if self.controller.mouse_pressed == False:
            mouse_pos = self.controller.mouse_pos #get mouse position from controller
            self.screen.blit(self.model.add_image, mouse_pos) #get image of component from model
        else:
            mouse_pos = self.controller.mouse_pos
            self.model.components.add(Resistor(100, mouse_pos[0], mouse_pos[1]))
            self.controller.mouse_pressed = False

        if self.model.add: #should be more about blitting image to screen once clicked
            self.screen.blit(self.model.add_image, self.model.add_pos)
        pg.display.flip()
