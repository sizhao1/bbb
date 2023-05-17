import pygame
import random

# 初始化Pygame
pygame.init()

# 游戏窗口的大小
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 加载游戏资源
player_img = pygame.image.load('player.png')
enemy_img = pygame.image.load('enemy.png')


# 玩家对象
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH // 2
        self.rect.y = WINDOW_HEIGHT - self.rect.height
        self.speed = 5

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed


# 敌人对象
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WINDOW_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > WINDOW_HEIGHT:
            self.kill()


# 初始化游戏窗口
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 初始化游戏时钟
clock = pygame.time.Clock()

# 初始化游戏精灵组
all_sprites = pygame.sprite.Group()

# 添加玩家对象到精灵组
player = Player()
all_sprites.add(player)

# 初始化敌人生成时间和敌人精灵组
enemy_timer = 0
enemies = pygame.sprite.Group()

# 游戏循环
running = True
while running:
    # 处理游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()

    # 更新游戏状态
    all_sprites.update()

    # 生成敌人
    enemy_timer += 1
    if enemy_timer == 60:
        enemy_timer = 0
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # 检测碰撞
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    # 绘制游戏画面
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # 控制游戏帧率
    clock.tick(60)

# 退出游戏
pygame.quit()