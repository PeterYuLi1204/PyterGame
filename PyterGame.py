import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
SAND_YELLOW = (	194, 178, 128)
WIDTH = 1600
HEIGHT = 1200
TITLE = "Pyter Game"

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/player_fish_left.png")
        self.image = pygame.transform.scale(self.image, (79, 51))

        self.change_x = 0
        self.change_y = 0

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """
        self.rect.x += self.change_x

        self.rect.y += self.change_y

        if self.change_x < 0:
            self.image = pygame.image.load("./assets/player_fish_left.png")
            self.image = pygame.transform.scale(self.image, (79, 51))

        if self.change_x > 0:
            self.image = pygame.image.load("./assets/player_fish_right.png")
            self.image = pygame.transform.scale(self.image, (79, 51))

    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def go_up(self):
        """ Called when the user hits the left arrow. """
        self.change_y = -6

    def go_down(self):
        """ Called when the user hits the right arrow. """
        self.change_y = 6

    def stop_x(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0

    def stop_y(self):
        """ Called when the user lets off the keyboard. """
        self.change_y = 0

def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    all_sprites_group = pygame.sprite.Group()

    player = Player()
    all_sprites_group.add(player)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop_x()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop_x()
                if event.key == pygame.K_UP and player.change_y < 0:
                    player.stop_y()
                if event.key == pygame.K_DOWN and player.change_y > 0:
                    player.stop_y()

        # ----- LOGIC
        all_sprites_group.update()

        # ----- RENDER
        screen.fill(SKY_BLUE)
        pygame.draw.rect(screen, SAND_YELLOW, pygame.Rect(0, HEIGHT - 150, WIDTH, 150))
        all_sprites_group.draw(screen)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(75)

    pygame.quit()


if __name__ == "__main__":
    main()