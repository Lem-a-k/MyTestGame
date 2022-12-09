import os
import sys

import pygame

size = width, height = 1000, 600


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if color_key is not None:
        # image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)

    img1 = load_image("asteroid.png")
    img2 = load_image("bomb.png")

    all_sprites = pygame.sprite.Group()
    pers = pygame.sprite.Sprite(all_sprites)
    pers.image = img2
    pers.rect = pers.image.get_rect()
    pers.rect.x = 10
    pers.rect.y = 10
    pers.dx = 0
    pers.dy = 0

    clock = pygame.time.Clock()
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pers.rect.x = event.pos[0] - pers.rect.width // 2
                pers.rect.y = event.pos[1] - pers.rect.height // 2
            elif event.type == pygame.MOUSEMOTION:
                pass
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pers.dy -= 1
                elif event.key == pygame.K_DOWN:
                    pers.dy += 1
                elif event.key == pygame.K_LEFT:
                    pers.dx -= 1
                elif event.key == pygame.K_RIGHT:
                    pers.dx += 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    pers.dy += 1
                elif event.key == pygame.K_DOWN:
                    pers.dy -= 1
                elif event.key == pygame.K_LEFT:
                    pers.dx += 1
                elif event.key == pygame.K_RIGHT:
                    pers.dx -= 1
        print(pers.dx, pers.dy)
        screen.fill((50, 20, 75))
        pers.rect = pers.rect.move(pers.dx, pers.dy)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
