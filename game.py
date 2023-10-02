import pygame
from player import Player
from monst import Monstre, MUMMY, Alien
from comet_event import comet


class Game:

    def __init__(self):
        self.start = False
        self.players = pygame.sprite.Group()
        self.all_monstre = pygame.sprite.Group()
        self.player = Player(self)
        #gener l'evenement
        self.comet = comet(self)
        self.players.add_internal(self.player)
        self.pressed = {}

# start again pr redemare les monstre
    def start_again(self):
        self.start = True
        self.avoirmonstre(MUMMY)
        self.avoirmonstre(Alien)

    def avoirmonstre(self,Monstre_class_name):
        self.all_monstre.add(Monstre_class_name.__call__(self))


    def check_collisions(self, sprite, group):
          return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)



    def game_over(self):
        #remettre le jeu neuf,retirer les monstres,remmetre les joueur à 100 de vie,jeu en attente
        self.all_monstre = pygame.sprite.Group()
        # bich tfas5 les comets et les remettre a 0
        self.comet.cometget = pygame.sprite.Group()
        self.comet.return_pourcenta0()
        self.player.health = self.player.max_health
        self.start = False



    def  lejeu(self,screen1,direction):
       # ce code été mis aprés le boucle while en main on a deplacer pr la lisibilité
       # mettre a jour le joueur

       screen1.blit(self.player.image, self.player.rect)
       # actualiser la bar de vie de joueur
       self.player.update_health_bar_player(screen1)
       #actualiser l'animation de joueur
       self.player.update_animation()
       # actualise la barre d'evenement de jeux
       self.comet.update_bar(screen1)


       # recuperer les projectiles de joueur
       for projectile in self.player.all_projectiles:
          projectile.move(direction)

       self.player.all_projectiles.draw(screen1)
       # appliquer l'ensemble des images des monstre draw pr dessiner sur ecran
       # appliquer l'ensemble des images des projectile draw pr dessiner sur ecran
       for Monstre in self.all_monstre:
          # if Monstre.rect.x != game1.player.rect.x :
          Monstre.move()
          # le boucle qui fait marcher le monstre on le rajoute le couleur
          Monstre.update_health_bar(screen1)
          Monstre.update_animation()
          print(Monstre.rect.x)
          print(self.player.rect.x)
       # recuperer les comet=feu
       for comet in self.comet.cometget:
           comet.feu_tombe()


       self.all_monstre.draw(screen1)
       # appliquer les images de mn group monstre
       self.comet.cometget.draw(screen1)




       # récupérer si le joueur veut aller vers la gauche ou la droit
       if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 880:
           self.player.move_right()
       elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
          self.player.move_left()

