'''
Main file for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Run the program
'''
import time
import pygame
from model import CircuitModel
from view import PyGameWindowView
from controller.mouse_controller import Controller


def start_software(size):
    """
    Given screen 'size' as (x,y) tuple, start BrickBreaker game
    """
    pygame.init()

    model = CircuitModel(size)
    print(model)
    view = PyGameWindowView(model, size)
    controller = Controller(model)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False
            controller.handle_event(event)
        model.update()
        view.draw()
        time.sleep(.001)

    pygame.quit()

if __name__ == '__main__':
    size = (1420, 1080)
    start_software(size)
