import pygame

class Mapa:
    pygame.init()

    ANCHO_PANTALLA: int = pygame.display.Info().current_w
    ALTO_PANTALLA: int = pygame.display.Info().current_h

    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)
    VERDE = ( 0, 255, 0)
    ROJO = (255, 0, 0)

    ANCHO_BLOQUE  = 45
    ALTO_BLOQUE = 45
    MARGEN_BLOQUE = 1

    CANTIDAD_FILAS: int = ANCHO_PANTALLA // ANCHO_BLOQUE
    CANTIDAD_COLUMNAS: int = ALTO_PANTALLA // ALTO_BLOQUE

    PASTO = pygame.image.load("assets/relieves/pasto.png")
    PASTO = pygame.transform.scale(PASTO, (ALTO_BLOQUE, ANCHO_BLOQUE))
    TIERRA = pygame.image.load("assets/relieves/tierra.png")
    TIERRA = pygame.transform.scale(TIERRA, (ALTO_BLOQUE, ANCHO_BLOQUE))

    grid = []

    for fila in range(100):
        grid.append([])
        for columna in range(100):
            grid[fila].append(1)
    grid[0][0] = 1

    DIMENSION_VENTANA = [ANCHO_PANTALLA, ALTO_PANTALLA]
    pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
    pygame.display.set_caption("Mapa")

    bucle = True
    reloj = pygame.time.Clock()

    while bucle:
        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT: 
                bucle = False

        pantalla.fill(NEGRO)

        for fila in range(100):
            for columna in range(100):
                if grid[fila][columna] == 1:
                    pantalla.blit(PASTO, (((MARGEN_BLOQUE + ANCHO_BLOQUE) * columna + MARGEN_BLOQUE), ((MARGEN_BLOQUE + ALTO_BLOQUE) * fila + MARGEN_BLOQUE)))
                    PASTO_RECT = PASTO.get_rect()
                    pantalla.blit(PASTO, PASTO_RECT)
                elif grid[fila][columna] == 0:
                    pantalla.blit(TIERRA, (((MARGEN_BLOQUE + ANCHO_BLOQUE) * columna + MARGEN_BLOQUE), ((MARGEN_BLOQUE + ALTO_BLOQUE) * fila + MARGEN_BLOQUE)))
                    TIERRA_RECT = TIERRA.get_rect()
                    pantalla.blit(TIERRA, TIERRA_RECT)

        reloj.tick(100)
        pygame.display.flip()

    pygame.quit()