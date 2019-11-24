import pygame
import sys
import time

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
blue_block = (3, 132, 252)
yellow_block = (255, 217, 0)
green_block = (32, 212, 4)
display_h = 720
display_w = 600
rect_x = 50
rect_y = 50
rect_change_x = 9
rect_change_y = 9

gamedisplay = pygame.display.set_mode((display_w, display_h))
pygame.display.set_caption("Stacker")
clock = pygame.time.Clock()
# images to load
logo = pygame.image.load("stacker_logo.png")
block = pygame.image.load("block.png")
grid_line = pygame.image.load("grid_line.png")
horizontal_line = pygame.image.load("horizontal_line.png")

# start game text
font = pygame.font.Font("ARCADECLASSIC.TTF", 30)
text = font.render("Press  space  to  start", True, white)
textRect = text.get_rect()
textRect.center = (display_w//2, display_h//2)

# background


def welcome_background():
    gamedisplay.blit(logo, (0, 0))


def game_background():
    for x_coord in range(60, 600, 60):
        gamedisplay.blit(grid_line, (x_coord, 0))

    for y_coord in range(60, 720, 60):
        gamedisplay.blit(horizontal_line, (0, y_coord))


def welcome_loop():
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bumped = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space key pressed")
                game_loop()

        gamedisplay.fill(black)
        gamedisplay.blit(text, textRect)
        welcome_background()
        pygame.display.update()
        clock.tick(60)


def game_loop():
    sq_x = 60
    sq_y = 660
    sq_change_x = 9
    blocks = []
    bumped = True
    while bumped:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("second space key pressed")

                    blocks.append((sq_x, sq_y))
                    # moves the block -60 after every space bar key press
                    sq_y -= 60
        gamedisplay.fill(black)
        for pos in blocks:

            pygame.draw.rect(gamedisplay, yellow_block, [*pos, 240, 60])

        # draws the initial block that is positioned at the bottom of the window
        pygame.draw.rect(gamedisplay, blue_block, [sq_x, sq_y, 240, 60])

        # boundaries so the block only is animated within the window
        sq_x += sq_change_x
        if sq_x > 360 or sq_x < 0:
            sq_change_x = sq_change_x * -1

        game_background()

        pygame.display.update()
        clock.tick(60)


welcome_loop()

pygame.quit()
quit()
