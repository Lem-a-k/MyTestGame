import pygame

from main import game_main

size = width, height = 1000, 500
pygame.init()
screen = pygame.display.set_mode(size)


if __name__ == "__main__":
    running = True
    game = None
    font = pygame.font.Font(None, 30)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                running = game_main()
        screen.fill(pygame.Color("yellow"))
        string_rendered = font.render("Нажмите <пробел>", 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 40
        intro_rect.x = width // 2 - intro_rect.width // 2
        screen.blit(string_rendered, intro_rect)
        pygame.display.flip()
    pygame.quit()