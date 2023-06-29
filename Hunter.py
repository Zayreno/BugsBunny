from Bullet import Bullet
from configs import *

class Hunter:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__img = Skins.ELMER
        self.__bullets = []
        self.__total_shoot_frames = 0

    def get_overlaping_area(self, image, offset_x, offset_y):
        self_mask = pygame.mask.from_surface(self.__img)
        who_mask = pygame.mask.from_surface(image)
        return who_mask.overlap_area(self_mask, [self.__x - offset_x, self.__y - offset_y])

    def colides_with(self, who):
        return who.get_overlaping_area(self.__img, self.__x, self.__y) > 0

    def draw(self, surface):
        surface.blit(self.__img, [self.__x, self.__y])

    def shoot_if_ready(self):
        self.__total_shoot_frames += 1
        if self.__total_shoot_frames == 120:
            self.__bullets.append(Bullet(self.__x - 5, self.__y + 68))
            self.__total_shoot_frames = 0

    def move_shootings(self):
        for bullet in self.__bullets:
            bullet.move()

            if bullet.is_out():
                self.__bullets.remove(bullet)

    #novo metodo
    def hits(self, rabbit):
        for bullet in self.__bullets:
            if bullet.colides_with(rabbit):
                self.__bullets.remove(bullet)
                return True

        return False

    def draw_shootings(self, surface):
        for bullet in self.__bullets:
            bullet.draw(surface)

    def reset(self):
        self.__bullets = []

