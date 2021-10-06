import pygame 
import random

pygame.init()

# Pantalla - Ventana

W, H = 1280, 720
PANTALLA = pygame.display.set_mode((W, H), pygame.RESIZABLE)


class Entrenadores:
    
    def __init__(self):
        
        self.posY = 600
        self.posX = 600
        self.ejecutar = True
        self.entrenador = ''
        self.nroEntrenador = random.randint(1, 5)

        self.pokeTrainer = ()

    def getPosY(self):
        return self.posY
        
    def getPosX(self):
        return self.posX    
    def defineEntrenador(self):
    
        if self.nroEntrenador == 1:
            self.entrenador = 'monica'
           
        elif self.nroEntrenador == 2:
            self.entrenador = 'pedro'
           
        elif self.nroEntrenador == 3:
            self.entrenador = 'juan'
        
        elif self.nroEntrenador == 4:
            self.entrenador = 'joaco'
               
        elif self.nroEntrenador == 5:
            self.entrenador = 'pepa'
    

    def getSprite(self):

        if self.nroEntrenador == 1:
            self.sprite = pygame.image.load("assets/personajes/maestros/a1.png")

        elif self.nroEntrenador == 2:
            self.sprite = pygame.image.load("assets/personajes/maestros/b1.png")

        elif self.nroEntrenador == 3:
            self.sprite = pygame.image.load("assets/personajes/maestros/c1.png")

        elif self.nroEntrenador == 4:
            self.sprite = pygame.image.load("assets/personajes/maestros/d1.png")

        else:
            self.sprite = pygame.image.load("assets/personajes/maestros/e1.png")

        return self.sprite
        
    def pokemonTrainer(self):

        if self.nroEntrenador == 1:
            self.pokeTrainer = ("bulbasur02","gato03","pajarito03")
            
        elif self.nroEntrenador == 2:
            self.pokeTrainer = ("charmander03","gusanito02","pez02")

        elif self.nroEntrenador == 3:
            self.pokeTrainer = ("monstruo02","pajarito","pajarito03")

        elif self.nroEntrenador == 4:
            self.pokeTrainer = ("sapo03","ratoide02","pepapig02")

        else:
            self.pokeTrainer = ("vamoacalmarno03","pikachu02","charmander03")

        return self.pokeTrainer

   
    def ejecucion(self):
        while self.ejecutar:
            for evento in pygame.event.get(): 
                if evento.type == pygame.QUIT: 
                    self.ejecutar = False   
    
            PANTALLA.blit(self.getSprite(),(self.getPosY(), self.getPosX()))
            pygame.display.flip()


aa = Entrenadores()
aa.defineEntrenador()
print(aa.pokemonTrainer())

print(aa.entrenador)
aa.ejecucion()  
aa.getSpritePokemon()
    

        
        