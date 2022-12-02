import pygame

size = width, height = 800, 400


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    fps = 30
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pass
        screen.fill((250, 255, 200))
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
