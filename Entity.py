import pygame
import random

class MoveingObject:
    def __init__(self, screen, image, x=0, y=0):
        self.image = pygame.image.load('static/img/'+image)
        self.x, self.y = x, y
        self.speed, self.xDirection, self.yDirection = 5, 0, 0
        self.screen = screen
        self.xMin, self.xMax, self.yMin, self.yMax = 0, 735, 0, 735

    def move_left(self):
        self.xDirection = -1

    def move_right(self):
        self.xDirection = 1

    def move_up(self):
        self.yDirection = -1

    def move_down(self):
        self.yDirection = 1

    def recompute_and_draw(self):
        self.recompute_position()
        self.validate_position()
        self.draw()

    def recompute_position(self):
        self.x += self.xDirection * self.speed
        self.y += self.yDirection * self.speed

    def validate_position(self):
        self.x = self.xMin if self.x < self.xMin else self.x
        self.x = self.xMax if self.x > self.xMax else self.x
        self.y = self.yMin if self.y < self.yMin else self.y
        self.y = self.yMax if self.y > self.yMax else self.y

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def stop_horizontal_movement(self):
        self.xDirection = 0

    def stop_vertical_movement(self):
        self.yDirection = 0

class BattelShip(MoveingObject):
    def __init__(self, screen):
        super().__init__(screen, 'spaceship.png')
        self.reset()
        self.bullets = []
        for i in range(2):
            self.bullets.append(Bullet(screen))
        self.life_remaining, self.bullet_remaining = 3, 50

    def shoot(self):
        for bullet in self.bullets:
            if bullet.fire(self.x + 16):
                self.bullet_remaining -= 1
                break

    def recompute_and_draw(self):
        super().recompute_and_draw()
        for bullet in self.bullets:
            bullet.recompute_and_draw()

    def reset(self):
        self.x, self.y = 370, 480

class EnemyShip(MoveingObject):
    def __init__(self, screen):
        super().__init__(screen, 'enemy.png')
        self.reset()

    def recompute_and_draw(self):
        if self.x <= self.xMin or self.x >= self.xMax:
            self.y += 50
            self.xDirection *= -1
        super().recompute_and_draw()

    def reset(self):
        self.x, self.y = random.randint(0, 735), random.randint(0, 50)
        self.speed, self.yMax, self.xDirection = 4, 865, -1

class Bullet(MoveingObject):
    def __init__(self, screen):
        super().__init__(screen, 'bullet.png')
        self.state = 'READY'
        self.reset()

    def fire(self, x):
        if self.state == 'READY':
            self.x, self.y = x, 460
            self.yDirection = -1
            self.state = 'FIRED'
            return True
        return False

    def recompute_and_draw(self):
        if self.yDirection !=0 and self.y == self.yMin:
            self.reset()

        if self.state == 'FIRED':
            super().recompute_and_draw()

    def reset(self):
        self.x, self.y = -32, -32
        self.yDirection, self.speed, self.state = 0, 8, 'READY'
