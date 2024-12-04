import pygame
import random
import time

# Khởi tạo Pygame
pygame.init()

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Kích thước cửa sổ
width = 1920
height = 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Bắn Súng')

# Tốc độ
clock = pygame.time.Clock()
player_speed = 10
bullet_speed = 15

# Tạo nhân vật
player_width = 50
player_height = 50

# Hàm để vẽ nhân vật
def draw_player(x, y):
    pygame.draw.rect(screen, green, [x, y, player_width, player_height])

# Hàm để vẽ đạn
def draw_bullet(bullet_x, bullet_y):
    pygame.draw.rect(screen, red, [bullet_x, bullet_y, 5, 10])

# Hàm để vẽ mục tiêu
def draw_target(target_x, target_y):
    pygame.draw.circle(screen, black, (target_x, target_y), 15)

def game_loop():
    game_over = False

    # Vị trí nhân vật
    player_x = width / 2
    player_y = height - player_height - 10

    # Danh sách đạn và mục tiêu
    bullets = []
    targets = [[random.randint(20, width - 20), random.randint(20, height // 2)] for _ in range(5)]

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_width:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            bullets.append([player_x + player_width // 2, player_y])

        # Cập nhật vị trí đạn
        bullets = [[b[0], b[1] - bullet_speed] for b in bullets if b[1] > 0]

        # Kiểm tra va chạm giữa đạn và mục tiêu
        for bullet in bullets:
            for target in targets:
                if target[0] - 15 < bullet[0] < target[0] + 15 and target[1] - 15 < bullet[1] < target[1] + 15:
                    targets.remove(target)
                    bullets.remove(bullet)
                    targets.append([random.randint(20, width - 20), random.randint(20, height // 2)])
                    break

        # Vẽ mọi thứ lên màn hình
        screen.fill(white)
        draw_player(player_x, player_y)
        for bullet in bullets:
            draw_bullet(bullet[0], bullet[1])
        for target in targets:
            draw_target(target[0], target[1])

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

game_loop()
