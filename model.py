'''
Model file for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Create and update components
'''
from resistor import Resistor
import pygame as pg

class CircuitModel:
    """ Stores the components """
    def __init__(self):
        self.components = pg.sprite.Group()

        self.add = False #instead of boolean, store what component got clicked?
        # TO DO: Make so that it picks which image to load based on which
        # component was clicked
        self.add_image = pg.image.load('./images/resistor.png')

        # Adds the sideboard components to click on
        self.components.add(Resistor(100, 75, 60))

        self.view = None
        self.controller = None


        self.being_dragged = True
        #self.width = size[0]
        #self.height = size[1]
        #have dictionary of components
    def update(self):
        """ Update the software state """
        pass
        #update components, position of components

    def __str__(self):
        return self.r.__str__()
