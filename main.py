import pygame

size = width, height = 800, 400


class Board:

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.board = [[0] * m for _ in range(n)]

        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.color = pygame.Color('purple')

    def set_view(self, left, top, cell_size, color=pygame.Color('purple')):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.color = color

    def draw(self, cur_screen):
        for i in range(self.n):
            for j in range(self.m):
                pygame.draw.rect(cur_screen, self.color,
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size,
                                  self.cell_size + 1, self.cell_size + 1), 1)
                if self.board[i][j] == 1:
                    pygame.draw.circle(cur_screen, self.color,
                                       (self.left + j * self.cell_size + self.cell_size // 2,
                                        self.top + i * self.cell_size + self.cell_size // 2), self.cell_size // 2 - 1)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if self.left <= x <= self.left + self.m * self.cell_size:
            if self.top <= y <= self.top + self.n * self.cell_size:
                return (y - self.top) // self.cell_size, (x - self.left) // self.cell_size
        return None

    def on_click(self, cell_coords):
        i, j = cell_coords
        self.board[i][j] ^= 1

    def process_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        print(cell)
        if cell is not None:
            self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)

    board = Board(3, 5)
    board.set_view(50, 20, 100)
    clock = pygame.time.Clock()
    fps = 30
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                board.process_click(event.pos)
        screen.fill((250, 255, 200))
        board.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
