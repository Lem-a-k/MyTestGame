from copy import deepcopy
from itertools import product

import pygame

size = width, height = 1000, 600


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
        if self.left <= x < self.left + self.m * self.cell_size:
            if self.top <= y < self.top + self.n * self.cell_size:
                return (y - self.top) // self.cell_size, (x - self.left) // self.cell_size
        return None

    def on_click(self, cell_coords):
        row, col = cell_coords
        self.board[row][col] ^= 1

    def process_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        print(cell)
        if cell is not None:
            self.on_click(cell)

    def step(self):
        new_board = deepcopy(self.board)
        for i in range(self.n):
            for j in range(self.m):
                neighbours = 0
                for di, dj in product([-1, 0, 1], repeat=2):
                    if di == dj == 0:
                        continue
                    n_i = (i + di) % self.n
                    n_j = (j + dj) % self.m
                    neighbours += self.board[n_i][n_j]
                if neighbours == 3:
                    new_board[i][j] = 1
                if neighbours < 2 or neighbours > 3:
                    new_board[i][j] = 0
        self.board = new_board


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(size)

    board = Board(25, 40)
    board.set_view(50, 20, 20)
    clock = pygame.time.Clock()
    BOARD_STEP = pygame.USEREVENT + 1
    pygame.time.set_timer(BOARD_STEP, 100)
    fps = 30
    pause = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                board.process_click(event.pos)
            elif event.type == pygame.MOUSEMOTION:
                if 1 in event.buttons:
                    board.process_click(event.pos)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pause = not pause
            elif event.type == BOARD_STEP:
                if not pause:
                    board.step()
        screen.fill((250, 255, 200))
        board.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
