import pygame
import math
from player import Player
from blocks import Block
from game import Game
from balle import Balle

pygame.init()
pygame.display.set_caption("Casse Briques")
screen = pygame.display.set_mode((1200,720))
my_font = pygame.font.SysFont('Comic Sans MS', 30)

clock = pygame.time.Clock()
pos = pygame.mouse.get_pos() 

# model_bullet0 = pygame.image.load("img/Bullet.png").convert_alpha()
# pause_button = pygame.image.load("img/pause.png").convert_alpha()
# pause_button = pygame.transform.scale(pause_button, (50 , 50))
# dialog = pygame.transform.scale(dialog_box , (750 , 320))
# robot_model1 = pygame.image.load("PygameAssets/alien.png").convert_alpha()
# robot_model1 = pygame.transform.scale(robot_model1, (900 , 600))


game = Game()
        
ticks = 0
run = True        
while run:
    clock.tick(30)

    if game.boutons() == -1: #pour stocker les valeurs des inputs (donc test le quit)
        run = False
    if game.pressed.get(pygame.K_ESCAPE): #si on appuie sur echap, quitter
        run = False


    if game.isMenu :  #lancement du jeu sur le menu

        intro = True
        timerIntro = pygame.time.get_ticks()
        while intro:

            if game.boutons() == -1:  #pour stocker les valeurs des inputs (donc test le quit)
                run = False
                intro = False
            if game.pressed.get(pygame.K_ESCAPE): #si on appuie sur echap, quitter
                run = False
                intro = False


            time = pygame.time.get_ticks()
            delta_time = (time - ticks) / 1000
            ticks = time


            screen.fill((0,0,0))

            pnj = pygame.image.load("Pygameassets/alien.png").convert_alpha()
            pnj = pygame.transform.scale_by(pnj, 1/3)
            dialog_box = pygame.image.load("img/dialog_box.png").convert_alpha()
            dialog_box = pygame.transform.scale(dialog_box, (400, 200))
            textMenu = my_font.render("Bienvenue, humain.", 1, pygame.Color("BLACK"))
            textMenu2 = my_font.render("Appuies sur play pour jouer.", 1, pygame.Color("BLACK"))
            play = pygame.image.load("PygameAssets/button.png")
            play_rect = play.get_rect(topleft = (325,325))
            screen.blit(pnj,(150,100))
            screen.blit(dialog_box,(350,75))
            

            if not (pygame.time.get_ticks() - timerIntro > 2000):
                screen.blit(textMenu, (420,150))
            
            else :
                screen.blit(textMenu2, (355,150))
                screen.blit(play, (325,325))
            
            result = game.boutons(1, play_rect)

            if (result == -1):
                run= False 
                intro = False
            elif (result == 1):
                intro = False
                game.isMenu = False
                print("false menu flase")
   

            pygame.display.update()
            
    else: # le jeu commence
        

        if (game.boutons() == -1):
            run = False
        if game.pressed.get(pygame.K_ESCAPE): #si on appuie sur echap, quitter
            run = False

        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 1200 - game.player.width:
            game.player.move_right()

        if game.pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0:
            game.player.move_left()

    

        screen.fill((0,0,0))
                    
        screen.blit(game.player.image,game.player.rect) #pour faire apparaitre le player => plateforme
        game.all_block.draw(screen) #pour faire apparaitre tous les block
        game.all_ball.draw(screen)  #pour faire apparaitre toutes les balles
        

        game.all_ball.update()  #pour mettre a jour les balles (déplacement/collisions) a chaque tour de boucle
        game.all_block.update()  #pour mettre a jour les blocks (collisions) a chaque tour de boucle

        pygame.display.update()


pygame.quit()