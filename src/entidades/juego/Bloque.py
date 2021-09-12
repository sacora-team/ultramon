import pygame

class Bloque:
    def __init__(self, imagen):

        self.ancho_bloque = 40
        self.alto_bloque = 40
        self.margen_bloque = 1
        self.imagen_bloque = imagen

    def get_ancho_bloque(self) -> None:
        return self.ancho_bloque

    def get_alto_bloque(self) -> None:
        return self.alto_bloque

    def get_margen_bloque(self) -> None:
        return self.margen_bloque

    def get_imagen_bloque(self) -> None:
        return self.imagen_bloque

    def set_imagen_bloque(self, imagen) -> None:
        self.imagen_bloque = imagen

    def transformar_escala(self) -> None:
        self.set_imagen_bloque(pygame.transform.scale(self.get_imagen_bloque,
        (self.get_ancho_bloque(), self.get_alto_bloque())))
        
bloque_pasto = Bloque("assets/relieves/pasto.png").transformar_escala()