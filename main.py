import random

import pygame

MAXW, MAXH = 1000, 800
size = width, height = None, None

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]


def get_random_color():
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    MY_EVENT_TYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MY_EVENT_TYPE, 10 * 100)

    fps = 60  # количество кадров в секунду
    running = True
    ball = None
    screen.fill((10, 10, 60))
    painting = False
    # prev_pos = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                painting = True
            elif event.type == pygame.MOUSEBUTTONUP:
                painting = False
            elif event.type == pygame.MOUSEMOTION:
                if painting:
                    pygame.draw.circle(screen, pygame.Color('purple'),
                                       (event.pos[0], event.pos[1]), 10)
                    # if prev_pos is not None:
                    pygame.draw.line(screen, pygame.Color('purple'), (event.pos[0], event.pos[1]),
                                     (event.pos[0] - event.rel[0], event.pos[1] - event.rel[1]), 10 * 2)
                # prev_pos = event.pos
            elif event.type == MY_EVENT_TYPE:
                pygame.draw.ellipse(screen, get_random_color(), (random.randint(0, width),
                                                                 random.randint(0, height),
                                                                 random.randint(5, 10),
                                                                 random.randint(5, 10)))
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
