import pygame
import random

# 初始化 pygame
pygame.init()

# 定义常量
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 20
BG_COLOR = (50, 50, 50)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

# 创建窗口和画布
screen = pygame.display.set_mode((WIDTH, HEIGHT))
canvas = screen.copy()

# 定义贪吃蛇和食物
snake = [(WIDTH // 2, HEIGHT // 2)]
food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
        random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

# 定义方向
UP = (0, -CELL_SIZE)
DOWN = (0, CELL_SIZE)
LEFT = (-CELL_SIZE, 0)
RIGHT = (CELL_SIZE, 0)

# 定义初始方向
direction = RIGHT

# 定义时钟
clock = pygame.time.Clock()

# 定义分数
score = 0

# 定义字体
font = pygame.font.SysFont(None, 30)

# 游戏循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

    # 移动贪吃蛇
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if head == food:
        food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
        score += 10
    else:
        snake.pop()
    if head in snake:
        pygame.quit()
        quit()
    snake.insert(0, head)

    # 绘制画布
    canvas.fill(BG_COLOR)
    for cell in snake:
        pygame.draw.rect(canvas, SNAKE_COLOR, (cell[0], cell[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(canvas, FOOD_COLOR, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    score_text = font.render('Score: {}'.format(score), True, (255, 255, 255))
    canvas.blit(score_text, (10, 10))

    # 绘制窗口
    screen.blit(canvas, (0, 0))
    pygame.display.update()

    # 控制帧率
    clock.tick(10)