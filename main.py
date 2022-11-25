import random

import pygame

MAXW, MAXH = 1000, 800
size = width, height = None, None


def draw(cur_screen):
    screen.fill((255, 255, 255))
    side = a // n
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print(i, j)
                screen.fill((0, 0, 0), (i * side, (height - side - j * side), side, side))


if __name__ == '__main__':

    a, n = map(int, input().split())
    size = wight, height = a, a
    pygame.init()
    screen = pygame.display.set_mode(size)
    draw(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
