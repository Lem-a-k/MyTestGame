import os
import sys
import random

import pygame

from intersect import intersect_rect, intersect_circle

size = width, height = 1000, 500
pygame.init()
screen = pygame.display.set_mode(size)

BORDER = 5


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


class Creature(pygame.sprite.Sprite):
    img_main = load_image("creature.png", -1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Creature.img_main
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.rect.width // 2
        self.rect.y = height // 2 - self.rect.height // 2
        self.speed = 2
        self.dx = self.dy = 0

    def update(self, *args):
        if args:
            cur_event = args[0]
            if cur_event.type == pygame.KEYDOWN:
                if cur_event.key == pygame.K_UP:
                    self.dy -= self.speed
                elif cur_event.key == pygame.K_DOWN:
                    self.dy += self.speed
                elif cur_event.key == pygame.K_LEFT:
                    self.dx -= self.speed
                elif cur_event.key == pygame.K_RIGHT:
                    self.dx += self.speed
            elif cur_event.type == pygame.KEYUP:
                if cur_event.key == pygame.K_UP:
                    self.dy += self.speed
                elif cur_event.key == pygame.K_DOWN:
                    self.dy -= self.speed
                elif cur_event.key == pygame.K_LEFT:
                    self.dx += self.speed
                elif cur_event.key == pygame.K_RIGHT:
                    self.dx -= self.speed
        else:
            self.rect.x += self.dx
            self.rect.y += self.dy


class Bomb(pygame.sprite.Sprite):
    img1 = load_image("bomb.png")
    img2 = load_image("boom.png")

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = Bomb.img1
        self.rect = self.image.get_rect()
        x = random.randint(BORDER, width - BORDER - self.rect.width)
        y = random.randint(BORDER, height - BORDER - self.rect.height)
        self.rect.x = x
        self.rect.y = y
        # self.rect.x, self.rect.y = pos[0] - self.rect.width // 2, pos[1] - self.rect.height // 2

    def update(self, *args):
        if args:
            if args[0].type == pygame.MOUSEBUTTONUP and args[0].button != 1:
                if self.image == Bomb.img1 and self.rect.collidepoint(args[0].pos):
                    self.image = Bomb.img2
                    self.rect.width = self.image.get_rect().width
                    self.rect.height = self.image.get_rect().height
                    self.rect.x -= self.rect.width // 4
                    self.rect.y -= self.rect.height // 4
        else:
            self.rect = self.rect.move(random.randrange(3) - 1,
                                       random.randrange(3) - 1)


if __name__ == '__main__':

    all_sprites = pygame.sprite.Group()
    all_bombs = pygame.sprite.Group()
    main_character = pygame.sprite.GroupSingle()

    pers = Creature(all_sprites, main_character)
    clock = pygame.time.Clock()
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    Bomb(event.pos, all_sprites, all_bombs)
                else:
                    all_sprites.update(event)
            elif event.type == pygame.MOUSEMOTION:
                pass
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                all_sprites.update(event)

        screen.fill((50, 20, 75))

        all_bombs.draw(screen)
        main_character.draw(screen)

        pygame.display.flip()
        all_sprites.update()
        clock.tick(fps)
    pygame.quit()
