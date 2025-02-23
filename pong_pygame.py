import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball properties
ball_radius = 15
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [random.choice([3, -3]), random.choice([3, -3])]

# Paddle properties
paddle_width = 100
paddle_height = 15
paddle_pos = [WIDTH // 2 - paddle_width // 2, HEIGHT - paddle_height - 10]
paddle_speed = 10

# Score properties
score = 0
font = pygame.font.Font(None, 36)

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_pos[0] < WIDTH - paddle_width:
        paddle_pos[0] += paddle_speed

    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Ball collision with walls
    if ball_pos[0] <= ball_radius or ball_pos[0] >= WIDTH - ball_radius:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] <= ball_radius:
        ball_vel[1] = -ball_vel[1]

    # Ball collision with paddle
    if (paddle_pos[0] < ball_pos[0] < paddle_pos[0] + paddle_width and
            paddle_pos[1] < ball_pos[1] + ball_radius < paddle_pos[1] + paddle_height):
        ball_vel[1] = -ball_vel[1]
        score += 1

    # Check if ball hits the bottom
    if ball_pos[1] > HEIGHT:
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_vel = [random.choice([3, -3]), random.choice([3, -3])]
        score = 0

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    pygame.draw.rect(screen, WHITE, (paddle_pos[0], paddle_pos[1], paddle_width, paddle_height))

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()
