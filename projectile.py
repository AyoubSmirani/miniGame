import pygame
class PROJECTILE(pygame.sprite.Sprite) :
    def __init__(self, player, game, ymin, ysar):
        #ymin,ysar
        # definir le constructeur de cette class par super
        super().__init__()
        self.vitesse = 3
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.player = player
        self.game = game
        #self.direction = direction
        self.rect.x = player.rect.x + ymin
        self.rect.y = player.rect.y + ysar
        self.origin_image = self.image
        self.angle = 0
    def remove(self):
       self.player.all_projectiles.remove(self)



    def move(self,direction):
        if direction == 1 :
           self.rect.x +=self.vitesse
        else :
           self.rect.x-=self.vitesse

        for monstre in self.game.check_collisions(self, self.game.all_monstre) :
          self.remove()
          # ntaya7 il dam
          monstre.damage(self.player.attack)



        self.rotation()
        #centre la rotation en avoir le centre de l'image avec get_rect()
        self.rect = self.image.get_rect(center=self.rect.center)
         #detruire la projectile
        if self.rect.x > 1080:
            #supprimer le projectiles  (en dehors de l'ecran)
            self.remove()
        if self.rect.x < -10:
            self.remove()
    def rotation(self):
#tourner le projectile
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image,self.angle,1)
    #verifier si le projectile entre en collision avec le monstre

