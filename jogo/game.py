from pygame import display
from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale

screen_size = (800, 600)


class Personagem(Sprite):
    def __init__(self):
        super().__init__(self)
        self.image = load('image/dunofausto_small.png')
        self.rect = self.image.get_rect()


class Torrada:
    def __init__(self):
        super().__init__(self)
        self.image = load('image/torrada_small.png')
        self.rect = self.image.get_rect()


class
dunofausto = Personagem()
while True:
    superficie = display.set_mode(screen_size)
    display.set_caption("Jogo teste.")
    background = scale(
        load('images/space.jpg'),
        screen_size
    )
    superficie.blit(
        background,
        (0, 0)
    )
    display.update()
