import pygame
from Orientation import *
from configs import *

class Rabbit:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = Skins.BUGS_BUNNY
        self.__initial_y = y
        self.__jump_state = None
        self.__lives = 3
        #self.__total_jump_frames = 0

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def move_left(self):
        self.__x -= 5

        if self.__x < 10:
            self.__x = 10

    def lose_lives(self):
        self.__lives -= 1

    def remaining_lives(self):
        return self.__lives

    def reset(self):
        self.__lives = 3
        self.__x = 10
        self.__y = 200

    def move_right(self):
        self.__x += 5

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def jump(self):
        if self.__jump_state != None:
            return

        self.__jump_state = Direction.RISING

    def update_jump(self):
        if self.__jump_state == Direction.RISING:
            self.__y -= 5
            if self.__y <= 80:
                self.__jump_state = Direction.FALLING
        elif self.__jump_state == Direction.FALLING:
            self.__y += 5
            if self.__y >= self.__initial_y:
                self.__jump_state = None




