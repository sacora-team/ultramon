import pygame
 
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = ( 0, 255, 0)
ROJO = (255, 0, 0)

LARGO  = 30
ALTO = 30
MARGEN = 1
 

grid = []
for fila in range(100):
    grid.append([])
    for columna in range(100):
        grid[fila].append(0)

grid[0][0] = 1
 

pygame.init()
  

DIMENSION_VENTANA = [1280, 720]
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)
pygame.display.set_caption("Mapa")

hecho = False

reloj = pygame.time.Clock()


while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            hecho = True
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            
            pos = pygame.mouse.get_pos()

            columna = pos[0] // (LARGO + MARGEN)
            fila = pos[1] // (ALTO + MARGEN)
            
            grid[fila][columna] = 1
            print("Click ", pos, "Coordenadas de la retícula: ", fila, columna)


    pantalla.fill(NEGRO)
 
    for fila in range(100):
        for columna in range(100):
            color = BLANCO
            if grid[fila][columna] == 1:
                color = VERDE
            pygame.draw.rect(pantalla,
                             color,
                             [(MARGEN + LARGO) * columna + MARGEN,
                              (MARGEN + ALTO) * fila + MARGEN,
                              LARGO,
                              ALTO])
     
    reloj.tick(60)
    pygame.display.flip()
     

pygame.quit()