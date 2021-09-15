import pygame
import random

pygame.init()

class Mapa:
    def __init__(self):
        self.ancho_pantalla: int = pygame.display.Info().current_w
        self.alto_pantalla: int = pygame.display.Info().current_h

        self.ancho_bloque: int = 40
        self.alto_bloque: int = 40
        self.margen_bloque: int = 1

        self.cantidad_filas: float = (self.alto_pantalla / self.alto_bloque)
        self.cantidad_columnas: float = (self.ancho_pantalla / self.ancho_bloque)

        # TODO Hacer que los bloques se creen en base a al tamaño de la pantalla.

        self.dimension_pantalla: tuple = [self.ancho_pantalla - self.cantidad_filas , self.alto_pantalla - self.cantidad_columnas]

    def get_ancho_pantalla(self) -> None:
        return self.ancho_pantalla
    
    def get_alto_pantalla(self) -> None:
        return self.alto_pantalla

    def get_ancho_bloque(self) -> None:
        return self.ancho_bloque

    def get_alto_bloque(self) -> None:
        return self.alto_bloque

    def get_margen_bloque(self) -> None:
        return self.margen_bloque

    def get_cantidad_filas(self) -> None:
        return self.cantidad_filas

    def get_cantidad_columnas(self) -> None:
        return self.cantidad_columnas

    def get_dimension_pantalla(self) -> None:
        return self.dimension_pantalla

mapa = Mapa()

PASTO = pygame.image.load("assets/relieves/pasto.png")
PASTO = pygame.transform.scale(PASTO, (mapa.get_ancho_bloque(), mapa.get_alto_bloque()))
TIERRA = pygame.image.load("assets/relieves/tierra.png")
TIERRA = pygame.transform.scale(TIERRA, (mapa.get_ancho_bloque(), mapa.get_alto_bloque()))
AGUA = pygame.image.load("assets/relieves/agua.png")
AGUA = pygame.transform.scale(AGUA, (mapa.get_ancho_bloque(), mapa.get_alto_bloque()))

print(mapa.get_cantidad_columnas())
grid = []
for fila in range(mapa.get_cantidad_filas()):
    grid.append([])
    for columna in range(mapa.get_cantidad_columnas()):
        grid[fila].append(0)

for fila in range(1):
    for columna in range(0, mapa.get_cantidad_columnas()):
        grid[fila][columna] = 2


pantalla = pygame.display.set_mode(mapa.get_dimension_pantalla())
pygame.display.set_caption("Ultramon")

bucle = True
reloj = pygame.time.Clock()

while bucle:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            bucle = False

    pantalla.fill((0,0,0))

    for fila in range(mapa.get_cantidad_filas()):
        for columna in range(mapa.get_cantidad_columnas()):
            if grid[fila][columna] == 0:
                pantalla.blit(PASTO, (
                    ((mapa.get_margen_bloque() + mapa.get_ancho_bloque()) * columna),
                    ((mapa.get_margen_bloque() + mapa.get_alto_bloque()) * fila))
                    )

                PASTO_RECT = PASTO.get_rect()
                pantalla.blit(PASTO, PASTO_RECT)

            elif grid[fila][columna] == 1:
                pantalla.blit(TIERRA, (
                    ((mapa.get_margen_bloque() + mapa.get_ancho_bloque()) * columna),
                    ((mapa.get_margen_bloque() + mapa.get_alto_bloque()) * fila))
                    )

                TIERRA_RECT = TIERRA.get_rect()
                pantalla.blit(TIERRA, TIERRA_RECT)

            elif grid[fila][columna] == 2:
                pantalla.blit(AGUA, (
                    ((mapa.get_margen_bloque() + mapa.get_ancho_bloque()) * columna),
                    ((mapa.get_margen_bloque() + mapa.get_alto_bloque()) * fila))
                    )

                AGUA_RECT = AGUA.get_rect()
                pantalla.blit(AGUA, AGUA_RECT)


    reloj.tick(100)
    pygame.display.flip()