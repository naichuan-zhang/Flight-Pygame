import os
import pygame

from plane_sprites import GameSprite

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图片
bg = pygame.image.load(os.path.join("images", "background.png"))
screen.blit(bg, (0, 0))

# 绘制飞机
hero = pygame.image.load(os.path.join("images", "me1.png"))
screen.blit(hero, (150, 500))

# 更新窗口
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机精灵
enemy = GameSprite("enemy1.png")
enemy1 = GameSprite("enemy1.png", 2)

# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 飞机向上飞行
    hero_rect.y -= 1

    if hero_rect.y <= 0:
        hero_rect.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # update - 让组中所有精灵更新位置
    enemy_group.update()
    # draw - 绘制screen上所有精灵
    enemy_group.draw(screen)

    pygame.display.update()


pygame.quit()
