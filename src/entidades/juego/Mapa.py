import pygame

from .Bloque import Bloque


pygame.init()

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)

class Mapa:

    def __init__(self):
        self.ancho_pantalla = pygame.display.Info().current_w
        self.alto_pantalla = pygame.display.Info().current_h
        self.bloque = Bloque()

    def get_ancho_pantalla(self):
        return self.ancho_pantalla

    def get_alto_pantalla(self):
        return self.alto_pantalla


    def calcular_filas(self):
        cantidad_filas = self.get_ancho_pantalla // Bloque.get_ancho_bloque
        return cantidad_filas

    def calcular_columnas(self):
        cantidad_columnas = self.get_alto_pantalla // Bloque.get_alto_bloque
        return cantidad_columnas


    grid = []

    for fila in range(100):
        grid.append([])
        for columna in range(100):
            grid[fila].append(1)

    grid[0][0] = 1

    DIMENSION_VENTANA = [get_ancho_pantalla, get_alto_pantalla]
    pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
    pygame.display.set_caption("Mapa")

    bucle = True
    reloj = pygame.time.Clock()

    while bucle:
        pygame.mouse.set_visible(not bucle)
        pantalla.fill(NEGRO)

        for fila in range(calcular_filas()*2):
            for columna in range(calcular_columnas()*2):

                if grid[fila][columna] == 1:
                    pantalla.blit(Bloque.PASTO, (
                        ((Bloque.get_margen_bloque + Bloque.get_ancho_bloque) * columna + Bloque.get_margen_bloque),
                        ((Bloque.get_margen_bloque + Bloque.get_alto_bloque) * fila + Bloque.get_margen_bloque)))

                    PASTO_RECT = Bloque.PASTO.get_rect()
                    pantalla.blit(Bloque.PASTO, PASTO_RECT)

                elif grid[fila][columna] == 2:
                    pantalla.blit(Bloque.ARBOL, (
                        ((Bloque.get_margen_bloque + Bloque.get_ancho_bloque) * columna + Bloque.get_margen_bloque), 
                        ((Bloque.get_margen_bloque + Bloque.get_alto_bloque) * fila + Bloque.get_margen_bloque)))

                    ARBOL_RECT = Bloque.ARBOL.get_rect()
                    pantalla.blit(Bloque.ARBOL, ARBOL_RECT)

        reloj.tick(100)
        pygame.display.flip()

    pygame.quit()