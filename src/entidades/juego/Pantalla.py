import pygame


class Pantalla(pygame.Surface):
    def __init__(self) -> None:
        self.ancho_pantalla = pygame.display.Info().current_w
        self.alto_pantalla = pygame.display.Info().current_h
        self.color_fondo = (0,0,0)
        super().__init__((self.get_ancho_pantalla(), self.get_alto_pantalla()))

    def get_ancho_pantalla(self):
        return self.ancho_pantalla

    def get_alto_pantalla(self):
        return self.alto_pantalla

    def get_color_fondo(self):
        return self.color_fondo

    def dimension_pantalla(self):
        return (self.get_ancho_pantalla(), self.get_alto_pantalla())
