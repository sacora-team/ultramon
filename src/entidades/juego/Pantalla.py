import pygame

class Pantalla:
    def __init__(self):
        self.ancho_pantalla = pygame.display.Info().current_w
        self.alto_pantalla = pygame.display.Info().current_h

    def get_ancho_pantalla(self):
        return self.ancho_pantalla

    def get_alto_pantalla(self):
        return self.alto_pantalla

    def dimension_pantalla(self):
        return (self.get_ancho_pantalla(), self.get_alto_pantalla())