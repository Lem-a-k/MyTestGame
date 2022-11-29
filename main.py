import random

import pygame

MAXW, MAXH = 1000, 800
size = width, height = None, None

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]


class Ball:
    R = 20

    def __init__(self, x, y, dx, dy):
        self.x_pos = x
        self.y_pos = y
        self.dx = dx
        self.dy = dy
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))

    def move(self):
        if self.x_pos + self.dx + Ball.R > width or self.x_pos + self.dx - Ball.R < 0:
            self.dx *= -1
        if self.y_pos + self.dy + Ball.R > height or self.y_pos + self.dy - Ball.R < 0:
            self.dy *= -1
        self.x_pos = self.x_pos + self.dx
        self.y_pos = self.y_pos + self.dy

    def draw(self, cur_screen):
        pygame.draw.circle(cur_screen, self.color,
                           (self.x_pos, self.y_pos), Ball.R)


if __name__ == '__main__':
    # что поменять:
    # 1) шарик добавляется только по щелчку левой кнопки мыши
    # 2) направление полёта на старте
    # 3) цвет
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    x_pos = 0
    fps = 60  # количество кадров в секунду
    running = True
    balls = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                balls.append(Ball(event.pos[0], event.pos[1],
                                  random.randint(-4, 4), random.randint(-4, 4)))

        screen.fill((10, 10, 60))
        for b in balls:
            b.draw(screen)
        pygame.display.flip()
        for b in balls:
            b.move()

        clock.tick(fps)
    pygame.quit()
