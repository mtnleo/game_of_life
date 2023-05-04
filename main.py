import pygame, time, gc
from copy import deepcopy

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of life by mtnleo")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
LIGHT_GRAY = (230, 230, 230)


BLOCK_SIZE = 20

MOUSE_POS = (WIDTH/2, HEIGHT/2)

FPS = 75

pygame.font.init()
FONT = pygame.font.SysFont("couriernew", 18, bold=True)
ITER_TEXT = pygame.font.Font.render(FONT, "iters: ", True, BLACK, LIGHT_GRAY)

def get_empty_list():
    empty_list = []
    return empty_list

def get_matrix():
    matrix = []
    x, y = 0, 0
    for i in range(0, WIDTH // BLOCK_SIZE):
        row = get_empty_list()
        for j in range(0, HEIGHT // BLOCK_SIZE):
            row.append(False)
            y += BLOCK_SIZE
        matrix.append(row)
        x += BLOCK_SIZE

    return matrix

def update_matrix_coords(matrix, pos):
    new_matrix = deepcopy(matrix)
    x = pos[0]
    y = pos[1]

    new_matrix[x][y] = True
    return new_matrix

def update_matrix_coords_false(matrix, pos):
    new_matrix = deepcopy(matrix)
    x = pos[0]
    y = pos[1]

    new_matrix[x][y] = False
    return new_matrix

def update_matrix(matrix, pos):
    matrix[pos[0]][pos[1]] = True
    return matrix

def dead_cell_check(new_matrix, matrix, pos):
    alive_neighbors = 0

    for i in range(pos[0] - 1, pos[0] + 2):
        for j in range(pos[1] - 1, pos[1] + 2):
            if j > -1 and i > -1:
                try:
                    if i == pos[0] and j == pos[1]:
                        pass
                    elif matrix[i][j]:
                        alive_neighbors += 1
                except IndexError: ## if it surpasses the list index, don't evaluate
                    pass
            
    if alive_neighbors == 3:
        new_matrix[pos[0]][pos[1]] = True
    
    return new_matrix

def check_cells(new_matrix, matrix, pos):
    alive_neighbors = 0

    for i in range(pos[0] - 1, pos[0] + 2):
        for j in range(pos[1] - 1, pos[1] + 2):
            if j > -1 and i > -1:
                try:
                    if i == pos[0] and j == pos[1]:
                        pass
                    elif matrix[i][j]:
                        alive_neighbors += 1
                    else:
                        new_matrix = dead_cell_check(new_matrix, matrix, (i, j))
                except IndexError: ## if it surpasses the list index, don't evaluate
                    pass

    if alive_neighbors < 2 or alive_neighbors > 3:
        new_matrix = update_matrix_coords_false(new_matrix, pos)
    
    return new_matrix

def check_matrix(matrix):
    new_matrix = deepcopy(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j]:
                new_matrix = check_cells(new_matrix, matrix, (i, j))

    return new_matrix

def draw_window():
    WIN.fill(BLACK)
    pygame.display.update()

def draw_iteration(iters):
    pos_y = 0
    pos_x = WIDTH - (WIDTH * .2)
    rect_width = WIDTH * .2
    rect_height = HEIGHT * .05

    rect = pygame.Rect(pos_x, pos_y, rect_width, rect_height)
    pygame.draw.rect(WIN, LIGHT_GRAY, rect, 0)
    
    text = pygame.font.Font.render(FONT, str(iters), True, BLACK)
    WIN.blit(ITER_TEXT, (pos_x + 2, pos_y + 3))
    WIN.blit(text, (pos_x + rect_width // 2 - 20, pos_y + 4))
    


def draw_grid_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            rect = pygame.Rect(i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            if matrix[i][j]:
                pygame.draw.rect(WIN, WHITE, rect, 0)
            else:
                pygame.draw.rect(WIN, BLACK, rect, 0)
                pygame.draw.rect(WIN, GRAY, rect, 1)




def main():
    clock = pygame.time.Clock()
    run = True
    matrix = get_matrix()
    ready = False

    ITERS = 0

    while run:
        while not ready and run: # Time for drawing the initial state, space to continue
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    left_click, _, right_click = pygame.mouse.get_pressed()

                    x = pygame.mouse.get_pos()[0] // BLOCK_SIZE
                    y =  pygame.mouse.get_pos()[1] // BLOCK_SIZE

                    if left_click:
                        matrix = update_matrix_coords(matrix, (x, y))
                    if right_click:
                        matrix = update_matrix_coords_false(matrix, (x, y))

                if event.type == pygame.KEYDOWN:
                    ready = True

            draw_grid_matrix(matrix)

            pygame.display.update()

        while ready and run: # Actual game

            clock.tick(6)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            draw_grid_matrix(matrix)
            draw_iteration(ITERS)

            matrix = check_matrix(matrix)
            ITERS += 1

            pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()