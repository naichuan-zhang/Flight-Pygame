import os
import random
import pygame

# 常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT       # 敌机出现定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


# 敌机创建
class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1):
        super(GameSprite, self).__init__()
        self.image = pygame.image.load(os.path.join("images", image_name))
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        super(Background, self).__init__("background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        super(Background, self).update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    def __init__(self):
        super(Enemy, self).__init__("enemy1.png")
        self.speed = random.randint(1, 3)
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self, *args):
        super(Enemy, self).update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("Enemy has been killed %s" % self.rect)


class Hero(GameSprite):
    def __init__(self):
        super(Hero, self).__init__("me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullet_group = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            self.bullet_group.add(bullet)


class Bullet(GameSprite):
    def __init__(self):
        super(Bullet, self).__init__("bullet1.png", -2)

    def update(self, *args):
        super(Bullet, self).update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("Bullet has been destroyed %s" % self.rect)