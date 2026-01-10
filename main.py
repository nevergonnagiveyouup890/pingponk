from pygame import *
from pygame.sprite import *
from random import *

class GameSprite(Sprite):
    def __init__(self, img, xsprite, ysprite, w, h, speed):
        super().__init__()
        self.width = w
        self.height = h
        self.image = transform.scale(image.load(img), (self.width, self.height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.xsprite = xsprite
        self.ysprite = ysprite
        self.rect.x = self.xsprite
        self.rect.y = self.ysprite
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, img, xsprite, ysprite, w, h, speed):
        super().__init__(img, xsprite, ysprite, w, h, speed)
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < window_height - self.height:
            self.rect.y += self.speed
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < window_height - self.height:
            self.rect.y += self.speed
running = True
player_range_from_center = 100

clock = time.Clock()
FPS = 60


init()
#mixer.init()
#mixer.music.load("")
#mixer.music.play()

font.init()
game_font = font.Font(None, 72)

window_width = 1366
window_height = 766
window = display.set_mode((window_width, window_height))

display.set_caption("game")

background = transform.scale(
    image.load("PingPong/Backgrounds/background.png"),
    (window_width, window_height)
)

player1 = Player("PingPong/PingPong/racket.png", 0+player_range_from_center, window_height/2, 30, 100, 10)
player2 = Player("PingPong/PingPong/racket.png", window_width-player_range_from_center-30, window_height/2, 30, 100, 10)

while running:
    for event_i in event.get():
        if event_i.type == QUIT:
            running = False

    if True: 
        window.blit(background, (0, 0))

        player1.reset()
        player2.reset()

        player1.update_left()
        player2.update_right()
    clock.tick(FPS)
    display.update()
