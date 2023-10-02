import pygame
from balle_feu import feu
class comet:
    def __init__(self,game):
        self.pourcent = 0
        self.pourcent_speed = 6
        self.game = game
        #definir groupe de sprite pr appeler les comet
        self.cometget = pygame.sprite.Group()

        self.fall_mode = False


    def add_pourcent(self):
        self.pourcent = self.pourcent +(self.pourcent_speed /100)
        #savoir si la bar se termine ou non
    def bar_complet(self):
        return self.pourcent >= 100
    def return_pourcenta0(self):
        self.pourcent = 0

    def feu_fall(self):
        #boucle por les valeur entre 1 et 10
        for i in range(1,10) :
           self.cometget.add(feu(self))


    #essaie de faire la pluie de comet
    def essaieplui(self):
        #la jauge d'evenement est totalement chargé
        if self.bar_complet() and len(self.game.all_monstre) == 0 :
            print("pluie de comet")
            self.feu_fall()
            self.fall_mode = True # activer l'evenement

    def update_bar(self,surface):
        # ajouter des porcent
        self.add_pourcent()
        # barre noir (arriere plan)
        #(0,0,0) couleur rgb
        # [0 , s..] les x et y  || suface.get_width() = longeur de la fentre || epaisseur de la barre
        pygame.draw.rect(surface,  (0,0,0),[0, surface.get_height()-20,surface.get_width(),10])
        #bar rouge  (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [0, surface.get_height()-20, ((surface.get_width()/100)*self.pourcent), 10])

