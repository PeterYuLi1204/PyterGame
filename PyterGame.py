import pygame
import math

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
        self.image = pygame.image.load("./assets/box.jpg")
        self.image = pygame.transform.scale(self.image, (15, 15))

        self.rect = self.image.get_rect()

    def update(self):
        """ Move the player. """
        self.rect.center = pygame.mouse.get_pos()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./assets/demon.png")
        self.image = pygame.transform.scale(self.image, (96, 70))

        self.rect = self.image.get_rect()



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
    enemy_sprites_group = pygame.sprite.Group()

    player = Player()
    all_sprites_group.add(player)

    enemy = Enemy()
    all_sprites_group.add(enemy)
    enemy_sprites_group.add(enemy)

    enemy.rect.x = 100
    enemy.rect.y = 100

    # Light circle
    radius = 75

    cover_surf = pygame.Surface((radius*2, radius*2))
    cover_surf.fill(0)
    cover_surf.set_colorkey((255, 255, 255))
    pygame.draw.circle(cover_surf, (255, 255, 255), (radius, radius), radius)

    # List of clicked sprites
    clicked_sprites = []

    # ----- MAIN LOOP

    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                # get a list of all sprites that are under the mouse cursor
                clicked_sprites = [s for s in all_sprites_group if s.rect.collidepoint(pos)]
                print(clicked_sprites)
                # do something with the clicked sprites...

        clicked_sprites.clear()

        print(clicked_sprites)

        # Light circle
        clip_center = pygame.mouse.get_pos()
        print(clip_center)

        screen.fill(0)
        clip_rect = pygame.Rect(clip_center[0] - radius, clip_center[1] - radius, radius * 2, radius * 2)
        screen.set_clip(clip_rect)

        # ----- LOGIC
        all_sprites_group.update()

        # ----- RENDER
        screen.blit(background, (0, 0))
        screen.blit(cover_surf, clip_rect)

        # Render enemy only if they are close enough to the light
        if math.sqrt((enemy.rect.x + (enemy.rect.width / 2) - clip_center[0]) ** 2 + (enemy.rect.y + (enemy.rect.height / 2) - clip_center[1]) ** 2) <= 90:
            enemy_sprites_group.draw(screen)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(75)

    pygame.quit()


if __name__ == "__main__":
    main()