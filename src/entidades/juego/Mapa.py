import pygame
import random

pygame.init()

class Mapa:
    def __init__(self):
        self.ancho_pantalla: int = pygame.display.Info().current_w
        self.alto_pantalla: int = pygame.display.Info().current_h

        self.cantidad_filas: int = 14
        self.cantidad_columnas: int = 24

        self.ancho_bloque: int = (self.ancho_pantalla) // self.cantidad_columnas
        self.alto_bloque: int = (self.alto_pantalla) // self.cantidad_filas

        self.dimension_pantalla: tuple = [self.ancho_pantalla - self.cantidad_filas, self.alto_pantalla - self.cantidad_columnas]

    def get_ancho_pantalla(self) -> None:
        return self.ancho_pantalla
    
    def get_alto_pantalla(self) -> None:
        return self.alto_pantalla

    def get_ancho_bloque(self) -> None:
        return self.ancho_bloque

    def get_alto_bloque(self) -> None:
        return self.alto_bloque

    def get_cantidad_filas(self) -> None:
        return self.cantidad_filas

    def get_cantidad_columnas(self) -> None:
        return self.cantidad_columnas

    def get_dimension_pantalla(self) -> None:
        return self.dimension_pantalla

mapa = Mapa()

pantalla = pygame.display.set_mode(mapa.get_dimension_pantalla())
pygame.display.set_caption("Ultramon")

bucle = True
reloj = pygame.time.Clock()

#### PASTO  ####
PASTO = pygame.image.load("assets/relieves/pasto.png")
PASTO = pygame.transform.scale(PASTO, (mapa.get_ancho_bloque(), mapa.get_alto_bloque()))
PASTO_TXT = "PASTO"

#### TIERRA  ####
TIERRA = pygame.image.load("assets/relieves/tierra.png")
TIERRA = pygame.transform.scale(TIERRA, (mapa.get_ancho_bloque(), mapa.get_alto_bloque()))
TIERRA_TXT = "TIERRA"

#### AGUA  ####
AGUA = pygame.image.load("assets/relieves/agua.png")
AGUA = pygame.transform.scale(AGUA, (mapa.get_ancho_bloque(), mapa.get_alto_bloque()))
AGUA_TXT = "AGUA"

#### PIEDRA  ####
PIEDRA = pygame.image.load("assets/ambiente/piedra.png")
PIEDRA = pygame.transform.scale(PIEDRA, (mapa.get_ancho_bloque(), mapa.get_alto_bloque()))
PIEDRA_TXT = "PIEDRA"

#### ARBOL  ####
ARBOL = pygame.image.load("assets/ambiente/arbol.png")
ARBOL = pygame.transform.scale(ARBOL, (mapa.get_ancho_bloque(), mapa.get_alto_bloque()))
ARBOL_TXT = "ARBOL"

#### FUENTE  ####
FUENTE = pygame.image.load("assets/ambiente/fuente.png")
FUENTE = pygame.transform.scale(FUENTE, (mapa.get_ancho_bloque(), mapa.get_alto_bloque()))
FUENTE_TXT = "FUENTE"

#### GRILLA ####
grid = []

#### PASTO -DEFINIR POSICION DE BLOQUES DE PASTO- ####
for fila in range(0, mapa.get_cantidad_filas()):
    grid.append([])
    for columna in range(0, mapa.get_cantidad_columnas()):
        grid[fila].append("PASTO")

#### AGUA -DEFINIR POSICION DE BLOQUES DE AGUA- ####
for fila in range(1, 2):
    for columna in range(0, mapa.get_cantidad_columnas()):
        grid[fila][columna] = "AGUA"

for fila in range(12, 13):
    for columna in range(0, mapa.get_cantidad_columnas()):
        grid[fila][columna] = "AGUA"

#### ARBOL -DEFINIR POSICION DE BLOQUES DE ARBOL- ####
for fila in range(0, 1):
    for columna in range(0, mapa.get_cantidad_columnas()):
        grid[fila][columna] = "ARBOL"

for fila in range(13, 14):
    for columna in range(0, mapa.get_cantidad_columnas()):
        grid[fila][columna] = "ARBOL"

#### FUENTE -DEFINIR POSICION DE BLOQUES DE PASTO- ####
grid[mapa.get_cantidad_filas() // 2][mapa.get_cantidad_columnas() // 2] = "FUENTE"

while bucle:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            bucle = False

    pantalla.fill((0, 0, 0))

    for fila in range(0, mapa.get_cantidad_filas()):
        for columna in range(0, mapa.get_cantidad_columnas()):

            #### PASTO -DIBUJAR BLOQUES DE PASTO- ####
            if grid[fila][columna] == PASTO_TXT:
                pantalla.blit(PASTO, (
                    ((mapa.get_ancho_bloque()) * columna),
                    ((mapa.get_alto_bloque()) * fila))
                    )

                PASTO_RECT = PASTO.get_rect()
                pantalla.blit(PASTO, PASTO_RECT)

            #### TIERRA -DIBUJAR BLOQUES DE TIERRA- ####
            elif grid[fila][columna] == TIERRA_TXT:
                pantalla.blit(TIERRA, (
                    ((mapa.get_ancho_bloque()) * columna),
                    ((mapa.get_alto_bloque()) * fila))
                    )

                TIERRA_RECT = TIERRA.get_rect()
                pantalla.blit(TIERRA, TIERRA_RECT)

            #### AGUA -DIBUJAR BLOQUES DE AGUA- ####
            elif grid[fila][columna] == AGUA_TXT:
                pantalla.blit(AGUA, (
                    ((mapa.get_ancho_bloque()) * columna),
                    ((mapa.get_alto_bloque()) * fila))
                    )

                AGUA_RECT = AGUA.get_rect()
                pantalla.blit(AGUA, AGUA_RECT)

            #### ARBOL -DIBUJAR BLOQUES DE ARBOL- ####
            if grid[fila][columna] == ARBOL_TXT:
                pantalla.blit(ARBOL, (
                    ((mapa.get_ancho_bloque()) * columna),
                    ((mapa.get_alto_bloque()) * fila))
                    )

                ARBOL_RECT = ARBOL.get_rect()
                pantalla.blit(ARBOL, ARBOL_RECT)

            #### FUENTE -DIBUJAR BLOQUES DE FUENTE- ####
            elif grid[fila][columna] == FUENTE_TXT:
                pantalla.blit(FUENTE, (
                    ((mapa.get_ancho_bloque()) * columna),
                    ((mapa.get_alto_bloque()) * fila))
                    )

                FUENTE_RECT = FUENTE.get_rect()
                pantalla.blit(FUENTE, FUENTE_RECT)


    reloj.tick(100)
    pygame.display.flip()