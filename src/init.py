import pygame

from src.character.player.player import Player
from src.const.game import SCREEN

class Game_controller:
  running = True
  player = Player("Player")
  sprites = pygame.sprite.Group()


  def __init__(self):
    self._game = None
    self.sprites.add(self.player)

  def start(self):
    SCREEN.fill((0, 0, 0))
    self.get_events(pygame.event)
    # self.player.draw()
    self.sprites.draw(SCREEN)
    self.sprites.update()

    print(f"Player position: ({self.player.x}, {self.player.y})")

  def get_events(self, event):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
