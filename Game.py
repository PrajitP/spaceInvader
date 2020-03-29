import math
import pygame

from Entity import BattelShip, EnemyShip

class Game:
    def __init__(self, screen, enemy_count=3):
        self.screen = screen
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.battelShip = BattelShip(screen)
        self.enemyShips = []
        for i in range(enemy_count):
            self.enemyShips.append(EnemyShip(screen))
        self.score = 0

    def recompute_and_draw(self):
        self.battelShip.recompute_and_draw()
        for enemyShip in self.enemyShips:
            enemyShip.recompute_and_draw()
            for bullet in self.battelShip.bullets:
                if self.has_collision(enemyShip, bullet):
                    self.score += 1
                    bullet.reset()
                    enemyShip.reset()
            if enemyShip.y >= 480:
                self.battelShip.life_remaining -= 1
                enemyShip.reset()
        self.recompute_and_draw_score()

    def is_game_over(self):
        if self.battelShip.life_remaining <= 0 or self.battelShip.bullet_remaining <= 0:
            return True
        elif self.score >= 20:
            return True
        else:
            return False

    def recompute_and_draw_result(self):
        if self.score >= 20:
            self.render_success()
        else:
            self.render_failure()

    def render_success(self):
        score_board = self.font.render("You Won", True, (255,255,255))
        self.screen.blit(score_board, (340, 240))

    def render_failure(self):
        score_board = self.font.render("Game Over", True, (255,255,255))
        self.screen.blit(score_board, (340, 240))

    def recompute_and_draw_score(self):
        score = "{} Kill : {} Bullet : {} Life".format(self.score,\
                                                       self.battelShip.bullet_remaining,\
                                                       self.battelShip.life_remaining)
        score_board = self.font.render(score, True, (255,255,255))
        self.screen.blit(score_board, (5, 5))

    def has_collision(self, obj1, obj2):
        distance = math.sqrt((math.pow(obj2.x - obj1.x, 2)) + (math.pow(obj2.y - obj1.y, 2)))
        if distance < 32:
            return True
        else:
            return False