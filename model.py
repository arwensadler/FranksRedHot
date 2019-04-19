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

        # Adds the sideboard components to click on
        self.r = Resistor(100, 75, 60)
        self.components.add(self.r)

        # TO DO: Make so that it picks which image to load based on which
        # component was clicked
        self.comp_type = self.r #component that is clicked

        self.view = None
        self.controller = None

        #self.width = size[0]
        #self.height = size[1]
        #have dictionary of components
    def update(self):
        """ Update the software state """
        pass
        #update components, position of components

    def __str__(self):
        return self.r.__str__()
