import pygame

pygame.init()

class Mapa:
    def __init__(self):
        self.ancho_pantalla: int = pygame.display.Info().current_w
        self.alto_pantalla: int = pygame.display.Info().current_h

        self.ancho_bloque: int = 45
        self.alto_bloque: int = 45
        self.margen_bloque: int = 1

        self.cantidad_filas: int = self.ancho_pantalla // self.ancho_bloque
        self.cantidad_columnas: int = self.alto_pantalla // self.alto_bloque

        self.dimension_pantalla: tuple = [self.ancho_pantalla, self.alto_pantalla]

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

grid = []

for fila in range(100):
    grid.append([])
    for columna in range(100):
        grid[fila].append(1)
grid[0][0] = 1

pantalla = pygame.display.set_mode(mapa.get_dimension_pantalla())
pygame.display.set_caption("Ultramon")

bucle = True
reloj = pygame.time.Clock()

while bucle:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            bucle = False

    pantalla.fill((0,0,0))

    for fila in range(100):
        for columna in range(100):
            if grid[fila][columna] == 1:
                pantalla.blit(PASTO, (
                    ((mapa.get_margen_bloque() + mapa.get_ancho_bloque()) * columna + mapa.get_margen_bloque()),
                    ((mapa.get_margen_bloque() + mapa.get_alto_bloque()) * fila + mapa.get_margen_bloque()))
                    )
                PASTO_RECT = PASTO.get_rect()
                pantalla.blit(PASTO, PASTO_RECT)

            elif grid[fila][columna] == 0:
                pantalla.blit(TIERRA, (
                    ((mapa.get_margen_bloque() + mapa.get_ancho_bloque()) * columna + mapa.get_margen_bloque()),
                    ((mapa.get_margen_bloque() + mapa.get_alto_bloque()) * fila + mapa.get_margen_bloque()))
                    )
                TIERRA_RECT = TIERRA.get_rect()
                pantalla.blit(TIERRA, TIERRA_RECT)

    reloj.tick(100)
    pygame.display.flip()