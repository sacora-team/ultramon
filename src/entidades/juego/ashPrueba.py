import pygame

# Iniciación de Pygame
pygame.init()

# Pantalla - Ventana
W, H = 1280, 720
PANTALLA = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption('Ash')
icono = pygame.image.load('assets/items/ultraball.png')
pygame.display.set_icon(icono)

# Fondo del juego
fondo = pygame.image.load('assets/fondos/fondo1.png')

# Sprites Ash
ash = pygame.image.load('assets/personajes/ash/frente.png')

caminaDerecha = [
        pygame.image.load('assets/personajes/ash/derecha.png'),
        pygame.image.load('assets/personajes/ash/derechaCaminando1.png'),
        pygame.image.load('assets/personajes/ash/derechaCaminando2.png')
]

caminaIzquierda = [
        pygame.image.load('assets/personajes/ash/izquierda.png'),
        pygame.image.load('assets/personajes/ash/izquierdaCaminando1.png'),
        pygame.image.load('assets/personajes/ash/izquierdaCaminando2.png')
]

caminaAbajo = [
        pygame.image.load('assets/personajes/ash/frente.png'),
        pygame.image.load('assets/personajes/ash/frenteCaminando.png'),
]

caminaArriba = [
        pygame.image.load('assets/personajes/ash/reversa.png'),
        pygame.image.load('assets/personajes/ash/reversaCaminando1.png'),
        pygame.image.load('assets/personajes/ash/reversaCaminando2.png')
]

x=0
px = 1280
py = 720
ancho = 40
velocidad = 10

# Control de FPS
reloj = pygame.time.Clock()

# Variables dirección
izquierda = False
derecha = False
arriba = False
abajo = False

# Pasos
cuentaPasos = 0

# Movimiento
def recargaPantalla():
    global cuentaPasos
    global x

    PANTALLA.blit(fondo, (1280, 720))
    
    # Contador de pasos
    if cuentaPasos + 1 >= 3:
        cuentaPasos = 0

    # Movimiento hacia la izquierda
    if izquierda:
        PANTALLA.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    # Movimiento hacia la derecha
    elif derecha:
        PANTALLA.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    # Movimiento hacia arriba
    elif arriba:
        PANTALLA.blit(caminaArriba[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1

    # Movimiento hacia arriba
    elif abajo:
        PANTALLA.blit(caminaAbajo[cuentaPasos // 1], (int(px), int(py)))
        cuentaPasos += 1        

    else:
        PANTALLA.blit(ash,(int(px), int(py)))

    pygame.display.update()

ejecuta = True

# Bucle de acciones y controles
while ejecuta:
        
    # FPS
    reloj.tick(18)

    # Bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecuta = False

    # Opción tecla pulsada
    keys = pygame.key.get_pressed()

    # Tecla A - Movimiento a la izquierda
    if keys[pygame.K_a]:
        px -= velocidad
        izquierda = True
        derecha = False
        arriba = False
        abajo = False

    # Tecla D - Movimiento a la derecha
    elif keys[pygame.K_d]:
        px += velocidad
        izquierda = False
        derecha = True
        arriba = False
        abajo = False

    # Personaje quieto
    else:
        izquierda = False
        derecha = False
        arriba = False
        abajo = True
        cuentaPasos = 0

    # Tecla W - Movimiento hacia arriba
    if keys[pygame.K_w]:
        izquierda = False
        derecha = False
        arriba = True
        abajo = False
        py -= velocidad

    # Tecla S - Movimiento hacia abajo
    if keys[pygame.K_s]:
        izquierda = False
        derecha = False
        arriba = False
        abajo = True
        py += velocidad


    # Actualización de la ventana
    
    PANTALLA.blit(fondo, (0, 0))
    pygame.display.flip()

    # Llamada a la función de actualización de la ventana
    recargaPantalla()

# Salida del juego
pygame.quit()