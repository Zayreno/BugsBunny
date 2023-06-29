import pygame
import random
from configs import *

class Carrot:
    def __init__(self, img_pos):
        self.__x = random.randint(100, 1000)
        self.__y = random.randint(-500, -70)
        self.__img = Skins.CARROT[img_pos]
        self.__total_frames_img = 0
        self.__img_pos = img_pos

    def falling(self):
        self.__y += 3
        self.__total_frames_img += 1

    def respawn(self):
        if self.__y >= 340:
            self.__y = random.randint(-600, -100)

    def was_eaten(self):
        self.__y = random.randint(-600, -100)

    def draw(self, surface):
        if self.__total_frames_img == 5:
            self.__total_frames_img = 0
            self.__img_pos = (self.__img_pos + 1) % len(Skins.CARROT)

            #x = (x + 1) % 20
            #troca = not troca

            self.__img = Skins.CARROT[self.__img_pos]

        surface.blit(self.__img, [self.__x, self.__y])

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def reset(self):
        self.__x = random.randint(100, 1000)
        self.__y = random.randint(-500, -70)
