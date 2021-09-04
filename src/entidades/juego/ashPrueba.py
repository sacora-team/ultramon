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
fondo = pygame.image.load('assets/fondos/fondoPNG.png')

# Reloj
reloj = pygame.time.Clock()


class Ash:

    # Sprites Ash
    def __init__(self) -> None:
        # Velocidad
        self.velocidad: int = 10

        # Posicion X y Posicion Y del personaje
        self.px: int = 600
        self.py: int = 600

        # Variables dirección
        self.izquierda: bool = False
        self.derecha: bool = False
        self.abajo: bool = False
        self.arriba: bool = False

        # Ejecutar bucle
        self.ejecutar = True

        # Cuenta pasos
        self.cuentaPasos: int = 0

        # Sprites Movimientos
        self.spriteIzquierda: tuple = [
            pygame.image.load('assets/personajes/ash/izquierda.png'),
            pygame.image.load('assets/personajes/ash/izquierdaCaminando1.png'),
            pygame.image.load('assets/personajes/ash/izquierdaCaminando2.png')]

        self.spriteDerecha: tuple = [
            pygame.image.load('assets/personajes/ash/derecha.png'),
            pygame.image.load('assets/personajes/ash/derechaCaminando1.png'),
            pygame.image.load('assets/personajes/ash/derechaCaminando2.png')]

        self.spriteAbajo: tuple = [
            pygame.image.load('assets/personajes/ash/frente.png'),
            pygame.image.load('assets/personajes/ash/frenteCaminando.png'),
            pygame.image.load('assets/personajes/ash/frenteCaminando.png')]

        self.spriteArriba: tuple = [
            pygame.image.load('assets/personajes/ash/reversa.png'),
            pygame.image.load('assets/personajes/ash/reversaCaminando1.png'),
            pygame.image.load('assets/personajes/ash/reversaCaminando2.png')]
        
        self.spriteQuieto: str = pygame.image.load('assets/personajes/ash/frente.png')


    def getVelocidad(self) -> int:
        return self.velocidad

    def setVelocidad(self, velocidad: int):
        self.velocidad = velocidad

    # Get y Set de PX y PY
    def getPx(self) -> int:
        return self.px

    def setPx(self, px: int):
        self.px = px

    def getPy(self) -> int:
        return self.py

    def setPy(self, py: int):
        self.py = py

    # Get y Set movimientos
    def getIzquierda(self) -> bool:
        return self.izquierda

    def setIzquierda(self, izquierda: bool):
        self.izquierda = izquierda

    def getDerecha(self) -> bool:
        return self.derecha

    def setDerecha(self, derecha: bool):
        self.derecha = derecha

    def getAbajo(self) -> bool:
        return self.abajo

    def setAbajo(self, abajo: bool):
        self.abajo = abajo

    def getArriba(self) -> bool:
        return self.arriba

    def setArriba(self, arriba: bool):
        self.arriba = arriba

    # Get de los sprites
    def getSpriteIzquierda(self) -> tuple:
        return self.spriteIzquierda

    def getSpriteDerecha(self) -> tuple:
        return self.spriteDerecha

    def getSpriteAbajo(self) -> tuple:
        return self.spriteAbajo

    def getSpriteArriba(self) -> tuple:
        return self.spriteArriba

    def getSpriteQuieto(self) -> str:
        return self.spriteQuieto

    def getEjecutar(self) -> bool:
        return self.ejecutar    

    def getCuentaPasos(self) -> int:
        return self.cuentaPasos

    def setCuentaPasos(self, cuentaPasos: int):
        self.cuentaPasos = cuentaPasos

    def contadorDePasos(self) -> int:
        # Contador de pasos
        if (self.getCuentaPasos() + 1) >= 3:
            self.setCuentaPasos(0)

    def movimiento(self):

        global fondo
        PANTALLA.blit(fondo, (1280, 720))

        # Movimiento hacia la izquierda
        if self.getIzquierda():
            PANTALLA.blit(self.getSpriteIzquierda[self.contadorDePasos()], (self.getPx(), self.getPy()))
            self.setCuentaPasos(self.getCuentaPasos() + 1)

        # Movimiento hacia la derecha
        elif self.getDerecha():
            PANTALLA.blit(self.getSpriteDerecha[self.contadorDePasos()], (self.getPx(), self.getPy()))
            self.setCuentaPasos(self.getCuentaPasos() + 1)

        # Movimiento hacia arriba
        elif self.getArriba():
            PANTALLA.blit(self.getSpriteArriba[self.contadorDePasos()], (self.getPx(), self.getPy()))
            self.setCuentaPasos(self.getCuentaPasos() + 1)

        # Movimiento hacia arriba
        elif self.getAbajo():
            PANTALLA.blit(self.getSpriteAbajo[self.contadorDePasos()], (self.getPx(), self.getPy()))
            self.setCuentaPasos(self.getCuentaPasos() + 1) 

        else:
            PANTALLA.blit(self.getSpriteQuieto(), (self.getPx(), self.getPy()))

        pygame.display.update()

    # Bucle de acciones y controles
    def ejecutarMovimiento(self):
        while self.getEjecutar():

            # Control de FPS
            reloj.tick(18)

            # Bucle del juego
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Salida del juego
                    pygame.quit()

            # Tecla pulsada
            keys = pygame.key.get_pressed()

            # Tecla A - Movimiento a la izquierda
            if keys[pygame.K_a]:
                self.setIzquierda(True)
                self.setDerecha(False)
                self.setArriba(False)
                self.setAbajo(False)
                i = (self.getPx()) - self.velocidad
                self.setPx(i) 

            # Tecla D - Movimiento a la derecha
            elif keys[pygame.K_d]:
                self.setIzquierda(False)
                self.setDerecha(True)
                self.setArriba(False)
                self.setAbajo(False)
                i = (self.getPx()) + self.velocidad
                self.setPx(i) 

            # Tecla W - Movimiento hacia arriba
            elif keys[pygame.K_w]:
                self.setIzquierda(False)
                self.setDerecha(False)
                self.setArriba(True)
                self.setAbajo(False)
                i = (self.getPy()) + self.velocidad
                self.setPx(i)

            # Tecla S - Movimiento hacia abajo
            elif keys[pygame.K_s]:
                self.setIzquierda(False)
                self.setDerecha(False)
                self.setArriba(False)
                self.setAbajo(True)
                i = (self.getPy()) - self.velocidad
                self.setPx(i)

            # Personaje quieto
            else:
                self.setIzquierda(False)
                self.setDerecha(False)
                self.setArriba(False)
                self.setAbajo(False)
                self.setCuentaPasos(0)

            # Actualización de la ventana   
            self.movimiento()
            pygame.display.update()


ash = Ash().ejecutarMovimiento()