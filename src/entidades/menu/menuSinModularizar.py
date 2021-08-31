import pygame
import ctypes 
import sys

##############
# PREVISORIO #
##############

pygame.init()
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Resolucion y Pantalla
resolucion = (ancho, alto)
pantalla = pygame.display.set_mode((resolucion), pygame.RESIZABLE)


# Fondo
fondo = pygame.image.load("assets/fondos/fondo1.png")
fondo = pygame.transform.scale(fondo, (ancho, alto))
rect_fondo = fondo.get_rect()
rect_fondo = rect_fondo.move((0, 0))
pantalla.blit(fondo, rect_fondo)


# Icono y nombre de ventana
icono = pygame.image.load("assets/menu/imagenesMenu/icono.png")
pygame.display.set_icon(icono)
pygame.display.set_caption('Ultramon')

# Colores
COLOR_CIAN = (162,202,223)   
COLOR_CELESTE = (178,255,255)


# Boton Salir (Diseño)
texto_salir = pygame.image.load("assets/menu/imagenesMenu/salirEstado1.png")
texto_salir = pygame.transform.scale(texto_salir, (400, 250))
pantalla.blit(texto_salir, (ancho/2 - 200, alto/2 - 125))

# Boton Jugar (Diseño)
texto_jugar = pygame.image.load("assets/menu/imagenesMenu/jugarEstado1.png")
texto_jugar = pygame.transform.scale(texto_jugar, (400, 250))
pantalla.blit(texto_jugar, (ancho/2 - 200, alto/3 - 125))


while True: 
      
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: 
            pygame.quit()
        if ev.type == pygame.MOUSEBUTTONDOWN: 
            if ancho/2 <= mouse[0] <= ancho/2+140 and alto/2 <= mouse[1] <= alto/2+40: 
                pygame.quit() 
                
    mouse = pygame.mouse.get_pos() 


    # Boton Salir (Funcion)

    if ancho/2-100 <= mouse[0] <= ancho/2+100 and alto/2-100 <= mouse[1] <= alto/2+100: 
        texto_salir = pygame.image.load("assets/menu/imagenesMenu/salirEstado1.png")
        # pygame.draw.rect(pantalla, COLOR_CELESTE,[ancho/2-125, alto/2-75, 250, 150])
    else:
        texto_salir = pygame.image.load("assets/menu/imagenesMenu/salirEstado2.png")
        # pygame.draw.rect(pantalla, COLOR_CIAN, [ancho/2-125, alto/2-75, 250, 150])


    # Boton Jugar (Funcion)

    if ancho/2-20 <= mouse[0] <= ancho/2+20 and alto/3-20 <= mouse[1] <= alto/3+20: 
        texto_jugar = pygame.image.load("assets/menu/imagenesMenu/jugarEstado1.png")
    else:
        texto_jugar = pygame.image.load("assets/menu/imagenesMenu/jugarEstado2.png")


    pygame.display.update()