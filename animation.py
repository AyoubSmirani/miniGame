import pygame

#definir une class qui va s'occuper d'annimation
class Animation(pygame.sprite.Sprite):
    def __init__(self, sprite_name, size=(200,200)):
        #sprite name pr definir de quelle class on va s'occuper
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0 #commencer l'anime de l'image 0
        self.images = amimations.get(sprite_name)
        self.animation = False
    #definir une methode pr déclancher l'animation
    def start_animation(self):
        self.animation = True
    def animate(self,loop=False):
      if self.animation :

        # passer a l'image suivante
        self.current_image += 1
        # verifier si on a atteind la fin de l'animation
        if self.current_image >= len(self.images) :
            #remmetre l'animation au depart
            self.current_image = 0
            if loop is False :
              #desactiver l'animation
              self.animation = False
            #modifier l'image d'animation précédente par la suivante
        self.image = self.images[self.current_image]
        self.image = pygame.transform.scale(self.image,self.size)

# definir une fonction pour charger les images
def charger_image(sprite_name):
        #charger les 24 images dans le dossier correspondant
        images = []
        # recuperer le chemin de dossier pour ce sprite
        path =f"assets/{sprite_name}/{sprite_name}"
        #boucler sur chaque image dans ce dossier
        for num in range(1,24) :
           image_path = path + str(num) + '.png'
           images.append(pygame.image.load(image_path))
        #renvoyer la liste d'image
        return images
    #definir un dictionaire qui va contenir les images chargéés de chaque sprite
amimations = { 'mummy' : charger_image('mummy'),'player' : charger_image('player'),'alien' : charger_image('alien')        }



