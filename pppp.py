from pygame import *
from random import randint
from time import time as timer

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, duz, sir, player_speed):
        super().__init__()
        
        self.image = transform.scale(image.load(player_image), (duz,sir))
        self.rect = self.image.get_rect()
        self.brzina = player_speed
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        tipke = key.get_pressed()
        if tipke[K_UP] and self.rect.y > 5:
            self.rect.y -= self.brzina
        if tipke[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.brzina
    def update_r(self):
        tipke = key.get_pressed()
        if tipke[K_w] and self.rect.y > 5:
            self.rect.y -= self.brzina
        if tipke[K_s] and self.rect.y < 400:
            self.rect.y += self.brzina

back = (181, 127, 172)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
lopta = GameSprite("donut.png",250,250,50,50,10)
iman = Player("teniser.png", 5, 5, 100, 100, 10)
merjem = Player("temiser.png", 500, 5, 100, 100, 10)
clock = time.Clock()
FPS = 60
game = True

while game: 
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False
    iman.update_r()
    merjem.update_l()
    lopta.reset()
    iman.reset()
    merjem.reset()
    display.update()
    clock.tick(FPS)