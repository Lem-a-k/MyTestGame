import random

import pygame

MAXW, MAXH = 1000, 800
size = width, height = None, None

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]


def draw(cur_screen):
    screen.fill((255, 255, 255))
    for i in range(n, 0, -1):
        pygame.draw.circle(cur_screen, colors[(i - 1) % 3], (width // 2, height // 2), i * w)


if __name__ == '__main__':

    w, n = map(int, input().split())
    size = width, height = 2 * w * n, 2 * w * n
    pygame.init()
    screen = pygame.display.set_mode(size)
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
