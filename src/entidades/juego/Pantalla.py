import pygame
from constantes.colores import Colores

class Pantalla:
    def __init__(self):
        self.ancho_pantalla = pygame.display.Info().current_w
        self.alto_pantalla = pygame.display.Info().current_h
        self.color_fondo = pygame.fill(Colores.NEGRO)

    def get_ancho_pantalla(self):
        return self.ancho_pantalla

    def get_alto_pantalla(self):
        return self.alto_pantalla

    def get_color_fondo(self):
        return self.color_fondo

    def dimension_pantalla(self):
        return (self.get_ancho_pantalla(), self.get_alto_pantalla())

PANTALLA = Pantalla()