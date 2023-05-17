import pygame
from player import Player
from balle import Balle
from blocks import Block

class Game:
    def __init__(self):
        self.player = Player() #création du joueur => plateforme
        self.pressed = {} #dictionnaire pour stocker les valeurs des inputs
        self.isMenu = True #en lancant le jeu, on ouvr le menu

        self.all_ball =  pygame.sprite.Group() #création d'un groupe pour toutes les balles
        self.all_ball.add(Balle(600, 450,self))   #création de la balle

        self.all_block = pygame.sprite.Group() #création d'un groupe pour tous les blocks
        for x in range (0, 1200, 76):
            self.all_block.add(Block(x, 0, self, "blue")) #création d'une ligne de block
            self.all_block.add(Block(x, 16, self,"green"))
            self.all_block.add(Block(x, 32, self,"yellow"))
            self.all_block.add(Block(x, 48, self,"light_blue"))
    

    def boutons(self ,testClic = 0,rect = [0,0]):  #pour stocker les valeurs des inputs
        for event in pygame.event.get(): #recupere toutes les actions
            if event.type == pygame.QUIT: #si on ferme, quitter
                return -1

            if testClic == 1:
                if event.type == pygame.MOUSEBUTTONDOWN: #si c'est une action a la souris
                    if (pygame.mouse.get_pressed()[0]):
                        pos = pygame.mouse.get_pos()
                        if rect.collidepoint(pos): #detecte la collision entre la souris et une image
                            print("j'ai win")
                            print(pos)
                            return 1

            elif event.type == pygame.KEYDOWN:  #à chaque appuie sur une touche, met la valeur de la touche dans le dictionnaire a True
                self.pressed[event.key] = True

            elif event.type == pygame.KEYUP:  #à chaque relachement sur une touche, met la valeur de la touche dans le dictionnaire a False
                self.pressed[event.key] = False