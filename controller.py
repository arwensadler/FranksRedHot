'''
Controller Class for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Takes controller input
'''

import pygame
from pygame.locals import *

class Controller:
    """ Handles mouse input from the user """
    def __init__(self):
        self.mouse_pos = (0, 0)

        self.model = None #will be updated in circuit.py
        self.view = None

        self.mouse_pressed = False
    def handle_event(self, event):
        """ Senses if mouse is pressed and updates mouse pressed """
        if pygame.mouse.get_pressed()[0]:
            self.mouse_pressed = True

            x,y = event.pos
            print(x,y)
            for component in self.model.components:
                if component.rect.collidepoint(x,y): #get type of component clicked
                    print(component.type)
                    self.model.comp_type = component.type #set type in model to that type

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
