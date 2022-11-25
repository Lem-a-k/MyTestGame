import random

import pygame

size = width, height = 800, 600

def draw(cur_screen):
    cur_screen.fill((10, 10, 30))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!", True, (50, 155, 50))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()

    for i in range(10000):
        cur_screen.fill(pygame.Color('white'),
                        (random.random() * width,
                         random.random() * height, 1, 1))
    cur_screen.blit(text, (text_x, text_y))
    pygame.draw.rect(cur_screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 2)
    pygame.draw.line(cur_screen, pygame.Color('orange'),
                     (0, 0), size, width=5)
    pygame.draw.line(cur_screen, pygame.Color('orange'),
                     (width, 0), (0, height), width=5)


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(size)

    while pygame.event.wait().type != pygame.QUIT:
        draw(screen)
        pygame.display.flip()
    pygame.quit()
