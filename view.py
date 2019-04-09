'''
View for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Main Window for Pick-and-Place
'''

import pygame

class PyGameWindowView:
    def __init__(self, model, size):
        self.model = model
        self.screen = pygame.display.set_mode(size)
    def draw(self):
        self.screen.fill(pygame.Color(255,255,255))
        pygame.display.set_caption('Test Window')
        #will draw components when we add those
