import pygame
from player import Player
from balle import Balle
from blocks import Block

class Game:
    def __init__(self):
        self.player = Player() #création du joueur => plateforme
        self.pressed = {} #dictionnaire pour stocker les valeurs des inputs

        self.all_ball =  pygame.sprite.Group() #création d'un groupe pour toutes les balles
        self.all_ball.add(Balle(600, 450,self))   #création de la balle

        self.all_block = pygame.sprite.Group() #création d'un groupe pour tous les blocks
        for x in range (0, 1200, 76):
            self.all_block.add(Block(x, 0, self, "blue")) #création d'une ligne de block
            self.all_block.add(Block(x, 16, self,"green"))
            self.all_block.add(Block(x, 32, self,"yellow"))
            self.all_block.add(Block(x, 48, self,"light_blue"))
