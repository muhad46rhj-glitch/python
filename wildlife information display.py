import pygame
import sys

# Start Pygame
pygame.init()

# Window
WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wildlife Information Display")

# Colors
SKY = (135, 206, 235)
GRASS = (80, 180, 80)
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
ORANGE = (255, 165, 0)
GREY = (130, 130, 130)
DARK_GREY = (90, 90, 90)
BLUE = (70, 160, 220)
GREEN = (40, 140, 60)
BROWN = (120, 80, 40)

# Fonts
title_font = pygame.font.SysFont("arial", 42, bold=True)
fact_font = pygame.font.SysFont("arial", 24)
small_font = pygame.font.SysFont("arial", 20)

def draw_penguin(x, y):
    # Body
    pygame.draw.ellipse(screen, BLACK, (x, y, 150, 220))

    # White belly
    pygame.draw.ellipse(screen, WHITE, (x + 25, y + 65, 100, 140))

    # Eyes
    pygame.draw.circle(screen, WHITE, (x + 48, y + 55), 18)
    pygame.draw.circle(screen, WHITE, (x + 102, y + 55), 18)

    pygame.draw.circle(screen, BLACK, (x + 48, y + 55), 8)
    pygame.draw.circle(screen, BLACK, (x + 102, y + 55), 8)

    # Beak
    pygame.draw.polygon(
        screen,
        ORANGE,
        [
            (x + 75, y + 75),
            (x + 55, y + 95),
            (x + 95, y + 95)
        ]
    )

    # Left wing
    pygame.draw.ellipse(screen, DARK_GREY, (x - 35, y + 90, 65, 120))

    # Right wing
    pygame.draw.ellipse(screen, DARK_GREY, (x + 120, y + 90, 65, 120))

    # Feet
    pygame.draw.ellipse(screen, ORANGE, (x + 20, y + 195, 55, 25))
    pygame.draw.ellipse(screen, ORANGE, (x + 75, y + 195, 55, 25))


def draw_elephant(x, y):
    # Body
    pygame.draw.ellipse(screen, GREY, (x, y + 45, 190, 120))

    # Head
    pygame.draw.circle(screen, GREY, (x + 35, y + 75), 65)

    # Ear
    pygame.draw.circle(screen, DARK_GREY, (x + 70, y + 55), 45)

    # Eye
    pygame.draw.circle(screen, BLACK, (x + 20, y + 55), 7)

    # Trunk
    pygame.draw.line(
        screen,
        GREY,
        (x - 20, y + 85),
        (x - 65, y + 120),
        25
    )

    pygame.draw.line(
        screen,
        GREY,
        (x - 65, y + 120),
        (x - 55, y + 155),
        20
    )

    # Legs
    pygame.draw.rect(screen, GREY, (x + 25, y + 135, 30, 70))
    pygame.draw.rect(screen, GREY, (x + 75, y + 135, 30, 70))
    pygame.draw.rect(screen, GREY, (x + 125, y + 135, 30, 70))

    # Feet
    pygame.draw.rect(screen, DARK_GREY, (x + 20, y + 195, 40, 15))
    pygame.draw.rect(screen, DARK_GREY, (x + 70, y + 195, 40, 15))
    pygame.draw.rect(screen, DARK_GREY, (x + 120, y + 195, 40, 15))


clock = pygame.time.Clock()

running = True

while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill(SKY)

    # Clouds
    pygame.draw.circle(screen, WHITE, (120, 90), 30)
    pygame.draw.circle(screen, WHITE, (155, 90), 40)
    pygame.draw.circle(screen, WHITE, (195, 90), 30)

    pygame.draw.circle(screen, WHITE, (700, 80), 30)
    pygame.draw.circle(screen, WHITE, (735, 80), 40)
    pygame.draw.circle(screen, WHITE, (775, 80), 30)

    # Mountains
    pygame.draw.polygon(
        screen,
        GREEN,
        [(0, 350), (180, 180), (350, 350)]
    )

    pygame.draw.polygon(
        screen,
        GREEN,
        [(250, 350), (470, 170), (700, 350)]
    )

    pygame.draw.polygon(
        screen,
        GREEN,
        [(600, 350), (780, 190), (900, 350)]
    )

    # Ground
    pygame.draw.rect(screen, GRASS, (0, 350, WIDTH, 250))

    # Pond
    pygame.draw.ellipse(screen, BLUE, (300, 430, 350, 100))

    # Trees
    for tree_x in [70, 820]:
        pygame.draw.rect(screen, BROWN, (tree_x, 270, 35, 100))
        pygame.draw.circle(screen, GREEN, (tree_x + 18, 250), 60)

    title = title_font.render(
        "WILDLIFE INFORMATION DISPLAY",
        True,
        BLACK
    )

    screen.blit(title, (180, 20))

    fact1 = fact_font.render(
        "Penguins are birds that cannot fly.",
        True,
        BLACK
    )

    fact2 = fact_font.render(
        "They are excellent swimmers!",
        True,
        BLACK
    )

    screen.blit(fact1, (40, 120))
    screen.blit(fact2, (40, 155))

    # Elephant information
    elephant_text = small_font.render(
        "Elephants are the largest land animals.",
        True,
        BLACK
    )

    screen.blit(elephant_text, (500, 270))

    # Draw animals
    draw_penguin(120, 300)
    draw_elephant(620, 300)

    # Update screen
    pygame.display.flip()

    # 60 FPS
    clock.tick(60)


# Quit
pygame.quit()
sys.exit()
