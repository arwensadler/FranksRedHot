'''
Controller Class for Frank's Red Hot SPICE Software
Author(s): @awenstrup, @aditya-sudhakar, @MellieZito, @arwensadler

Function: Takes controller input
'''

import pygame as pg

class Controller:
  def __init__(self):
      self.mouse_pos = (0, 0)

      self.model = None #will be updated in circuit.py
      self.view = None

  def moving_component(image):
      """ Blits an image of the component where the mouse is while the
      component is being dragged """
      mouse_pressed = False
      while (not mouse_pressed):
          self.view.screen.blit(image, pg.mouse.get_pos())
          if pg.mouse.get_pressed():
              mouse_pressed = True

  def update(self):
      self.mouse_pos = pg.mouse.get_pos()


  # def handle_event(self, event):
  #     if event.type == pygame.locals.MOUSEMOTION:
  #         self.model.resistor.x = event.pos[0]
  #     if event.type == pygame.locals.MOUSEBUTTONDOWN:
  #                       if event.button == 1:
  #                           self.model.relevantcomp.x = empty something
