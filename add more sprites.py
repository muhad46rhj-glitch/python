import pygame
import random

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
WHITE = (255, 255, 255)

# Player
player = pygame.Rect(375, 500, 50, 50)
player_speed = 5

# Seven enemy sprites
enemies = []

for i in range(7):
    enemy = pygame.Rect(
        random.randint(0, WIDTH - 40),
        random.randint(50, 350),
        40,
        40
    )
    enemies.append(enemy)

# Score
score = 0

# Font
font = pygame.font.Font(None, 36)

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed

    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    if keys[pygame.K_UP]:
        player.y -= player_speed

    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Keep player on screen
    player.x = max(0, min(WIDTH - player.width, player.x))
    player.y = max(0, min(HEIGHT - player.height, player.y))

    # Check collisions
    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1

            # Move enemy to a new random position
            enemy.x = random.randint(0, WIDTH - enemy.width)
            enemy.y = random.randint(50, 350)

    # Draw everything
    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Draw score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
