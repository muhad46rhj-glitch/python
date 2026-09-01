import math
import random
import pygame

pygame.init()

# -----------------------------
# Screen
# -----------------------------
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption("Space Invader")

clock = pygame.time.Clock()

# -----------------------------
# Image Sizes
# -----------------------------
PLAYER_WIDTH = 70
PLAYER_HEIGHT = 70

ENEMY_WIDTH = 60
ENEMY_HEIGHT = 60

BULLET_WIDTH = 20
BULLET_HEIGHT = 35

# -----------------------------
# Speeds
# -----------------------------
PLAYER_SPEED = 7
ENEMY_SPEED = 2
ENEMY_DROP = 30
BULLET_SPEED = 10

# -----------------------------
# Load Images
# -----------------------------
background = pygame.image.load(
    "background.jpg"
).convert()

background = pygame.transform.scale(
    background,
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

playerImg = pygame.image.load(
    "spaceship.png"
).convert_alpha()

playerImg = pygame.transform.scale(
    playerImg,
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)

enemyImg = pygame.image.load(
    "enemy.png"
).convert_alpha()

enemyImg = pygame.transform.scale(
    enemyImg,
    (ENEMY_WIDTH, ENEMY_HEIGHT)
)

bulletImg = pygame.image.load(
    "bullet.png"
).convert_alpha()

bulletImg = pygame.transform.scale(
    bulletImg,
    (BULLET_WIDTH, BULLET_HEIGHT)
)

# -----------------------------
# Player
# -----------------------------
playerX = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
playerY = SCREEN_HEIGHT - 100

# -----------------------------
# Enemies
# -----------------------------
num_of_enemies = 6

enemyX = []
enemyY = []
enemyX_change = []

for i in range(num_of_enemies):

    enemyX.append(
        random.randint(
            0,
            SCREEN_WIDTH - ENEMY_WIDTH
        )
    )

    enemyY.append(
        random.randint(50, 150)
    )

    enemyX_change.append(
        ENEMY_SPEED
    )

# -----------------------------
# Bullet
# -----------------------------
bulletX = 0
bulletY = playerY

bullet_state = "ready"

# -----------------------------
# Score
# -----------------------------
score = 0

font = pygame.font.Font(
    "freesansbold.ttf",
    32
)

over_font = pygame.font.Font(
    "freesansbold.ttf",
    64
)


def show_score():

    text = font.render(
        "Score : " + str(score),
        True,
        (255, 255, 255)
    )

    screen.blit(
        text,
        (10, 10)
    )


def collision(
    enemy_x,
    enemy_y,
    bullet_x,
    bullet_y
):

    distance = math.sqrt(
        (enemy_x - bullet_x) ** 2
        +
        (enemy_y - bullet_y) ** 2
    )

    return distance < 30


def shoot():

    global bullet_state
    global bulletX
    global bulletY

    if bullet_state == "ready":

        bulletX = playerX + PLAYER_WIDTH // 2
        bulletY = playerY

        bullet_state = "fire"


# -----------------------------
# Game Loop
# -----------------------------
running = True

while running:

    # -------------------------
    # Events
    # -------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                shoot()

    # -------------------------
    # Smooth Player Movement
    # -------------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:

        playerX -= PLAYER_SPEED

    if keys[pygame.K_RIGHT]:

        playerX += PLAYER_SPEED

    # Keep spaceship inside screen
    playerX = max(
        0,
        min(
            playerX,
            SCREEN_WIDTH - PLAYER_WIDTH
        )
    )

    # -------------------------
    # Background
    # -------------------------
    screen.blit(
        background,
        (0, 0)
    )

    # -------------------------
    # Enemies
    # -------------------------
    for i in range(num_of_enemies):

        enemyX[i] += enemyX_change[i]

        # Bounce from walls
        if (
            enemyX[i] <= 0
            or enemyX[i] >= SCREEN_WIDTH - ENEMY_WIDTH
        ):

            enemyX_change[i] *= -1

            enemyY[i] += ENEMY_DROP

        # Collision
        if bullet_state == "fire":

            if collision(
                enemyX[i] + ENEMY_WIDTH // 2,
                enemyY[i] + ENEMY_HEIGHT // 2,
                bulletX,
                bulletY
            ):

                score += 1

                bullet_state = "ready"

                bulletY = playerY

                enemyX[i] = random.randint(
                    0,
                    SCREEN_WIDTH - ENEMY_WIDTH
                )

                enemyY[i] = random.randint(
                    50,
                    150
                )

        screen.blit(
            enemyImg,
            (enemyX[i], enemyY[i])
        )

    # -------------------------
    # Bullet
    # -------------------------
    if bullet_state == "fire":

        bulletY -= BULLET_SPEED

        screen.blit(
            bulletImg,
            (
                bulletX - BULLET_WIDTH // 2,
                bulletY
            )
        )

        if bulletY < 0:

            bullet_state = "ready"

            bulletY = playerY

    # -------------------------
    # Player
    # -------------------------
    screen.blit(
        playerImg,
        (playerX, playerY)
    )

    # -------------------------
    # Score
    # -------------------------
    show_score()

    # -------------------------
    # Update
    # -------------------------
    pygame.display.flip()

    clock.tick(60)


pygame.quit()