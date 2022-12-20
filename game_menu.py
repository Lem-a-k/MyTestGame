import pygame

from main import game_main

size = width, height = 1000, 500
pygame.init()
screen = pygame.display.set_mode(size)


if __name__ == "__main__":
    running = True
    game = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                running = game_main()
        screen.fill(pygame.Color("yellow"))
        pygame.display.flip()
    pygame.quit()