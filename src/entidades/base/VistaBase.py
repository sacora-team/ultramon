from pygame import display, image, Surface, transform, font, mouse

from ...constantes.colores import Colores


class VistaBase:
    def __init__(self) -> None:
        self.preInitWindow()
        self.anchoDisplay: int = display.Info().current_w
        self.altoDisplay: int = display.Info().current_h
        self.fuente: str = "./assets/fonts/pokemon_fire_red.ttf"
        self.window = display.set_mode((self.getAncho(), self.getAlto()))
        self.colores: Colores = Colores
        self.cantidadFilas: int = 14
        self.cantidadColumnas: int = 24

    def preInitWindow(self) -> None:
        display.set_icon(image.load("./assets/menu/imagenesMenu/icono.png"))
        display.set_caption("Ultramon")
        mouse.set_visible(False)

    def getWindow(self) -> Surface:
        return self.window

    def getColores(self) -> Colores:
        return self.colores

    def getAncho(self) -> int:
        return self.anchoDisplay

    def getAlto(self) -> int:
        return self.altoDisplay

    def getCantidadFilas(self) -> int:
        return self.cantidadFilas
    
    def setCantidadFilas(self, cantidad: int) ->  int:
        self.cantidadFilas = cantidad

    def getCantidadColumnas(self) -> int:
        return self.cantidadColumnas

    def setCantidadColumnas(self, cantidad: int) ->  int:
        self.cantidadColumnas = cantidad

    def getFuente(self) -> str:
        return self.fuente

    def renderizarImagen(self, url: str, x: int, y: int, escala: tuple[int] = None) -> None:
        imagen = image.load(url)
        if escala:
            imagen = transform.scale(imagen, escala)
        self.getWindow().blit(imagen, (x, y))
        display.update()
        
    def renderizarImagenSinUpdate(self, url: str, x: int, y: int, escala: tuple[int] = None) -> None:
        imagen = image.load(url)
        if escala:
            imagen = transform.scale(imagen, escala)
        self.getWindow().blit(imagen, (x, y))

    def renderizarTexto(self, texto: str, size: int, color: tuple[int], x: int, y: int) -> None:
        typography = font.Font(self.getFuente(), size)
        self.getWindow().blit(typography.render(texto, True, color), (x, y))
        display.update()
        
    def limpiarPantalla(self) -> None:
        self.getWindow().fill(self.getColores().NEGRO)
        display.update()
