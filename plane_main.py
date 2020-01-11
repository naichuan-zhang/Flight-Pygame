import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

    def start_game(self):
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __create_sprites(self):
        pass

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()

    def __check_collide(self):
        pass

    def __update_sprites(self):
        pass

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()


if __name__ == '__main__':
    PlaneGame().start_game()
