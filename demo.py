import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.5
LIFT = -10
PIPE_WIDTH = 70
PIPE_GAP = 150

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Bird class
class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.width = 30
        self.height = 30
        self.velocity = 0

    def flap(self):
        self.velocity += LIFT

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.top = random.randint(50, HEIGHT - PIPE_GAP - 50)
        self.bottom = HEIGHT - (self.top + PIPE_GAP)
        self.width = PIPE_WIDTH

    def update(self):
        self.x -= 3

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, 0, self.width, self.top))
        pygame.draw.rect(screen, GREEN, (self.x, HEIGHT - self.bottom, self.width, self.bottom))

    def collides(self, bird):
        if (bird.x + bird.width > self.x and bird.x < self.x + self.width):
            if bird.y < self.top or bird.y + bird.height > HEIGHT - self.bottom:
                return True
        return False

# Game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = []
    score = 0
    running = True
    spawn_pipe_timer = 0

    while running:
        screen.fill(WHITE)
        bird.update()
        bird.draw(screen)

        # Spawn pipes
        spawn_pipe_timer += 1
        if spawn_pipe_timer > 100:
            pipes.append(Pipe())
            spawn_pipe_timer = 0

        for pipe in pipes:
            pipe.update()
            pipe.draw(screen)

            if pipe.collides(bird):
                running = False

            if pipe.x + PIPE_WIDTH < 0:
                pipes.remove(pipe)
                score += 1

        # Draw score
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(text, (10, 10))

        # Check for bird collision with the ground or ceiling
        if bird.y > HEIGHT or bird.y < 0:
            running = False

        pygame.display.flip()
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

    pygame.quit()

if __name__ == "__main__":
    main()