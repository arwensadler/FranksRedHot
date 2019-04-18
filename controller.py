'''
Controller Class for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Takes controller input
'''

import pygame
from pygame.locals import *

class Controller:
  def __init__(self):
      self.mouse_pos = (0, 0)

      self.model = None #will be updated in circuit.py
      self.view = None

      self.mouse_pressed = False
  def moving_component(image):
      """ Blits an image of the component where the mouse is while the
      component is being dragged """

      if mouse_pressed:
          self.view.screen.blit(image, pygame.mouse.get_pos())
  def handle_event(self, event):
      if pygame.mouse.get_pressed()[0]:
          print('got pressed')
          self.mouse_pressed = True

  def update(self):
      self.mouse_pos = pygame.mouse.get_pos()


  # def handle_event(self, event):
  #     if event.type == pygame.locals.MOUSEMOTION:
  #         self.model.resistor.x = event.pos[0]
  #     if event.type == pygame.locals.MOUSEBUTTONDOWN:
  #                       if event.button == 1:
  #                           self.model.relevantcomp.x = empty something
