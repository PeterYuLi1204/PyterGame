import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Collide"

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/link.png")
        self.image = pygame.transform.scale(self.image, (51,66))

        self.rect = self.image.get_rect()

    def update(self):
        # Follow the mouse
        self.rect.center = pygame.mouse.get_pos()

class Treasure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/rupee.png")
        self.image = pygame.transform.scale(self.image, (22, 40))

        self.rect = self.image.get_rect()
        self.rect.center = random_coords()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Image
        self.image = pygame.image.load("./assets/ganondorf.png")
        self.image = pygame.transform.scale(self.image, (165, 111))

        self.rect = self.image.get_rect()
        self.rect.center = random_coords()

        self.xvel = 5
        self.yvel = 5

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel

def random_coords() -> list:
    """Returns a random x, y coordinate between 0 to WIDTH and 0 to HEIGHT"""

    return random.randrange(80, WIDTH-80), random.randrange(80, HEIGHT-80)


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)
    pygame.mouse.set_visible(False)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Create sprite group
    all_sprites_group = pygame.sprite.Group()
    treasure_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()

    # Create sprites to fill groups
    player = Player()
    all_sprites_group.add(player)

    # Number of treasure to create
    treasure_num = 10

    # Number of enemies to create
    enemy_num = 1

    # Score of player
    score = 0
    font = pygame.font.SysFont("American Typewriter", 20)

    # Lives of player
    lives = 3
    collided_time = 0
    time_invincible = 1000

    # Invincible
    flash = False

    # Level player is on
    level = 1

    for i in range(enemy_num):
        enemy = Enemy()
        all_sprites_group.add(enemy)
        enemy_sprites_group.add(enemy)

    for i in range(treasure_num):
        treasure = Treasure()
        all_sprites_group.add(treasure)
        treasure_sprites_group.add(treasure)


    treasure_sound = pygame.mixer.Sound("./assets/rupee.ogg")

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites_group.update()

        collided_treasure = pygame.sprite.spritecollide(player, treasure_sprites_group, dokill=True)
        collided_player = pygame.sprite.spritecollide(player, enemy_sprites_group, dokill=False)

        # Colliding with treasure
        if len(collided_treasure) > 0:
            treasure_sound.play()

        for treasure in collided_treasure:
            score += 1
            print(score)

        if score % treasure_num == 0 and len(treasure_sprites_group) != treasure_num:

            if lives < 3:
                lives += 1

            level += 1

            if enemy.xvel > 0:
                enemy.xvel += 1
            else:
                enemy.xvel -= 1

            if enemy.yvel > 0:
                enemy.yvel += 1
            else:
                enemy.yvel -= 1

            for i in range(treasure_num):
                treasure = Treasure()
                all_sprites_group.add(treasure)
                treasure_sprites_group.add(treasure)

        # Collide with enemy
        if (enemy.rect.x + 165) >= WIDTH or enemy.rect.x <= 0:
            enemy.xvel *= -1

        if (enemy.rect.y + 111) >= HEIGHT or enemy.rect.y <= 0:
            enemy.yvel *= -1

        if len(collided_player) > 0:
            if pygame.time.get_ticks() - collided_time > time_invincible:
                lives -= 1
                collided_time = pygame.time.get_ticks()
                flash = True

            if lives == 0:
                done = True

        #if pygame.time.get_ticks() - collided_time < time_invincible:




        # ----- RENDER
        screen.fill(WHITE)

        # Render sprites
        all_sprites_group.draw(screen)
        treasure_sprites_group.draw(screen)
        enemy_sprites_group.draw(screen)

        # Render text
        level_surf = font.render(f"Level: {level}", True, BLACK)
        screen.blit(level_surf, (10, 10))

        score_surf = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_surf, (10, 30))

        life_surf = font.render(f"Lives: {lives}", True, BLACK)
        screen.blit(life_surf, (10, 50))

        # ----- UPDATE DISPLAY
        pygame.display.flip()
        clock.tick(75)

    pygame.quit()


if __name__ == "__main__":
    main()