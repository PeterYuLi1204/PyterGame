import pygame
import math
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1200
HEIGHT = 1200
TITLE = "Pyter Game"


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("assets/circle.png")
        self.image = pygame.transform.scale(self.image, (150, 150))

        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        """ Move the player. """
        self.rect.center = pygame.mouse.get_pos()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./assets/demon.png")
        self.image = pygame.transform.scale(self.image, (96, 70))

        self.rect = self.image.get_rect()
        self.rect.center = random_coords()

        self.mask = pygame.mask.from_surface(self.image)

        self.xvel = 0
        self.yvel = 0

    def update(self):
        """ Move the player. """
        self.rect.x += self.xvel
        self.rect.y += self.yvel


def random_coords() -> tuple:
    """Returns a random x, y coordinate between 0 to WIDTH and 0 to HEIGHT"""
    return random.randrange(80, WIDTH - 80), random.randrange(80, HEIGHT - 80)


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    pygame.mouse.set_visible(False)

    background = pygame.image.load("./assets/floor_tiles.png").convert()

    # ----- LOCAL VARIABLES
    # Pygame conditions
    done = False
    clock = pygame.time.Clock()

    # Sprites
    all_sprites_group = pygame.sprite.Group()
    player_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()

    player = Player()
    player_sprites_group.add(player)
    all_sprites_group.add(player)

    enemy = Enemy()
    enemy_sprites_group.add(enemy)
    all_sprites_group.add(enemy)

    # Light circle
    radius = 75

    cover_surf = pygame.Surface((radius * 2, radius * 2))
    cover_surf.fill(0)
    cover_surf.set_colorkey((255, 255, 255))
    pygame.draw.circle(cover_surf, (255, 255, 255), (radius, radius), radius)

    # List of clicked sprites
    clicked_sprites = []

    # Time
    time_to_find = 15000
    time_to_catch = 10000

    time_spawned = 0
    time_found = 0
    time_caught = 0

    # Boolean to check if found
    found = False

    # Enemy velocity
    velocity_x = 2
    velocity_y = 4

    # Sounds

    # ----- MAIN LOOP

    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # get a list of all sprites that are under the mouse cursor
                clicked_sprites = [s for s in enemy_sprites_group if s.rect.collidepoint(pos)]
                print(clicked_sprites)
                # do something with the clicked sprites...

        clicked_sprites.clear()

        # Light circle
        clip_center = pygame.mouse.get_pos()

        screen.fill(0)
        clip_rect = pygame.Rect(clip_center[0] - radius, clip_center[1] - radius, radius * 2, radius * 2)
        screen.set_clip(clip_rect)

        # ----- LOGIC
        all_sprites_group.update()

        if not found:
            enemy_collide = pygame.sprite.spritecollide(player, enemy_sprites_group, False, pygame.sprite.collide_mask)

        if (enemy.rect.x + 48)> WIDTH or enemy.rect.x < 0:
            enemy.xvel *= -1

        if (enemy.rect.y + 35) > HEIGHT or enemy.rect.y < 0:
            enemy.yvel *= -1

        if len(enemy_collide) > 0:
            found = True

            enemy.xvel += velocity_x
            enemy.yvel += velocity_y

            velocity_x += 2
            velocity_y += 2

            time_found = pygame.time.get_ticks()

            enemy_collide.clear()

        # ----- RENDER
        screen.blit(background, (0, 0))

        enemy_sprites_group.draw(screen)

        screen.blit(cover_surf, clip_rect)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(75)


    pygame.quit()


if __name__ == "__main__":
    main()
