import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 30
gravity = 1
bird_speed = -10
jump_sound = pygame.mixer.Sound("jump.mp3")
collision_sound = pygame.mixer.Sound("collision.mp3")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images with adjusted sizes
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
bird_image = pygame.image.load('bird.png')
bird_image = pygame.transform.scale(bird_image, (50, 50))  # Adjust size
pipe_image = pygame.image.load('pipe.png')
pipe_image = pygame.transform.scale(pipe_image, (50, 300))  # Adjust size
pipe2_image = pygame.image.load('pipe2.png')
pipe2_image = pygame.transform.scale(pipe2_image, (50, 300))  # Adjust size

# Clock to control the frame rate
clock = pygame.time.Clock()

# Bird
bird_x = 100
bird_y = HEIGHT // 2
bird_y_change = 0

# Pipes
pipe_width = 50
pipe_height = 300
pipe_x = WIDTH
pipe_gap = 80  # Reduced the gap
pipe_speed = 5
speed_increase_interval = 5  # Increase speed every 5 points
speed_increase_amount = 1  # Increase speed by 1 unit

# Score
score = 0

# Game state
game_over = False
game_started = False
paused = False

def bird(y):
    screen.blit(bird_image, (bird_x, y))

def pipes(x, gap):
    screen.blit(pipe2_image, (x, gap - pipe_height))
    screen.blit(pipe_image, (x, gap + pipe_gap))

def show_score(score, x, y):
    font = pygame.font.Font('freesansbold.ttf', 24)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (x, y))

def game_over_text():
    font = pygame.font.Font('freesansbold.ttf', 32)
    over_text = font.render("Game Over", True, WHITE)
    screen.blit(over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

def final_score_text(score):
    font = pygame.font.Font('freesansbold.ttf', 24)
    final_score_text = font.render("Your Score: " + str(score), True, WHITE)
    screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2))

def start_menu():
    font = pygame.font.Font('freesansbold.ttf', 32)
    start_text = font.render("Press SPACE to Start", True, WHITE)
    pause_text = font.render("Press P to Pause", True, WHITE)  # New line
    screen.blit(start_text, (WIDTH // 2 - 150, HEIGHT // 2 - 25))
    screen.blit(pause_text, (WIDTH // 2 - 120, HEIGHT // 2 + 25))  # New line

def again_exit_menu():
    font = pygame.font.Font('freesansbold.ttf', 24)
    again_text = font.render("Press A to Play Again | Press Q to Quit", True, WHITE)
    screen.blit(again_text, (WIDTH // 2 - 200, HEIGHT // 2 + 50))

def pause_menu():
    font = pygame.font.Font('freesansbold.ttf', 24)
    pause_text = font.render("Game Paused | Press P to Resume", True, WHITE)
    screen.blit(pause_text, (WIDTH // 2 - 200, HEIGHT // 2))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_started:
                    game_started = True
                elif not game_over:
                    bird_y_change = bird_speed
                    jump_sound.play()
            elif event.key == pygame.K_a and game_over:
                # Play again
                bird_y = HEIGHT // 2
                game_over = False
                pipe_x = WIDTH
                score = 0
                pipe_speed = 5  # Reset pipe speed
            elif event.key == pygame.K_q and game_over:
                # Quit
                running = False
            elif event.key == pygame.K_p and not game_over:
                # Pause/unpause
                paused = not paused

    if not game_started:
        # Display start menu
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        start_menu()
    elif not game_over and not paused:
        bird_y += bird_y_change

        # Check if the bird hits the ground or the top
        if bird_y > HEIGHT or bird_y < 0:
            collision_sound.play()
            game_over_text()
            final_score_text(score)
            game_over = True
            bird_y_change = 0
            again_exit_menu()

        # Move pipes
        pipe_x -= pipe_speed
        if pipe_x < -pipe_width:
            pipe_x = WIDTH
            pipe_gap = random.randint(50, HEIGHT - 150)  # Ajuste en la generación de tubos
            score += 1

            # Increase speed every specified interval
            if score % speed_increase_interval == 0:
                pipe_speed += speed_increase_amount

        # Check for collisions with pipes
        if pipe_x < bird_x < pipe_x + pipe_width:
            if bird_y < pipe_gap or bird_y > pipe_gap + pipe_gap + 50:
                collision_sound.play()
                game_over_text()
                final_score_text(score)
                game_over = True
                bird_y_change = 0
                again_exit_menu()

        # Apply gravity
        bird_y_change += gravity

        # Draw background
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Draw bird
        bird(bird_y)

        # Draw pipes
        pipes(pipe_x, pipe_gap)

        # Draw score
        show_score(score, 10, 10)

    else:
        # Display game over or pause menu
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        if not paused:
            game_over_text()
            final_score_text(score)
            again_exit_menu()
        else:
            pause_menu()

    pygame.display.update()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
