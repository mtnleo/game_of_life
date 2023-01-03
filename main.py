import pygame, time

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of life by mtnleo")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

BLOCK_SIZE = 20

MOUSE_POS = (WIDTH/2, HEIGHT/2)

FPS = 1000

def draw_window():
    WIN.fill(BLACK)
    pygame.display.update()

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(WIN, GRAY, rect, 1)

def calculate_pos(coord):
    rectPos = coord // BLOCK_SIZE
    drawPos = rectPos * BLOCK_SIZE
    return drawPos

def draw_rectangle(pos):
    pos_x = pos[0]
    pos_y = pos[1]

    x = calculate_pos(pos_x)
    y = calculate_pos(pos_y)

    rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(WIN, WHITE, rect, 0)
            

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        draw_grid()
        
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                draw_rectangle(pygame.mouse.get_pos())

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()