import random

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1200
HEIGHT = 900
TITLE = "DVD Screensaver"

class Dvdlogo(pygame.sprite.Sprite):
    def __init__(self):
        # call superclass constructor
        super().__init__()

        self.image = pygame.image.load("./assets/DVDLogo.jpg")
        self.image = pygame.transform.scale(
            self.image,
            (235, 117),
        )
        # Default x and y is (0, 0)
        self.rect = self.image.get_rect()

        self.xvel = random.choice([-2, 2])

        self.yvel = random.choice([-2, 2])

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    dvd_logo = Dvdlogo()
    # set the coordinates of dvd_logo explicitly
    dvd_logo.rect.x = 150
    dvd_logo.rect.y = 180

    # Create an all sprite group
    all_sprites_group = pygame.sprite.Group()

    all_sprites_group.add(dvd_logo)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites_group.update()

        if (dvd_logo.rect.x + 236) >= WIDTH or dvd_logo.rect.x <= 0:
            dvd_logo.xvel *= -1

        if (dvd_logo.rect.y + 118) >= HEIGHT or dvd_logo.rect.y <= 0:
            dvd_logo.yvel *= -1

        # ----- RENDER
        screen.fill(BLACK)

        all_sprites_group.draw(screen)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(75)

    pygame.quit()


if __name__ == "__main__":
    main()