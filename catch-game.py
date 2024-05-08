pip install --upgrade pygame

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 400
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Catch Game")

a = 0

pygame.mixer.music.load("dura.mp3")
pygame.mixer.music.play(-1)

# Define colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# Define player constants
player_width = 80
player_height = 20
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10
player_vel = 0  # Initial player velocity
player_acc = 0.5  # Player acceleration
player_max_vel = 10  # Maximum player velocity

# Define object constants
object_width = 40
object_height = 40
object_vel = 3
object_x = random.randint(0, window_width - object_width)
object_y = -object_height

# Game score
score = 0
font = pygame.font.Font(None, 36)

# Game over
game_over = False

# Function to handle boundary checks for the player
def handle_boundary():
    global player_x, player_vel

    if player_x < 0:
        player_x = 0
        if player_vel < 0:
            player_vel = 0
    elif player_x > window_width - player_width:
        player_x = window_width - player_width
        if player_vel > 0:
            player_vel = 0

# Function to reset the game state
def reset_game():
    global player_x, player_vel, object_x, object_y, score, game_over
    player_x = window_width // 2 - player_width // 2
    player_vel = 0
    object_x = random.randint(0, window_width - object_width)
    object_y = -object_height
    score = 0
    game_over = False

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:  # Restart the game
                reset_game()

    if not game_over:
        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Move left
            player_vel -= player_acc
        elif keys[pygame.K_d]:  # Move right
            player_vel += player_acc
        else:
            # Apply friction to gradually stop the player when no keys are pressed
            if player_vel > 0:
                player_vel -= player_acc
            elif player_vel < 0:
                player_vel += player_acc

        # Limit the player velocity
        player_vel = max(-player_max_vel, min(player_max_vel, player_vel))

        # Update player position
        player_x += player_vel

        # Handle boundary checks for the player
        handle_boundary()

        # Update object position
        object_y += object_vel + (score // 5)  # Increase falling speed every +5 score

        # Check if the object is caught
        if player_x < object_x + object_width and player_x + player_width > object_x and player_y < object_y + object_height and player_y + player_height > object_y:
            score += 1
            object_x = random.randint(0, window_width - object_width)
            object_y = -object_height

        # Check if the object falls off the screen
        if object_y > window_height:
            game_over = True

    # Draw background, player, and object
    window.fill(blue)
    pygame.draw.rect(window, white, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(window, red, (object_x, object_y, object_width, object_height))

    # Display score
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, (10, 10))

    # Game over handling
    if game_over:
        # Display final score
        final_score_text = font.render("Final Score: " + str(score), True, white)
        text_width = final_score_text.get_width()
        text_height = final_score_text.get_height()
        window.blit(final_score_text, (window_width // 2 - text_width // 2, window_height // 2 - text_height // 2))
        # Display restart message
        restart_text = font.render("Press 'R' to restart", True, white)
        restart_width = restart_text.get_width()
        restart_height = restart_text.get_height()
        window.blit(restart_text, (window_width // 2 - restart_width // 2, window_height // 2 + text_height))

    # Update the game display
    pygame.display.update()

# Quit the game
pygame.quit()