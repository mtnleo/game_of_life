import pygame, numpy as np

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of life by mtnleo")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

BLOCK_SIZE = 20

MOUSE_POS = (WIDTH/2, HEIGHT/2)

FPS = 75

def get_matrix():
    matrix = []
    x, y = 0, 0
    for i in range(0, WIDTH // BLOCK_SIZE):
        row = []
        for j in range(0, HEIGHT // BLOCK_SIZE):
            row.append(False)
            y += BLOCK_SIZE
        matrix.append(row)
        x += BLOCK_SIZE

    return matrix

def update_matrix_coords(matrix, pos):
    x = pos[0] // BLOCK_SIZE
    y = pos[1] // BLOCK_SIZE

    matrix[x][y] = True
    return matrix

def update_matrix(matrix, pos):
    matrix[pos[0]][pos[1]] = True
    return matrix


def draw_window():
    WIN.fill(BLACK)
    pygame.display.update()

def draw_grid_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            rect = pygame.Rect(i * BLOCK_SIZE, j * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            if matrix[i][j]:
                pygame.draw.rect(WIN, WHITE, rect, 0)
            else:
                pygame.draw.rect(WIN, GRAY, rect, 1)

            

def main():
    clock = pygame.time.Clock()
    run = True
    matrix = get_matrix()
    while run:
        draw_grid_matrix(matrix)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                matrix = update_matrix_coords(matrix, pygame.mouse.get_pos())

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()