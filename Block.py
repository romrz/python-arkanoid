import pygame

class Block:
    def __init__(self, screen, x, y, width, height, color, label):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.label = label

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        pass
