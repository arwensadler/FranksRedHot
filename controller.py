import pygame.locals

class Controller:
  def __init__(self, model):
      self.model = model
  def handle_event(self, event):
        #if event.type == pygame.locals.MOUSEMOTION:
        #    self.model.paddle.x = event.pos[0] - self.model.paddle.width/2.0
        #from example code for later use
