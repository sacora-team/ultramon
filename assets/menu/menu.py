import pygame
import ctypes 
import sys


pygame.init()
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

resolucion = (ancho, alto)
pantalla = pygame.display.set_mode((resolucion), pygame.RESIZABLE)
pygame.FULLSCREEN


fondo = pygame.image.load("assets/fondos/fondo1.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))
rect_fondo = fondo.get_rect()
rect_fondo = rect_fondo.move((0, 0))
pantalla.blit(fondo, rect_fondo)


# Colores

COLOR_BLANCO = (255,255,255)   
COLOR_LIGHT = (170,170,170)
COLOR_NEGRO = (100,100,100)
COLOR_AZUL = (20, 25, 60)

TIPOGRAFIA = pygame.font.SysFont('Corbel', 30) 


texto_salir = pygame.image.load("assets/menu/imagenesMenu/salirEstado1.png")
pantalla.blit(texto_salir, (ancho/2, alto/2))
texto_salir = pygame.transform.scale(texto_salir, (200, 100))


texto_jugar = TIPOGRAFIA.render('Jugar', True, COLOR_BLANCO)


while True: 
      
    for ev in pygame.event.get(): 
        if ev.type == pygame.QUIT: 
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN: 
            if ancho/2 <= mouse[0] <= ancho/2+140 and alto/2 <= mouse[1] <= alto/2+40: 
                pygame.quit() 
    
    mouse = pygame.mouse.get_pos() 


    # Boton Salir  
    if ancho/2 <= mouse[0] <= ancho/2+50 and alto/2 <= mouse[1] <= alto/2+50: 
        texto_salir = pygame.image.load("assets/menu/imagenesMenu/salirEstado1.png")
    else: 
        texto_salir = pygame.image.load("assets/menu/imagenesMenu/salirEstado2.png")


    # Boton Jugar
    if ancho/2 <= mouse[0] <= ancho/2+50 and alto/3 <= mouse[1] <= alto/3+50: 
        pygame.draw.rect(pantalla, COLOR_LIGHT,[ancho/2-50, alto/3, 100, 50]) 
    else: 
        pygame.draw.rect(pantalla, COLOR_NEGRO, [ancho/2-50, alto/3, 100, 50])
    pantalla.blit(texto_jugar, (ancho/2-50, alto/3))

      

    pygame.display.update()