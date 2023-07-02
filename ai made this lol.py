import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cube Collector")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Player properties
player_size = 50
player_color = (0, 0, 255)
player_x = (screen_width - player_size) // 2
player_y = (screen_height - player_size) // 2
player_vel = 5

# Cube properties
cube_size = 25
cube_color = YELLOW
cubes_collected = 0

# Font properties
font = pygame.font.Font(None, 36)
win_font = pygame.font.Font(None, 72)

# Timer properties
cube_timer = pygame.USEREVENT + 1
pygame.time.set_timer(cube_timer, 2000)  # Create a cube every 2 seconds

# Set up the clock
clock = pygame.time.Clock()

# Function to draw the player and cubes
def draw_objects():
    screen.fill(WHITE)
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    for cube in cubes:
        pygame.draw.rect(screen, cube_color, (cube[0], cube[1], cube_size, cube_size))

    cubes_collected_text = font.render(f"Cubes Collected: {cubes_collected}", True, BLACK)
    screen.blit(cubes_collected_text, (10, 10))

    if cubes_collected >= 20:
        win_text = win_font.render("You Win!", True, BLACK)
        screen.blit(win_text, ((screen_width - win_text.get_width()) // 2, (screen_height - win_text.get_height()) // 2))

    pygame.display.flip()

# Game loop
cubes = []
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == cube_timer:
            cube_x = random.randint(0, screen_width - cube_size)
            cube_y = random.randint(0, screen_height - cube_size)
            cubes.append([cube_x, cube_y])

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player_y > 0:
        player_y -= player_vel
    if keys[pygame.K_s] and player_y < screen_height - player_size:
        player_y += player_vel
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_d] and player_x < screen_width - player_size:
        player_x += player_vel

    for cube in cubes:
        if (
            cube[0] < player_x + player_size
            and cube[0] + cube_size > player_x
            and cube[1] < player_y + player_size
            and cube[1] + cube_size > player_y
        ):
            cubes.remove(cube)
            cubes_collected += 1

    draw_objects()

    clock.tick(60)
