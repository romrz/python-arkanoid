import pygame

class Wall:
    def __init__(self, x, y, width, height, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label

