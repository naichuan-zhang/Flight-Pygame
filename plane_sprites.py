import os

import pygame

# 常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60


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
    def update(self, *args):
        pass
