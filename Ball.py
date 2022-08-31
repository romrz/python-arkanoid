import pygame

class Ball:
    def __init__(self, game, screen, position, size, color, speed):
        self.game = game
        self.screen = screen
        self.size = size
        self.color = color
        self.speed = pygame.math.Vector2(speed)
        self.rect = pygame.Rect(position, (size * 2, size * 2))

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.size)

    def update(self):
        self.rect.center = self.rect.center + self.speed

    def on_collision(self, entity):
        if entity.label == 'left wall':
            self.speed.x = -self.speed.x
        if entity.label == 'right wall':
            self.speed.x = -self.speed.x
        if entity.label == 'top wall':
            self.speed.y = -self.speed.y
        if entity.label == 'bottom wall':
            self.speed.y = -self.speed.y
        if entity.label == 'bar':
            self.speed.y = -self.speed.y
        if entity.label == 'block':
            self.speed.y = -self.speed.y
            self.game.remove_block(entity)

