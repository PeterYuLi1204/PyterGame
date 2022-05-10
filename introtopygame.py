# Introduction to Pygame

import pygame

pygame.init()

# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WINDOW_TITLE = "Game"

def main():
    # Create a Window
    screen_size = (800, 800)
    screen = pygame.display.set_mode(screen_size)

    # Set the title of the window
    pygame.display.set_caption(WINDOW_TITLE)

    done = False

    clock = pygame.time.Clock()

    white = False
    # --------- MAIN PROGRAM LOOP ------------
    while not done:
        # ---- Event Handler
        for event in pygame.event.get():   # list of events
            if event.type == pygame.QUIT:
                # When user clicks red quit button
                done = True
            elif event.type == pygame.KEYDOWN:
                print("A key has been pressed")
            elif event.type == pygame.KEYUP:
                print("A key has been let go")

        # ---- Environment Logic


        # ---- Render The Environment



        # Draw a rectangle
        # rect -> [x, y, Width, Height]
        if not white:
            screen.fill(GREEN)
            pygame.draw.rect(screen, BLACK, [100, 100, 200, 200])
            pygame.draw.rect(screen, BLACK, [500, 100, 200, 200])
            pygame.draw.rect(screen, BLACK, [300, 300, 200, 300])
            pygame.draw.rect(screen, BLACK, [200, 400, 100, 300])
            pygame.draw.rect(screen, BLACK, [500, 400, 100, 300])
            white = True
        else:
            screen.fill(WHITE)
            white = False



        # ---- Flip the display
        # Updates the screen with what we've drawn
        pygame.display.flip()

        # ---- Tick the clock
        clock.tick(75)

if __name__ == "__main__":
    main()