'''
Resistor Class for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Makes resistor objects
'''
import pygame as pg
from component import Component

class Resistor(Component): #inherit from component
    """ Encodes the state of resistors """
    def __init__(self, r=100, x=0, y=0, angle=0, height=100, width=20):
        """ Intializes Resistor with value r
        and position (x,y) at angle """
        super().__init__()
        self.r = r
        self.x = x
        self.y = y
        self.angle = angle
        self.name = 'resistor'
        self.type = 'r'
        self.fieldValue = 'R*'

        self.image = pg.image.load('images/resistor.png')
        self.image = pg.transform.scale(self.image, (height,width))

        self.rect = self.image.get_rect(center=(x,y))
    def __str__(self):
        return str(self.r) + " ohm " + self.name
