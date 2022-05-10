import random

import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Snowscape"

class Snow(pygame.sprite.Sprite):
    def __init__(self, width: int, yvel: int):
        """

        :param width: width of snow in px
        """
        super().__init__()

        self.image = pygame.Surface([width+10, width+10])
        self.image = self.image.convert_alpha()
        self.image.fill((0,0,0,0))
        # fill that image with an actual sprite
        pygame.draw.circle(self.image, WHITE, (15, 15), width // 2)

        self.rect = self.image.get_rect()

        self.yvel = yvel

    def update(self):
        if self.rect.y > HEIGHT:
            self.rect.y = -30
            self.rect.x = random.randrange(0, WIDTH)

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

    snow_sizes = 5
    num_snow = 120

    # Create a new snow object
    snow_sprites = pygame.sprite.Group()

    for i in range(snow_sizes):
        for n in range (num_snow):

            snow = Snow(10 + 5*i, i + 1)

            snow_sprites.add(snow)

            x, y = (random.randrange(0, WIDTH), random.randrange(0, HEIGHT))

            snow.rect.center = (x, y)


    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        snow_sprites.update()

        # ----- RENDER
        screen.fill(BLACK)

        snow_sprites.draw(screen)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(75)

    pygame.quit()


if __name__ == "__main__":
    main()