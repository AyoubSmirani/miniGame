import pygame
import math
from game import Game
from projectile import PROJECTILE

pygame.init()
#initialiser pygame
# gener la fenete de jeu set_caption:te propose de mettre le titre de fentre et l'icone
pygame.display.set_caption("game")
# .set_mode() definir la taille de la fenetre ((langeur,largeur)...) run condition vrai creer var screen pr recuper l'iterface
screen1 = pygame.display.set_mode((1080,720))
#charger un image a un chemin spicifique
background = pygame.image.load('assets/bg.jpg')
#amaltou test bich nbadel il taswira

# impoter et charger notre menu
menu = pygame.image.load('assets/banner.png')
menu = pygame.transform.scale(menu, (500, 500))
menu_rect = menu.get_rect()
menu_rect.x = screen1.get_width() / 4
#importe et charger notre button
button = pygame.image.load('assets/button.png')
button = pygame.transform.scale(button, (400, 150))
button_rect = button.get_rect()
button_rect.x = screen1.get_width() / 3.33
button_rect.y = screen1.get_height() / 2

playerp = pygame.image.load('assets/mummy.png')
playerp_rect =  playerp.get_rect()
playerp_rect.x = 500
playerp_rect.y = 540

monstrep = pygame.image.load('assets/mummy.png')
monstrep_rect =  monstrep.get_rect()
monstrep_rect.x = 600
monstrep_rect.y = 540
# charger notre jeu
game1 = Game()



run = True
# boucle lorsque le jeux est active
while run :
    # .blit appliquer l'arriere plan de notre jeux 0=langeur 0=largeur=hauteur -200 on augmente l'hauteur
    screen1.blit(background,(0,-200))



    m = 1
    #verifier si notre jeu a commence ou non
    if game1.start == True :
       game1.lejeu(screen1,m)
    else :
    # ajouter mon ecran de bienvenue
       screen1.blit(button, button_rect)
       screen1.blit(menu,menu_rect)
       screen1.blit(playerp,playerp_rect)
    pygame.display.flip()
    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
       # recupere que cette evenement est fermeture de la fenetre
       if event.type == pygame.QUIT :
           # stopper boucle tantque
           run = False
           pygame.quit()
       # detecter si un joueur lache un touche au clavier

       elif event.type == pygame.KEYDOWN:
           game1.pressed[event.key] = True
           if event.key == pygame.K_SPACE :
               direction = 1
               game1.player.launch(120,80)

           if event.key == pygame.K_i :
               direction = 2
               game1.player.launch(0,80)

           #au cas ou la touche n'est plus utilisé
       elif event.type == pygame.KEYUP:
           game1.pressed[event.key] = False
       elif event.type == pygame.MOUSEBUTTONDOWN :
           # verification si le souris est en collisions avec le button jouer collidepoint pr recuperer l'espace sur l'ecran et est ce qu'il ya collision ou non
           if button_rect.collidepoint(event.pos) :
               #mettre le jeu en mode lancer
               game1.start_again()

