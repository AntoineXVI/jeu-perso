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
text_surface = my_font.render('Heheheha', False, (255, 0, 0))

width = 50
height = 50
clock = pygame.time.Clock()
pos = pygame.mouse.get_pos() 
#start = pygame.transform.scale(start , (200 , 200))
# model_enemy1 = pygame.image.load("img/wall.png").convert_alpha()
# model_bullet0 = pygame.image.load("img/Bullet.png").convert_alpha()
# pause_button = pygame.image.load("img/pause.png").convert_alpha()
# pause_button = pygame.transform.scale(pause_button, (50 , 50))
# dialog_box = pygame.image.load("img/dialog_box.png").convert_alpha()
# dialog = pygame.transform.scale(dialog_box , (750 , 320))
# robot_model1 = pygame.image.load("PygameAssets/alien.png").convert_alpha()
# robot_model1 = pygame.transform.scale(robot_model1, (900 , 600))


game = Game()
        

run = True        
while run:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #si on ferme, quitter
            run = False
        if event.type == pygame.KEYDOWN:  #à chaque appuie sur une touche, met la valeur de la touche dans le dictionnaire a True
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:  #à chaque relachement sur une touche, met la valeur de la touche dans le dictionnaire a False
            game.pressed[event.key] = False
    

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