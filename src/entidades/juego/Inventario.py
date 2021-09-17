import pygame
from pygame import display, image, Surface, transform, font, mouse


class VistaBase:
    def __init__(self) -> None:
        self.preInitWindow()
        self.anchoDisplay: int = display.Info().current_w
        self.altoDisplay: int = display.Info().current_h
        self.fuente: str = "./assets/fonts/pokemon_fire_red.ttf"
        self.window = display.set_mode((self.getAncho(), self.getAlto()))

    def preInitWindow(self) -> None:
        display.set_icon(image.load("./assets/menu/imagenesMenu/icono.png"))
        display.set_caption("Ultramon")
        mouse.set_visible(False)

    def getWindow(self) -> Surface:
        return self.window

    def getAncho(self) -> int:
        return self.anchoDisplay

    def getAlto(self) -> int:
        return self.altoDisplay

    def getFuente(self) -> str:
        return self.fuente

    def renderizarImagen(self, url: str, x: int, y: int, escala: tuple[int] = None) -> None:
        imagen = image.load(url)
        if escala:
            imagen = transform.scale(imagen, escala)
        self.getWindow().blit(imagen, (x, y))
        display.update()

    def renderizarTexto(self, texto: str, size: int, color: tuple[int], x: int, y: int) -> None:
        typography = font.Font(self.getFuente(), size)
        self.getWindow().blit(typography.render(texto, True, color), (x, y))
        display.update()
        
    def limpiarPantalla(self) -> None:
        self.getWindow().fill((0, 0, 0))
        display.update()


pygame.init()

class Inventario(VistaBase):
    def __init__(self):
        super().__init__()
        self.getAncho
        self.getAlto

        self.bucle: bool = True
        
        self.estado: bool = False 
    
    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def get_bucle(self):
        return self.bucle

    def set_bucle(self, bucle: bool):
        self.bucle = bucle

    def abrir_inventario(self):
        if self.get_estado == False:
            self.renderizarImagen("assets/ambiente/inventario.png", 0, 0, (60, 40))
        if self.get_estado == True:
            self.renderizarImagen("assets/ambiente/inventario.png", 0, 0, (300, 200))


pantalla = pygame.display.set_mode((1080, 720))

inventarioloco = Inventario()
inventarioloco.abrir_inventario()

while inventarioloco.get_bucle():

    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            inventarioloco.set_bucle(False)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            inventarioloco.set_estado(True)