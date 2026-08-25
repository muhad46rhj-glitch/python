import pygame
import random
import math

pygame.init()

# ==================================================
# SCREEN
# ==================================================

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dog Food Mission")

clock = pygame.time.Clock()

# ==================================================
# IMAGES
# ==================================================

background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(
    background,
    (WIDTH, HEIGHT)
)

dog_image = pygame.image.load(
    "dog.png"
).convert_alpha()

dog_image = pygame.transform.scale(
    dog_image,
    (100, 100)
)

police_image = pygame.image.load(
    "police.png"
).convert_alpha()

police_image = pygame.transform.scale(
    police_image,
    (80, 80)
)

# ==================================================
# FONTS
# ==================================================

font = pygame.font.Font(None, 40)
big_font = pygame.font.Font(None, 80)

# ==================================================
# GAME VARIABLES
# ==================================================

dog_x = WIDTH // 2
dog_y = HEIGHT // 2

dog_speed = 6

food_size = 45

mission = 1
food_needed = 5
food_collected = 0
score = 0

game_over = False

# ==================================================
# BULLETS
# ==================================================

bullets = []

bullet_speed = 7
shoot_timer = 0

# ==================================================
# CREATE POLICE
# ==================================================

def create_police():

    return {
        "x": random.randint(50, WIDTH - 130),
        "y": random.randint(120, HEIGHT - 120),

        "speed": 2,

        "dx": random.choice([-1, 1]),
        "dy": random.choice([-1, 1])
    }


# Start with 3 police

police_dogs = []

for i in range(3):
    police_dogs.append(create_police())

# ==================================================
# CREATE FOOD
# ==================================================

def create_food():

    return (
        random.randint(
            50,
            WIDTH - food_size - 50
        ),

        random.randint(
            120,
            HEIGHT - food_size - 50
        )
    )


food_x, food_y = create_food()

# ==================================================
# NEXT MISSION
# ==================================================

def next_mission():

    global mission
    global food_needed
    global food_collected
    global food_x
    global food_y

    mission += 1

    food_collected = 0

    # More food required

    food_needed += 2

    # Add one more police

    new_police = create_police()

    new_police["speed"] = (
        2 + mission * 0.15
    )

    police_dogs.append(
        new_police
    )

    # Make all police slightly faster

    for police in police_dogs:

        police["speed"] += 0.1

    # New food

    food_x, food_y = create_food()


# ==================================================
# RESET GAME
# ==================================================

def reset_game():

    global dog_x
    global dog_y

    global mission
    global food_needed
    global food_collected
    global score

    global game_over

    global police_dogs

    global food_x
    global food_y

    global bullets
    global shoot_timer

    dog_x = WIDTH // 2
    dog_y = HEIGHT // 2

    mission = 1

    food_needed = 5
    food_collected = 0

    score = 0

    game_over = False

    bullets = []

    shoot_timer = 0

    police_dogs = []

    for i in range(3):

        police_dogs.append(
            create_police()
        )

    food_x, food_y = create_food()


# ==================================================
# MAIN LOOP
# ==================================================

running = True

while running:

    # ==================================================
    # EVENTS
    # ==================================================

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        # ==================================================
        # ARREST MENU
        # ==================================================

        if game_over:

            if event.type == pygame.KEYDOWN:

                # R = RESTART

                if event.key == pygame.K_r:

                    reset_game()

                # N = NEXT MISSION

                elif event.key == pygame.K_n:

                    game_over = False

                    dog_x = WIDTH // 2
                    dog_y = HEIGHT // 2

                    bullets = []

                    shoot_timer = 0

                    next_mission()

                # Q = QUIT

                elif event.key == pygame.K_q:

                    running = False

    # ==================================================
    # GAME
    # ==================================================

    if not game_over:

        # ==================================================
        # DOG MOVEMENT
        # ==================================================

        keys = pygame.key.get_pressed()

        # Arrow keys

        if keys[pygame.K_LEFT]:

            dog_x -= dog_speed

        if keys[pygame.K_RIGHT]:

            dog_x += dog_speed

        if keys[pygame.K_UP]:

            dog_y -= dog_speed

        if keys[pygame.K_DOWN]:

            dog_y += dog_speed

        # WASD

        if keys[pygame.K_a]:

            dog_x -= dog_speed

        if keys[pygame.K_d]:

            dog_x += dog_speed

        if keys[pygame.K_w]:

            dog_y -= dog_speed

        if keys[pygame.K_s]:

            dog_y += dog_speed

        # Keep dog inside screen

        dog_x = max(
            0,
            min(
                dog_x,
                WIDTH - 100
            )
        )

        dog_y = max(
            70,
            min(
                dog_y,
                HEIGHT - 100
            )
        )

        # ==================================================
        # DOG RECTANGLE
        # ==================================================

        dog_rect = pygame.Rect(
            int(dog_x),
            int(dog_y),
            100,
            100
        )

        # ==================================================
        # FOOD
        # ==================================================

        food_rect = pygame.Rect(
            food_x,
            food_y,
            food_size,
            food_size
        )

        if dog_rect.colliderect(
            food_rect
        ):

            food_collected += 1

            score += 10

            food_x, food_y = create_food()

        # ==================================================
        # POLICE MOVEMENT
        # ==================================================

        for police in police_dogs:

            police["x"] += (
                police["dx"]
                * police["speed"]
            )

            police["y"] += (
                police["dy"]
                * police["speed"]
            )

            # Bounce left

            if police["x"] <= 0:

                police["x"] = 0

                police["dx"] = 1

            # Bounce right

            if police["x"] >= WIDTH - 80:

                police["x"] = WIDTH - 80

                police["dx"] = -1

            # Bounce top

            if police["y"] <= 70:

                police["y"] = 70

                police["dy"] = 1

            # Bounce bottom

            if police["y"] >= HEIGHT - 80:

                police["y"] = HEIGHT - 80

                police["dy"] = -1

            # Police rectangle

            police_rect = pygame.Rect(
                int(police["x"]),
                int(police["y"]),
                80,
                80
            )

            # ==================================================
            # POLICE ARREST
            # ==================================================

            if police_rect.colliderect(
                dog_rect
            ):

                game_over = True

        # ==================================================
        # POLICE SHOOTING
        # ==================================================

        if mission >= 10:

            shoot_timer += 1

            # Shoot every 90 frames

            if shoot_timer >= 90:

                shoot_timer = 0

                for police in police_dogs:

                    # Direction toward dog

                    dx = dog_x - police["x"]

                    dy = dog_y - police["y"]

                    distance = math.sqrt(
                        dx * dx + dy * dy
                    )

                    if distance == 0:

                        distance = 1

                    dx /= distance
                    dy /= distance

                    # Create bullet

                    bullets.append({

                        "x":
                            police["x"] + 40,

                        "y":
                            police["y"] + 40,

                        "dx":
                            dx,

                        "dy":
                            dy
                    })

        # ==================================================
        # MOVE BULLETS
        # ==================================================

        for bullet in bullets:

            bullet["x"] += (
                bullet["dx"]
                * bullet_speed
            )

            bullet["y"] += (
                bullet["dy"]
                * bullet_speed
            )

        # ==================================================
        # REMOVE BULLETS OUTSIDE SCREEN
        # ==================================================

        bullets = [

            bullet

            for bullet in bullets

            if (
                0 < bullet["x"] < WIDTH
                and
                70 < bullet["y"] < HEIGHT
            )
        ]

        # ==================================================
        # BULLET COLLISION
        # ==================================================

        for bullet in bullets:

            bullet_rect = pygame.Rect(

                int(bullet["x"]) - 7,

                int(bullet["y"]) - 7,

                14,

                14
            )

            if bullet_rect.colliderect(
                dog_rect
            ):

                game_over = True

        # ==================================================
        # INFINITE MISSIONS
        # ==================================================

        if (
            not game_over
            and
            food_collected >= food_needed
        ):

            next_mission()

    # ==================================================
    # DRAW BACKGROUND
    # ==================================================

    screen.blit(
        background,
        (0, 0)
    )

    # ==================================================
    # NORMAL GAME
    # ==================================================

    if not game_over:

        # ==================================================
        # DRAW FOOD
        # ==================================================

        pygame.draw.circle(

            screen,

            (255, 180, 0),

            (
                food_x
                + food_size // 2,

                food_y
                + food_size // 2
            ),

            23
        )

        pygame.draw.circle(

            screen,

            (255, 255, 255),

            (
                food_x
                + food_size // 2,

                food_y
                + food_size // 2
            ),

            8
        )

        # ==================================================
        # DRAW POLICE
        # ==================================================

        for police in police_dogs:

            screen.blit(

                police_image,

                (
                    int(police["x"]),

                    int(police["y"])
                )
            )

        # ==================================================
        # DRAW BULLETS
        # ==================================================

        if mission >= 10:

            for bullet in bullets:

                pygame.draw.circle(

                    screen,

                    (255, 50, 50),

                    (
                        int(bullet["x"]),

                        int(bullet["y"])
                    ),

                    7
                )

        # ==================================================
        # DRAW DOG
        # ==================================================

        screen.blit(

            dog_image,

            (
                int(dog_x),

                int(dog_y)
            )
        )

        # ==================================================
        # UI
        # ==================================================

        screen.blit(

            font.render(

                f"Mission: {mission}",

                True,

                (255, 255, 255)
            ),

            (20, 20)
        )

        screen.blit(

            font.render(

                f"Food: "
                f"{food_collected}/"
                f"{food_needed}",

                True,

                (255, 255, 255)
            ),

            (20, 60)
        )

        screen.blit(

            font.render(

                f"Score: {score}",

                True,

                (255, 255, 255)
            ),

            (20, 100)
        )

        # Mission 10 warning

        if mission >= 10:

            warning = font.render(

                "WARNING: POLICE ARE SHOOTING!",

                True,

                (255, 50, 50)
            )

            screen.blit(

                warning,

                (
                    WIDTH
                    - warning.get_width()
                    - 20,

                    20
                )
            )

    # ==================================================
    # ARREST MENU
    # ==================================================

    else:

        # Dark overlay

        overlay = pygame.Surface(

            (
                WIDTH,
                HEIGHT
            )
        )

        overlay.set_alpha(220)

        overlay.fill(
            (0, 0, 0)
        )

        screen.blit(

            overlay,

            (0, 0)
        )

        # ==================================================
        # ARREST SCENE
        # ==================================================

        # Police on left

        screen.blit(

            police_image,

            (
                WIDTH // 2 - 200,

                270
            )
        )

        # Dog in middle

        screen.blit(

            dog_image,

            (
                WIDTH // 2 - 50,

                270
            )
        )

        # Police on right

        screen.blit(

            police_image,

            (
                WIDTH // 2 + 120,

                270
            )
        )

        # ==================================================
        # MENU TEXT
        # ==================================================

        arrested_text = big_font.render(

            "DOG ARRESTED!",

            True,

            (255, 255, 255)
        )

        message_text = font.render(

            "The police caught your dog!",

            True,

            (255, 255, 255)
        )

        mission_text = font.render(

            f"Mission Reached: {mission}",

            True,

            (255, 255, 255)
        )

        score_text = font.render(

            f"Score: {score}",

            True,

            (255, 255, 255)
        )

        restart_text = font.render(

            "R = Restart Game",

            True,

            (255, 255, 255)
        )

        next_text = font.render(

            "N = Next Mission",

            True,

            (255, 255, 255)
        )

        quit_text = font.render(

            "Q = Quit Game",

            True,

            (255, 255, 255)
        )

        # ==================================================
        # SHOW MENU
        # ==================================================

        screen.blit(

            arrested_text,

            (
                WIDTH // 2
                - arrested_text.get_width() // 2,

                50
            )
        )

        screen.blit(

            message_text,

            (
                WIDTH // 2
                - message_text.get_width() // 2,

                150
            )
        )

        screen.blit(

            mission_text,

            (
                WIDTH // 2
                - mission_text.get_width() // 2,

                400
            )
        )

        screen.blit(

            score_text,

            (
                WIDTH // 2
                - score_text.get_width() // 2,

                440
            )
        )

        screen.blit(

            restart_text,

            (
                WIDTH // 2
                - restart_text.get_width() // 2,

                490
            )
        )

        screen.blit(

            next_text,

            (
                WIDTH // 2
                - next_text.get_width() // 2,

                535
            )
        )

        screen.blit(

            quit_text,

            (
                WIDTH // 2
                - quit_text.get_width() // 2,

                580
            )
        )

    # ==================================================
    # UPDATE
    # ==================================================

    pygame.display.flip()

    clock.tick(60)

pygame.quit()