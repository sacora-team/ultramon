import pygame

from Bloque import Bloque
from Pantalla import PANTALLA

pygame.init()

class Mapa:

    def __init__(self):
        self.pantalla = PANTALLA
        self.bloque = Bloque()

    def calcular_filas(self):
        cantidad_filas = PANTALLA.get_ancho_pantalla() // Bloque.get_ancho_bloque()
        return cantidad_filas

    def calcular_columnas(self):
        cantidad_columnas = PANTALLA.get_alto_pantalla() // Bloque.get_alto_bloque()
        return cantidad_columnas

    grid = []
    for fila in range(100):
        grid.append([])
        for columna in range(100):
            grid[fila].append(1)
    grid[0][0] = 1

    pygame.display.set_mode(PANTALLA.get_ancho_pantalla, PANTALLA.get_alto_pantalla)
    pygame.display.set_caption("Ultramon")

    bucle = True
    reloj = pygame.time.Clock()

    while bucle:
        pygame.mouse.set_visible(not bucle)
        PANTALLA.get_color_fondo()

        for fila in range(calcular_filas()*2):
            for columna in range(calcular_columnas()*2):

                if grid[fila][columna] == 1:
                    PANTALLA.blit(Bloque.PASTO, (
                        ((Bloque.get_margen_bloque() + Bloque.get_ancho_bloque) * columna + Bloque.get_margen_bloque()),
                        ((Bloque.get_margen_bloque() + Bloque.get_alto_bloque) * fila + Bloque.get_margen_bloque()))
                        )

                    PASTO_RECT = Bloque.PASTO.get_rect()
                    PANTALLA.blit(Bloque.PASTO, PASTO_RECT)

                elif grid[fila][columna] == 2:
                    PANTALLA.blit(Bloque.ARBOL, (
                        ((Bloque.get_margen_bloque() + Bloque.get_ancho_bloque) * columna + Bloque.get_margen_bloque()), 
                        ((Bloque.get_margen_bloque() + Bloque.get_alto_bloque) * fila + Bloque.get_margen_bloque()))
                        )

                    ARBOL_RECT = Bloque.ARBOL.get_rect()
                    PANTALLA.blit(Bloque.ARBOL, ARBOL_RECT)

        reloj.tick(100)
        pygame.display.flip()

    pygame.quit()