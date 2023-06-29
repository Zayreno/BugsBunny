from Rabbit import Rabbit
from Hunter import Hunter
from Carrot import *

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((Window.WIDTH, Window.HEIGHT))
pygame.display.set_caption(Window.TITLE)
pygame.display.set_icon(Window.ICON)

carrots = [
    Carrot(0),
    Carrot(1),
    Carrot(2),
    Carrot(3)
]

background_sound = pygame.mixer.Sound("sounds/nature.ogg")
background_sound.play(loops=-1)
background_sound.set_volume(0.2)

bugs_bunny = Rabbit(10, 200)
elmer = Hunter(1100, 280)


score = 0
clock = pygame.time.Clock()
game_state = 'game'
while True:
    dt = clock.tick(60)

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    score_text = Font.FONT.render(F'{score}', True, (255, 255, 255))

    if game_state == 'gameover':
        if key[pygame.K_SPACE]:
            game_state = 'game'
            bugs_bunny.reset()
            elmer.reset()
            for carrot in carrots:
                carrot.reset()
            score = 0

    if game_state == 'gameover':
        screen.blit(World.GAMEOVER, (0, 0))
    elif game_state == 'game':
        screen.blit(World.BACKGROUND, [0, 0])

        if key[pygame.K_a] or key[pygame.K_LEFT]:
            bugs_bunny.move_left()
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            bugs_bunny.move_right()

        if key[pygame.K_w] or key[pygame.K_UP]:
            bugs_bunny.jump()

        bugs_bunny.update_jump()

        bugs_bunny.draw(screen)

        elmer.shoot_if_ready()
        elmer.move_shootings()
        if elmer.hits(bugs_bunny):
            bugs_bunny.lose_lives()

        if bugs_bunny.colides_with(elmer):
            game_state = 'gameover'

        elmer.draw_shootings(screen)
        elmer.draw(screen)

        for life in range(bugs_bunny.remaining_lives()):
            screen.blit(Skins.LIVES, [life * 55, 0])

        screen.blit(Skins.SCORE, [1100, 0])
        screen.blit(score_text, [1100 + ((Skins.SCORE.get_width() - score_text.get_width()) / 2), 0])

        for carrot in carrots:
            carrot.draw(screen)
            carrot.falling()
            carrot.respawn()
            if bugs_bunny.colides_with(carrot):
                carrot.was_eaten()
                score += 1

        if bugs_bunny.remaining_lives() == 0:
            game_state = 'gameover'

    pygame.display.update()

pygame.quit()
