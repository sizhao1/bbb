import pygame
import random

# 初始化pygame
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 设置游戏标题
pygame.display.set_caption('飞机大战')

# 加载背景图片
background = pygame.image.load('images/background.png')

# 加载英雄飞机图片
hero_img = pygame.image.load('images/hero.png')

# 定义英雄飞机的位置和移动速度
hero_x = 190
hero_y = 500
hero_speed = 5

# 定义敌机的信息列表
enemy_list = []

# 加载敌机图片
enemy_img = pygame.image.load('images/enemy.png')

# 定义计时器，用于控制敌机的出现速度
clock = pygame.time.Clock()
interval = 0

# 定义敌机的类
class Enemy:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y += self.speed

# 绘制敌机
def draw_enemy(enemy):
    screen.blit(enemy_img, (enemy.x, enemy.y))

# 主函数
def main():
    global hero_x, hero_y, interval

    # 游戏循环
    while True:

        # 设置刷新帧率
        clock.tick(60)

        # 监听游戏事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 关闭窗口
                pygame.quit()
                exit()

        # 绘制背景图片
        screen.blit(background, (0, 0))

        # 绘制英雄飞机
        screen.blit(hero_img, (hero_x, hero_y))

        # 移动英雄飞机
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if hero_x > 0:
                hero_x -= hero_speed
        elif keys[pygame.K_RIGHT]:
            if hero_x < 380:
                hero_x += hero_speed
        elif keys[pygame.K_UP]:
            if hero_y > 0:
                hero_y -= hero_speed
        elif keys[pygame.K_DOWN]:
            if hero_y < 600:
                hero_y += hero_speed

        # 控制敌机的出现速度
        interval += 1
        if interval % 50 == 0:
            # 创建敌机，并添加到敌机列表中
            enemy_x = random.randint(0, 430)
            enemy_y = -68
            enemy_speed = random.randint(2, 4)
            enemy = Enemy(enemy_x, enemy_y, enemy_speed)
            enemy_list.append(enemy)

        # 绘制并移动敌机
        for enemy in enemy_list:
            draw_enemy(enemy)
            enemy.move()

        # 删除移出屏幕的敌机
        for enemy in enemy_list:
            if enemy.y > 700:
                enemy_list.remove(enemy)

        # 更新界面
        pygame.display.update()

# 启动程序
if __name__ == '__main__':
    main()
