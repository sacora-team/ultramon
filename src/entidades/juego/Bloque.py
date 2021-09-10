import pygame

class Bloque:
    def __init__(self) -> None:
        self.ancho_bloque = 45
        self.alto_bloque = 45
        self.margen_bloque = 1

    def get_ancho_bloque(self):
        return self.ancho_bloque

    def get_alto_bloque(self):
        return self.ancho_bloque

    def get_margen_bloque(self):
        return self.margen_bloque


    PASTO = pygame.image.load("assets/relieves/pasto.png")
    PASTO = pygame.transform.scale(PASTO, (get_ancho_bloque, get_alto_bloque))
    
    TIERRA = pygame.image.load("assets/relieves/tierra.png")
    TIERRA = pygame.transform.scale(TIERRA, (get_ancho_bloque, get_alto_bloque))

    AGUA = pygame.image.load("assets/relieves/agua.png")
    AGUA = pygame.transform.scale(AGUA, (get_ancho_bloque, get_alto_bloque))
    
    ARBOL = pygame.image.load("assets/ambiente/arbol.png")
    ARBOL = pygame.transform.scale(ARBOL, (get_ancho_bloque, get_alto_bloque))
