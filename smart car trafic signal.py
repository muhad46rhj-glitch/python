import pygame
import sys

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Smart Traffic Signal Simulator")
clock = pygame.time.Clock()

# Colours
ROAD = (60, 60, 60)
GRASS = (70, 160, 70)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
BLUE = (0, 100, 255)

# Custom event
CHANGE_SIGNAL = pygame.USEREVENT + 1


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((50, 30))
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 235

        self.velocity = 3

    def update(self):
        self.rect.x += self.velocity

        # Reached right boundary
        if self.rect.right >= 700:
            self.rect.right = 700
            self.velocity = -3
            pygame.event.post(pygame.event.Event(CHANGE_SIGNAL))

        # Reached left boundary
        if self.rect.left <= 100:
            self.rect.left = 100
            self.velocity = 3
            pygame.event.post(pygame.event.Event(CHANGE_SIGNAL))


# Create car and sprite group
car = Car()
cars = pygame.sprite.Group()
cars.add(car)

# Traffic signal
signal = RED

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Change signal when car reaches boundary
        if event.type == CHANGE_SIGNAL:
            if signal == RED:
                signal = GREEN
                car.image.fill(BLUE)

            elif signal == GREEN:
                signal = YELLOW
                car.image.fill(YELLOW)

            else:
                signal = RED
                car.image.fill(RED)

    # Update car
    cars.update()

    # Background
    screen.fill(GRASS)

    # Road
    pygame.draw.rect(screen, ROAD, (0, 200, 800, 100))

    # Road lines
    for x in range(0, 800, 80):
        pygame.draw.rect(screen, WHITE, (x, 247, 40, 5))

    # Traffic light box
    pygame.draw.rect(screen, (30, 30, 30), (700, 50, 60, 150))

    # Traffic lights
    pygame.draw.circle(screen, RED, (730, 80), 18)
    pygame.draw.circle(screen, YELLOW, (730, 125), 18)
    pygame.draw.circle(screen, GREEN, (730, 170), 18)

    # Show active signal
    if signal == RED:
        pygame.draw.circle(screen, (255, 100, 100), (730, 80), 18)
    elif signal == YELLOW:
        pygame.draw.circle(screen, (255, 255, 150), (730, 125), 18)
    else:
        pygame.draw.circle(screen, (100, 255, 100), (730, 170), 18)

    # Draw sprite group
    cars.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()