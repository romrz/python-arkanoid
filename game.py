import sys
import pygame
import random
from Bar import Bar
from Wall import Wall
from Ball import Ball
from Block import Block

class Game:
    def __init__(self):
        pygame.init()

        self.FPS = 60
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.bg_color = (8, 8, 71)
        self.clock = pygame.time.Clock()
        self.delta_time = self.clock.tick(self.FPS)

        self.balls = [
            Ball(self, self.screen, (400, 450), 7, ((255, 255, 255)), (-5, -5)),
            Ball(self, self.screen, (400, 450), 7, ((0, 0, 255)), (-2, -2)),
        ]

        self.walls = [
            Wall(-20, 0, 20, self.screen_size[1], 'left wall'),
            Wall(0, -20, self.screen_size[0], 20, 'top wall'),
            Wall(self.screen_size[0], 0, 20, self.screen_size[1], 'right wall'),
            Wall(0, self.screen_size[1], self.screen_size[0], 20, 'bottom wall'),
        ]

        self.create_blocks()

        self.bar = Bar(self.screen)

        pygame.display.set_caption('Arkanoid')

    def create_blocks(self):
        self.blocks = []

        block_width = 60
        block_height = 30
        y = 0
        
        for y in range (0, 200, block_height):
            for x in range(0, 800, block_width):
                color = tuple(random.choices(range(256), k = 3))
                self.blocks.append(
                    Block(self.screen, x, y, block_width, block_height, color, 'block')
                )


    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.check_collisions()
            self.render()
            self.delta_time = self.clock.tick(self.FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.bar.direction = 1
                elif event.key == pygame.K_LEFT:
                    self.bar.direction = -1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.bar.direction = 0
                if event.key == pygame.K_LEFT:
                    self.bar.direction = 0

    def update(self):
        for ball in self.balls:
            ball.update()

        for block in self.blocks:
            block.update()

        self.bar.update()

    def check_collisions(self):
        for  ball in self.balls:
            for wall in self.walls:
                if ball.rect.colliderect(wall.rect):
                    ball.on_collision(wall)

            for block in self.blocks:
                if ball.rect.colliderect(block.rect):
                    ball.on_collision(block)

            if ball.rect.colliderect(self.bar.rect):
                ball.on_collision(self.bar)
        
        for wall in self.walls:
            if self.bar.rect.colliderect(wall.rect):
                self.bar.on_collision(wall)

    def render(self):
        self.screen.fill(self.bg_color)

        for ball in self.balls:
            ball.draw()

        for block in self.blocks:
            block.draw()

        self.bar.draw()

        pygame.display.flip()

    def remove_block(self, block):
        self.blocks.remove(block)


if __name__ == '__main__':
    game = Game()
    game.run()