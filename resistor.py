'''
Resistor Class for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Makes resistor objects
'''
import pygame as pg
from component import Component

class Resistor(Component):
    """ Encodes the state of resistors """
    def __init__(self, r=100, x=0, y=0, angle=0, height=10, width=10):
        """ Intializes Resistor with value r
        and position (x,y) at angle """
        super().__init__()
        self.r = r
        self.x = x
        self.y = y
        self.angle = angle
        self.name = 'r'
        self.fieldValue = 'R*'

        self.image, self.rect = self.load_image('images/'+name+'.png')
        self.image = pg.transform.scale(self.image, (height,width))

    def draw(self):
        pass
