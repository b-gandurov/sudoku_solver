import copy

import pygame

pygame.init()

size = (540, 540)
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont("arial", 40)

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def draw_grid():
    for x in range(0, 540, 60):
        pygame.draw.lines(screen, (0, 0, 0), False, [(x, 0), (x, 540)], 2 if x % 180 == 0 else 1)
    for y in range(0, 540, 60):
        pygame.draw.lines(screen, (0, 0, 0), False, [(0, y), (540, y)], 2 if y % 180 == 0 else 1)

def draw_board(game_board):
    screen.fill((255, 255, 255))
    for i in range(9):
        for j in range(9):
            if game_board[i][j] != 0:
                color = (255, 0, 0) if temp_board[i][j] == 0 else (0, 0, 0)
                text = font.render(str(game_board[i][j]), True, color)
                screen.blit(text, (j * 60 + 20, i * 60 + 15))
    draw_grid()
    pygame.display.update()

def find_empty_spot(game_board):
    for i in range(9):
        for j in range(9):
            if game_board[i][j] == 0:
                return i, j
    return None

def is_valid_move(game_board, num, pos):
    row, col = pos

    if any(game_board[row][i] == num for i in range(9)) or any(game_board[i][col] == num for i in range(9)):
        return False

    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if game_board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve_sudoku(game_board):
    empty_spot = find_empty_spot(game_board)
    if not empty_spot:
        return True
    row, col = empty_spot

    for num in range(1, 10):
        if is_valid_move(board, num, (row, col)):
            board[row][col] = num
            draw_board(board)
            pygame.time.wait(100)
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

temp_board = copy.deepcopy(board)
solve_sudoku(board)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
