import pygame
from projectile import PROJECTILE
import animation

class Player(animation.Animation):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health=100
        self.max_health =100
        self.attack = 20
        self.velo = 4
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.all_projectiles = pygame.sprite.Group()



    def update_health_bar_player(self,surface):
        #definir couleur pour notre joje de vie le code r,g,b qui se trouve dans les sites de couleur
        bar_couleur= (210,167,6)
        #definir couleur pr l'arriere plan de la jauge
        bar_couleur2 = (52, 57, 52)
        #definir la position de notre jauge de vie ainsi que sa largeur et sa epaisseur coordonéé x,y et w=largeur et h=hauteur [x,y,w,h]
        bar_position = [self.rect.x + 50,self.rect.y +20 ,self.health,5]
        #position de l'arriere jauge remplce sante qui va changer avec sante complet qui ne change pas(l'arriere)
        bar_position2 = [self.rect.x + 50, self.rect.y + 20, self.max_health, 5]
        # dessiner l'arrier bar
        pygame.draw.rect(surface, bar_couleur2, bar_position2)
        #dessiner notre bar
        pygame.draw.rect(surface,bar_couleur,bar_position)

    def damage(self,perte):
        if self.health - perte >perte :
          self.health -= perte
        else :
          self.game.game_over()
    def update_animation(self):
     self.animate()




    def launch(self, ymin, ysar):
        projectile = PROJECTILE(self,self.game,ymin,ysar)
        self.all_projectiles.add(projectile)
        #demarer l'animation de lancer
        self.start_animation()
    def move_right(self):
        if not self.game.check_collisions(self, self.game.all_monstre):
             self.rect.x += self.velo
    def move_left(self):
        self.rect.x -= self.velo
