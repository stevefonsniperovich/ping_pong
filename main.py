from pygame import *

window_y = 900
window_x = 1400
window = display.set_mode((window_x, window_y))
background = transform.scale(image.load("background.jpg"), (window_x, window_y))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, length, width, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (length, width))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Racket(GameSprite):
    def move_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x < 0:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x > window_x -100:
            self.rect.x += self.speed
    def move_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x < 0:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x > window_x -100:
            self.rect.x += self.speed

left_racket = Racket('racket.png', 100, 100, 150, 350, 2)
right_racket = Racket('racket.png', 100, 100, 150, 350, 2)

speed_x = 4
speed_y = 2

class Ball(GameSprite):
    global speed_y, speed_x
    def update(self):
        self.rect.x += speed_x
        self.rect.y += speed_y
    def bounce(self):
        if self.rect.x >= window_x - 100 or self.rect.x <= 0:
            speed_x *= -1
        if self.rect.y >= window_y - 100 or self.rect.y <= 0:
            speed_y *= -1

ball = Ball('ball.png', 50, 50, 650, 400, 0)

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        left_racket.reset()
        left_racket.move_left()
        right_racket.reset()
        right_racket.move_right()
        ball.reset()
        ball.update()
        ball.bounce()
