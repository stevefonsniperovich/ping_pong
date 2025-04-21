from pygame import *

window_y = 900
window_x = 1400
window = display.set_mode((window_x, window_y))
background = transform.scale(image.load("background.jpg"), (window_x, window_y))

class GameSprite(sprite.Sprite):
    def __init__(self, image, length, width, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image), (length, width))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.rect, (self.rect.x, self.rect.y))
    
class racket(GameSprite):
    def move_left(self):
        key = key.get_pressed()
            if key == Key_W and self.rect.x <:

finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
