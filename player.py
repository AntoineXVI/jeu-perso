import pygame
import math

class Player(pygame.sprite.Sprite): #la plateforme
    def __init__(self):
        super().__init__()
        self.x = 600
        self.y = 600
        self.hp = 10
        self.maxHp = 10
        self.image = pygame.image.load("PygameAssets/horizontal.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image,1/8)
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        self.height = self.image.get_height()
        self.width = self.image.get_width()

    def update(self):
        if self.hp == 0:
            self.kill()

    def move_right(self):
        self.rect.x += 5

    def move_left(self):
        self.rect.x -= 5
