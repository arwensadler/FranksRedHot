'''
Model file for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Create and update components
'''
from resistor import Resistor

class CircuitModel:
    def __init__(self, size):
        self.width = size[0]
        self.height = size[1]
        #have dictionary of components
    def update(self):
        """ Update the software state """
        #update components
    def __str__(self):
        pass
