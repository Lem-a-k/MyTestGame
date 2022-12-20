import os
import sys
import random

import pygame

size = width, height = 1000, 500
pygame.init()
screen = pygame.display.set_mode(size)

BORDER = 5

MENU_TXT = ["Начать", "Правила игры", "Выход"]


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

    def boom(self):
        self.image = Bomb.img2
        self.rect.width = self.image.get_rect().width
        self.rect.height = self.image.get_rect().height
        self.rect.x -= self.rect.width // 4
        self.rect.y -= self.rect.height // 4

    def update(self, *args):
        if args:
            if self.image == Bomb.img1 and isinstance(args[0], pygame.sprite.GroupSingle):
                if pygame.sprite.collide_mask(self, args[0].sprite):
                    self.boom()
            elif hasattr(args[0], 'type') and args[0].type == pygame.MOUSEBUTTONUP and args[0].button != 1:
                if self.image == Bomb.img1 and self.rect.collidepoint(args[0].pos):
                    self.boom()
        else:
            self.rect = self.rect.move(random.randrange(3) - 1,
                                       random.randrange(3) - 1)


def game_main():
    all_sprites = pygame.sprite.Group()
    all_bombs = pygame.sprite.Group()
    main_character = pygame.sprite.GroupSingle()

    pers = Creature(all_sprites, main_character)
    clock = pygame.time.Clock()
    fps = 60
    running = True
    stage = 'menu'
    selector = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONUP:
                if stage == 'menu':
                    pass
                elif stage == 'game':
                    if event.button == 1:
                        Bomb(event.pos, all_sprites, all_bombs)
                    else:
                        all_sprites.update(event)
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if stage == 'game':
                    if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                        stage = 'menu'
                    all_sprites.update(event)
                elif stage == 'menu':
                    if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                        if selector == 0:
                            stage = 'game'
                        elif selector == len(MENU_TXT) - 1:
                            running = False
                    elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                        selector = min(len(MENU_TXT) - 1, selector + 1)
                    elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                        selector = max(0, selector - 1)

        if stage == 'menu':
            screen.fill(pygame.Color('coral4'))
            font = pygame.font.Font(None, 30)

            for idx, line in enumerate(MENU_TXT):
                string_rendered = font.render(line, 1, pygame.Color('white'))
                intro_rect = string_rendered.get_rect()
                intro_rect.top = 40 + idx * 20
                intro_rect.x = width // 2 - intro_rect.width // 2
                screen.blit(string_rendered, intro_rect)
                if idx == selector:
                    pygame.draw.rect(screen, pygame.Color('white'), intro_rect, 1)

        elif stage == 'game':
            screen.fill((50, 20, 75))
            all_bombs.update(main_character)
            # pygame.sprite.groupcollide(main_character, all_bombs, False, True)
            all_sprites.update()
            all_bombs.draw(screen)
            main_character.draw(screen)

        pygame.display.flip()
        clock.tick(fps)
    return True


if __name__ == '__main__':
    game_main()
    pygame.quit()
