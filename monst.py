import pygame
import random
import animation
class Monstre(animation.Animation):
    def __init__(self, game, name, size):
        super().__init__(name,size)  # rect y
        self.game = game
        self.vitesse = random.randint(1,3)
        self.sante = 100
        self.sante_complet = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)   # choisir un nombre aléa qui permet se ne pas mettre tout les monstre dans les meme cordoneé
        self.rect.y = 540
        self.start_animation()

    def damage(self,pertevie):
        #infliger les degats
        self.sante -= pertevie
        # verifier si son nombre de points de vie est inferieur ou egal a 0 il va reparaitre a nouveau
        if self.sante <= 0 :
            self.rect.x = 1000 + random.randint(0,200)
            self.vitesse = random.randint(1,3)
            self.sante = 100

        # verifier si la barre de jeux est chargé au max
        if self.game.comet.bar_complet() :

              #retire les monstres
              self.game.all_monstre.remove(self)
              self.game.comet.essaieplui()
              ##self.game.comet.fall_mode = True


    def update_animation(self):
         self.animate(True)







    def update_health_bar(self,surface):
        #definir couleur pour notre joje de vie le code r,g,b qui se trouve dans les sites de couleur
        bar_couleur= (210,167,6)
        #definir couleur pr l'arriere plan de la jauge
        bar_couleur2 = (52, 57, 52)
        #definir la position de notre jauge de vie ainsi que sa largeur et sa epaisseur coordonéé x,y et w=largeur et h=hauteur [x,y,w,h]
        bar_position = [self.rect.x + 10,self.rect.y -20 ,self.sante,5]
        #position de l'arriere jauge remplce sante qui va changer avec sante complet qui ne change pas(l'arriere)
        bar_position2 = [self.rect.x + 10, self.rect.y - 20, self.sante_complet, 5]
        # dessiner l'arrier bar
        pygame.draw.rect(surface, bar_couleur2, bar_position2)
        #dessiner notre bar
        pygame.draw.rect(surface,bar_couleur,bar_position)


    def move(self):
        if not self.game.check_collisions(self, self.game.players):
            self.rect.x -= self.vitesse
        else :
            self.game.player.damage(self.attack)



# definir class pr l'alien
class Alien(Monstre):
    def __init__(self,game):
        super().__init__(game,"alien",(150,150))

# definir class pr le mummy
class MUMMY(Monstre):
    def __init__(self,game):
        super().__init__(game,"mummy",(150,150))







