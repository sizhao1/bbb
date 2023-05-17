import pygame
import random

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 定义游戏屏幕大小
width = 800
height = 600

pygame.init()
# 创建游戏屏幕
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇")

clock = pygame.time.Clock()

# 定义贪吃蛇的方向
up = 0
right = 1
down = 2
left = 3

# 定义贪吃蛇的初始位置和长度
snake_list = [(200, 200), (210, 200), (220, 200)]
snake_direction = right

# 定义食物的位置
food_x = round(random.randrange(0, width - 10) / 10.0) * 10.0
food_y = round(random.randrange(0, height - 10) / 10.0) * 10.0

# 定义字体
font_style = pygame.font.SysFont(None, 50)

# 定义游戏结束函数
def end_game(score):
    message = font_style.render("Game Over! Your score is: " + str(score), True, red)
    screen.blit(message, [width / 4, height / 2])
    pygame.display.update()
    pygame.time.delay(2000)

# 定义游戏主函数
def game():
    global snake_direction, snake_list, food_x, food_y

    # 定义贪吃蛇的移动速度
    snake_speed = 15

    # 定义初始分数
    score = 0

    while True:
        # 处理游戏事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != down:
                    snake_direction = up
                elif event.key == pygame.K_DOWN and snake_direction != up:
                    snake_direction = down
                elif event.key == pygame.K_LEFT and snake_direction != right:
                    snake_direction = left
                elif event.key == pygame.K_RIGHT and snake_direction != left:
                    snake_direction = right

        # 移动贪吃蛇
        if snake_direction == up:
            head = (snake_list[0][0], snake_list[0][1] - 10)
        elif snake_direction == down:
            head = (snake_list[0][0], snake_list[0][1] + 10)
        elif snake_direction == left:
            head = (snake_list[0][0] - 10, snake_list[0][1])
        elif snake_direction == right:
            head = (snake_list[0][0] + 10, snake_list[0][1])

        # 检测是否撞墙
        if head[0] < 0 or head[0] > width - 10 or head[1] < 0 or head[1] > height - 10:
            end_game(score)
            snake_list = [(200, 200), (210, 200), (220, 200)]
            snake_direction = right
            food_x = round(random.randrange(0, width - 10) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - 10) / 10.0) * 10.0
            score = 0
            continue

        # 检测是否吃到食物
        if head[0] == food_x and head[1] == food_y:
            food_x = round(random.randrange(0, width - 10) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - 10) / 10.0) * 10.0
            score += 10
        else:
            snake_list.pop()

        snake_list.insert(0, head)

        # 绘制游戏画面
        screen.fill(black)
        pygame.draw.rect(screen, blue, [food_x, food_y, 10, 10])

        for pos in snake_list:
            pygame.draw.rect(screen, green, [pos[0], pos[1], 10, 10])

        message = font_style.render("Score: " + str(score), True, white)
        screen.blit(message, [0, 0])

        pygame.display.update()

        # 控制游戏速度
        clock.tick(snake_speed)

# 开始游戏
game()

pygame.quit()
quit()

