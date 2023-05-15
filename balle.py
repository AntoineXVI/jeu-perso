import pygame
import math
from player import Player

class Balle(pygame.sprite.Sprite): #la balle qui rebondit
    def __init__(self,x,y,game):
        super().__init__()
        self.x = x
        self.y = y
        self.game = game
        self.vitesse = 5
        self.isDown = True #si la balle descend
        self.image = pygame.image.load("img/balle.png").convert_alpha()
        self.image = pygame.transform.scale_by(self.image,1/10)
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        self.height = self.image.get_height()
        self.width = self.image.get_width()

    def update(self):
        if self.isDown == True:
            self.rect.y += self.vitesse
        elif self.isDown == False:
            self.rect.y -= self.vitesse

        if self.rect.y > 720 - self.height: #si la balle sors de l'écran, detruire
            self.kill()
        if self.rect.y < 0:
            self.kill()
            
        if self.rect.colliderect(self.game.player.rect): #si la balle touche la plateforme, changer le sens de déplacement y
            self.isDown = False