import pygame

class Bar:
    def __init__(self,  screen):
        self.screen = screen
        self.rect = pygame.Rect(300, 550, 100, 10)
        self.color = (200, 200, 200)
        self.direction = 0
        self.speed = 10
        self.label = 'bar'

    def update(self):
        self.rect.x = self.rect.x + self.direction * self.speed
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    def on_collision(self, entity):
        if entity.label == 'left wall':
            self.rect.x = 0
        if entity.label == 'right wall':
            self.rect.right = 800

