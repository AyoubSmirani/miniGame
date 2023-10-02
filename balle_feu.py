import random
import pygame

class feu(pygame.sprite.Sprite):
    def __init__(self,comet):
        super().__init__()
        self.vitesse = random.randint(1,6)
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0,800)
        self.comet = comet
        self.damage = 20
    def remove_balle(self):
        self.comet.cometget.remove(self)
        # verifier si il ya plus de boule de feu
        if len(self.comet.cometget) == 0:
            # remettre la jauge au départ
            self.comet.return_pourcenta0()
            self.comet.game.avoirmonstre('alien')
            self.comet.game.avoirmonstre('mummy')
    def feu_tombe(self):
        self.rect.y += self.vitesse
        #ne tombe pas sur le sol
        if self.rect.y >= 500 :
            print("feu")
            #retirer la boule de feu
            self.remove_balle()




        #verifier si la barre de feu touche la joueur
        if self.comet.game.check_collisions(self,self.comet.game.players) :
            # retire la boule de feu
            self.remove_balle()
            #subir 20 point de dégat
            self.comet.game.player.damage(self.damage)

