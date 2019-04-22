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
        self.r = Resistor(100, 20, 200)
        self.components.add(self.r)

        # TO DO: Make so that it picks which image to load based on which
        # component was clicked
        self.comp_type = None #component that is clicked

        self.view = None
        self.controller = None

        #self.width = size[0]
        #self.height = size[1]
        #have dictionary of components
    def add_comp(self, comp, x, y):
        """ Adds a component to the sprite group of a given type and position"""
        if comp == 'r':
            self.components.add(Resistor(100, x, y)) #if type 'r', make a resistor
        else:
            print('Not an existing component')
    def update(self):
        """ Update the software state """
        #update components, position of components

    def __str__(self):
        """ Prints components to help in debugging """
        output_lines = []
        for component in self.components.sprites():
            output_lines.append(str(component))
        return "\n".join(output_lines) #prints one component per line
