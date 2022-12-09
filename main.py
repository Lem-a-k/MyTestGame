import os
import sys
import random

import pygame

size = width, height = 1000, 600
pygame.init()
screen = pygame.display.set_mode(size)


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


class Bomb(pygame.sprite.Sprite):
    img1 = load_image("bomb.png")
    img2 = load_image("boom.png")

    def __init__(self, pos, *group):
        super().__init__(*group)
        self.image = Bomb.img1
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0] - self.rect.width // 2, pos[1] - self.rect.height // 2

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

    img1 = load_image("asteroid.png")

    all_sprites = pygame.sprite.Group()

    clock = pygame.time.Clock()
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    Bomb(event.pos, all_sprites)
                else:
                    all_sprites.update(event)
            elif event.type == pygame.MOUSEMOTION:
                pass
            elif event.type == pygame.KEYDOWN:
                pass
            elif event.type == pygame.KEYUP:
                pass

        screen.fill((50, 20, 75))

        all_sprites.draw(screen)
        pygame.display.flip()
        all_sprites.update()
        clock.tick(fps)
    pygame.quit()
