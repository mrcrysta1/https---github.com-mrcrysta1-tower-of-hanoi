import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 20
BALL_SPEED = 5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Ball properties
ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)
ball_y = 0
ball_dy = BALL_SPEED

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_y += ball_dy

    # Check if the ball is caught
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if (
        ball_x - BALL_RADIUS <= mouse_x <= ball_x + BALL_RADIUS
        and ball_y - BALL_RADIUS <= mouse_y <= ball_y + BALL_RADIUS
    ):
        ball_y = 0
        ball_x = random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS)

    # Draw the background
    window.fill(WHITE)

    # Draw the ball
    pygame.draw.circle(window, RED, (ball_x, int(ball_y)), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
