import pygame

pygame.init()

from Bloque import Bloque
from Pantalla import Pantalla

class Mapa:

    def __init__(self) -> None:
        self.mapa: bool = True
        self.grid = []
        self.pantalla = Pantalla()
        self.bloque = Bloque()

    def get_grid(self):
        return self.grid

    def set_grid(self, grid):
        self.grid = grid

    def get_pantalla(self):
        return self.pantalla

    def get_bloque(self):
        return self.bloque

    def calcular_filas(self):
        cantidad_filas = self.get_pantalla().get_ancho_pantalla() // self.get_bloque().get_ancho_bloque()
        return cantidad_filas

    def calcular_columnas(self):
        cantidad_columnas = self.get_pantalla().get_alto_pantalla() // self.get_bloque().get_alto_bloque()
        return cantidad_columnas

    def crear_grid(self):
        for fila in range(100):
            self.set_grid(self.get_grid().append([]))
            for columna in range(100):
                self.set_grid([fila].append(1))
        self.set_grid[0][0] = 1    

    def bucle(self):
        pygame.display.set_mode((self.get_pantalla().get_ancho_pantalla(), self.get_pantalla().get_alto_pantalla()))
        pygame.display.set_caption("Ultramon")

        bucle = True
        reloj = pygame.time.Clock()

        while bucle:
            pygame.mouse.set_visible(not bucle)
            self.get_pantalla().fill(self.get_pantalla().get_color_fondo())

            for fila in range(self.calcular_filas()*2):
                for columna in range(self.calcular_columnas()*2):

                    if self.get_grid()[fila][columna] == 1:
                        self.get_pantalla().blit(self.get_bloque().get_bloque_pasto(), (
                            ((self.get_bloque().get_margen_bloque() + self.get_bloque().get_ancho_bloque) * columna + self.get_bloque().get_margen_bloque()),
                            ((self.get_bloque().get_margen_bloque() + self.get_bloque().get_alto_bloque) * fila + self.get_bloque().get_margen_bloque()))
                            )

                        PASTO_RECT = self.get_bloque().get_bloque_pasto().get_rect()
                        self.get_pantalla.blit(self.get_bloque().get_bloque_pasto(), PASTO_RECT)

                    elif self.get_grid()[fila][columna] == 2:
                        self.get_pantalla.blit(self.get_bloque().get_bloque_arbol(), (
                            ((self.get_bloque().get_margen_bloque() + self.get_bloque().get_ancho_bloque) * columna + self.get_bloque().get_margen_bloque()), 
                            ((self.get_bloque().get_margen_bloque() + self.get_bloque().get_alto_bloque) * fila + self.get_bloque().get_margen_bloque()))
                            )

                        ARBOL_RECT = self.get_bloque().get_bloque_arbol().get_rect()
                        self.get_pantalla.blit(self.get_bloque().get_bloque_arbol(), ARBOL_RECT)

            reloj.tick(100)
            pygame.display.flip()

Mapa().bucle()