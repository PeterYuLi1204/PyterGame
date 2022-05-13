import pygame

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


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    pygame.mouse.set_visible(False)

    background = pygame.image.load("./assets/floor_tiles.png").convert()


    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    all_sprites_group = pygame.sprite.Group()

    player = Player()
    all_sprites_group.add(player)

    radius = 75

    cover_surf = pygame.Surface((radius*2, radius*2))
    cover_surf.fill(0)
    cover_surf.set_colorkey((255, 255, 255))
    pygame.draw.circle(cover_surf, (255, 255, 255), (radius, radius), radius)

    clicked_sprites = []

    # ----- MAIN LOOP

    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                # get a list of all sprites that are under the mouse cursor
                clicked_sprites = [s for s in all_sprites_group if s.rect.collidepoint(pos)]
                print(clicked_sprites)
                # do something with the clicked sprites...

        clip_center = pygame.mouse.get_pos()

        clicked_sprites.clear()

        print(clicked_sprites)

        screen.fill(0)
        clip_rect = pygame.Rect(clip_center[0] - radius, clip_center[1] - radius, radius * 2, radius * 2)
        screen.set_clip(clip_rect)

        # ----- LOGIC
        all_sprites_group.update()

        # ----- RENDER
        screen.blit(background, (0, 0))
        screen.blit(cover_surf, clip_rect)
        all_sprites_group.draw(screen)

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(75)

    pygame.quit()


if __name__ == "__main__":
    main()