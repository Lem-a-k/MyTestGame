import random

import pygame

MAXW, MAXH = 1000, 800
size = width, height = None, None

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]


class Ball:

    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.r = 0
        self.color = pygame.Color('yellow')

    def grow(self):
        self.r += 1

    def draw(self, cur_screen):
        pygame.draw.circle(cur_screen, self.color,
                           (self.x_pos, self.y_pos), self.r)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    x_pos = 0
    fps = 60  # количество кадров в секунду
    running = True
    ball = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                ball = Ball(event.pos[0], event.pos[1])

        screen.fill((10, 10, 60))
        if ball is not None:
            ball.draw(screen)
        pygame.display.flip()
        if ball is not None:
            ball.grow()

        clock.tick(fps)
    pygame.quit()
