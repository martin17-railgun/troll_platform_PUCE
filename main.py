import pygame

from src.init import Game_controller

pygame.init()
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Simple Pygame Window")
game_controller = Game_controller()

while game_controller.running:
  game_controller.start()
  pygame.display.flip()
  clock.tick(60)

import pygame
import sys

# Inicialización
pygame.init()

# Pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Movimiento Troll Total")

# Reloj
clock = pygame.time.Clock()

# Clase Ball (Personaje)
class Ball:
    def __init__(self, radius=20, color="red"):
        self.radius = radius
        self.color = color
        self.position = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.velocity = pygame.Vector2(0, 0)
        self.gravity = 0.5
        self.jump_strength = -10
        self.on_ground = True

    def update(self):
        # Movimiento vertical
        self.velocity.y += self.gravity
        self.position.y += self.velocity.y

        # Límite inferior (suelo)
        if self.position.y + self.radius > SCREEN_HEIGHT:
            self.position.y = SCREEN_HEIGHT - self.radius
            self.velocity.y = 0
            self.on_ground = True

    def draw(self):
        pygame.draw.circle(
            SCREEN,
            pygame.Color(self.color),
            (int(self.position.x), int(self.position.y)),
            self.radius
        )

    def troll_movement(self, keys):
        # Izquierda va a la derecha, derecha va a la izquierda
        if keys[pygame.K_LEFT]:
            self.position.x += 5
        if keys[pygame.K_RIGHT]:
            self.position.x -= 5

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_strength
            self.on_ground = False

# Crear personaje
ball = Ball()

# Loop principal
running = True
while running:
    clock.tick(60)
    SCREEN.fill((0, 0, 0))  # Fondo negro

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Con cualquier tecla, salta
        if event.type == pygame.KEYDOWN:
            ball.jump()

    keys = pygame.key.get_pressed()
    ball.troll_movement(keys)
    ball.update()
    ball.draw()

    pygame.display.flip()

pygame.quit()
sys.exit()

