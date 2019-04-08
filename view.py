'''
View for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Main Window for Pick-and-Place
'''

import pygame


background_color = (255,255,255)
(width, height) = (1420, 1080)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Test Window')
screen.fill(background_color)


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
