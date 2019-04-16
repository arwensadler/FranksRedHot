'''
Main file for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Run the program
'''
import time
import pygame
from model import CircuitModel
from view import PyGameWindowView
from controller import Controller


def start_software(size):
    """
    Creates all the classes and tells the classes how to communicate with
    each other
    Given screen 'size' as (x,y) tuple and gives it to view
    """
    pygame.init()

    #initializes model, view, controller
    model = CircuitModel()
    view = PyGameWindowView(size)
    controller = Controller()

    #gives model, view, controller references to the other ones
    model.view = view
    model.controller = controller

    view.model = model
    view.controller = controller

    controller.model = model
    controller.view = view

    #runs software
    running = True

    if running: print("begin while")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        print('running')
        model.update()
        print('model updated')
        view.draw()
        print('view drawn')
        controller.update()
        print('controller updated')
        #time.sleep(.001)


    pygame.quit()

if __name__ == '__main__':
    size = (1440, 1080)
    start_software(size)
