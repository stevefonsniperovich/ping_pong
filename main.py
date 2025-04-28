from pygame import *
from time import time
font.init()

font = font.Font(None, 100)
counter_1 = 0
counter_2 = 0
win1 = font.render('Player 1 wins', True, (220, 220, 0))
win2 = font.render('Player 2 wins', True, (220, 220, 0))
goals1 = font.render(str(counter_1), True, (255, 255, 255))
goals2 = font.render(str(counter_2), True, (255, 255, 255))
game_starting = font.render('starting one more game...', True, (255, 0, 0))
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
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_y -150:
            self.rect.y += self.speed
    def move_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_y -150:
            self.rect.y += self.speed

left_racket = Racket('racket.png', 100, 150, 150, 350, 3)
right_racket = Racket('racket.png', 100, 150, 1200, 350, 3)

speed_x = 4
speed_y = 2

class Ball(GameSprite):
    global speed_y, speed_x
    def update(self):
        self.rect.x += speed_x
        self.rect.y += speed_y

ball = Ball('ball.png', 50, 50, 650, 400, 2)

finish = False
game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        window.blit(goals1, (0, 0))
        window.blit(goals2, (0, 0))
        left_racket.reset()
        left_racket.move_left()
        right_racket.reset()
        right_racket.move_right()
        ball.reset()
        ball.update()
        if ball.rect.y > window_y - 100 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(ball, left_racket) or sprite.collide_rect(ball, right_racket):
            speed_x *= -1
        clock.tick(FPS)
        display.update()
    if ball.rect.x > window_x or ball.rect.x < -100:
        finish = True
        start_time = time
        end_time = 0
        while end_time - start_time < 5:
            end_time = time()
            if ball.rect.x > window_x:
                window.blit(win1, (650, 400))
            if ball.rect.x < -100:
                window.blit(win2, (650, 400))
            window.blit(game_starting, (600, window_y - 100))
        finish = False
