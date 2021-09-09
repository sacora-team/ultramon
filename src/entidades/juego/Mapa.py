import pygame

ANCHO = pygame.display.Info().current_w
ALTO = pygame.display.Info().current_h

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)

PASTO = pygame.image.load("assets/relieves/pasto.png")
PASTO = pygame.transform.scale(PASTO, (30, 30))
TIERRA = pygame.image.load("assets/relieves/tierra.png")
TIERRA = pygame.transform.scale(TIERRA, (30, 30))

LARGO  = 30
ALTO = 30
MARGEN = 1
 
grid = []
for fila in range(100):
    grid.append([])
    for columna in range(100):
        grid[fila].append(1)
grid[0][0] = 1

pygame.init()  

DIMENSION_VENTANA = [ANCHO, ALTO]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Mapa")

finalizar = True
reloj = pygame.time.Clock()

while finalizar:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            finalizar = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            columna = pos[0] // (LARGO + MARGEN)
            fila = pos[1] // (ALTO + MARGEN)
            grid[fila][columna] = 1
            
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            columna = pos[0] // (LARGO + MARGEN)
            fila = pos[1] // (ALTO + MARGEN)
            grid[fila][columna] = 0


    pantalla.fill(NEGRO)

    for fila in range(100):
        for columna in range(100):
            if grid[fila][columna] == 1:
                pantalla.blit(PASTO, (((MARGEN + LARGO) * columna + MARGEN), ((MARGEN + ALTO) * fila + MARGEN)))
                PASTO_RECT = PASTO.get_rect()
                pantalla.blit(PASTO, PASTO_RECT)
            elif grid[fila][columna] == 0:
                pantalla.blit(TIERRA, (((MARGEN + LARGO) * columna + MARGEN), ((MARGEN + ALTO) * fila + MARGEN)))
                TIERRA_RECT = TIERRA.get_rect()
                pantalla.blit(TIERRA, TIERRA_RECT)

    reloj.tick(100)
    pygame.display.flip()

pygame.quit()