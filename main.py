import pygame

from Game import Game

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Invader')
game = Game(screen)

running = True
while running:
    screen.fill((0, 0, 0))          # Background Black
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.battelShip.move_left()
            elif event.key == pygame.K_RIGHT:
                game.battelShip.move_right()
            elif event.key == pygame.K_SPACE:
                game.battelShip.shoot()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                game.battelShip.stop_horizontal_movement()
    if game.is_game_over():
        game.recompute_and_draw_result()
    else:
        game.recompute_and_draw()
    pygame.display.update()

