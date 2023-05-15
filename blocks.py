import pygame
import math
from balle import Balle


class Block(pygame.sprite.Sprite): #les blocks cassables
    def __init__(self,x,y, game, color):
        super().__init__()
        self.x = x
        self.y = y
        self.game = game
        self.isHit = False
        self.cooldown = True
        self.color = color
        self.image = pygame.image.load("PygameAssets/blocks/block_" + self.color +".png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(70,15))
        self.image_hit = pygame.image.load("PygameAssets/blocks/block_hit.png").convert_alpha()
        self.image_hit = pygame.transform.scale(self.image_hit,(70,15))
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        
    def update(self):
        for balle in self.game.all_ball:
            if self.rect.colliderect(balle.rect) and self.isHit == False: #si la balle touche un block , changer la couleur du block
                self.image = self.image_hit
                self.isHit = True
                balle.isDown = True
                self.cooldown = False

            if self.rect.colliderect(balle.rect) and self.cooldown and self.isHit : #si la balle touche le block une 2eme fois, detruire le block et changer le sens de la balle
                    self.kill()
                    balle.isDown = True

            if self.cooldown == False:
                self.timer = pygame.time.get_ticks()
                self.cooldown = True