import pygame
pygame.init()

class Window:
    WIDTH = 1250
    HEIGHT = 470
    TITLE = "Looney Tunes"
    ICON = pygame.image.load("imgs/icon.png")

class World:
    BACKGROUND = pygame.image.load("imgs/fundo.png")
    GAMEOVER = pygame.transform.scale(pygame.image.load('imgs/defeat.png'), (1250, 470))

class Skins:
    BUGS_BUNNY = pygame.image.load("imgs/coelho.png")
    ELMER = pygame.image.load("imgs/cacador.png")
    BULLET = pygame.image.load("imgs/bullet.png")
    CARROT = [
        pygame.image.load('imgs/cenoura1.png'),
        pygame.image.load('imgs/cenoura2.png'),
        pygame.image.load('imgs/cenoura3.png'),
        pygame.image.load('imgs/cenoura4.png')
    ]
    LIVES = pygame.image.load('imgs/lives.png')
    SCORE = pygame.transform.scale(pygame.image.load('imgs/carrot.png'), (150, 80))


class Font:
    FONT = pygame.font.Font('fonts/MonomaniacOne-Regular.ttf', 50)