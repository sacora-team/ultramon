from pygame import display, image, Surface, transform, font, mouse
import ctypes


class ViewBase:
    def __init__(self) -> None:
        self.initWindow()
        self.anchoDisplay: int = ctypes.windll.user32.GetSystemMetrics(0)
        self.altoDisplay: int = ctypes.windll.user32.GetSystemMetrics(1)
        self.font: str = "./assets/fonts/pokemon_fire_red.ttf"
        self.window = display.set_mode((self.getAncho(), self.getAlto()))
        self.colores: dict[str, tuple[int]] = {
            "BLANCO": (255, 255, 255),
            "NEGRO": (0, 0, 0),
        }

    def initWindow(self) -> None:
        display.set_icon(image.load("./assets/menu/imagenesMenu/icono.png"))
        display.set_caption("Ultramon")
        mouse.set_visible(False)

    def getWindow(self) -> Surface:
        return self.window

    def getColores(self) -> dict:
        return self.colores

    def getAncho(self) -> int:
        return self.anchoDisplay

    def getAlto(self) -> int:
        return self.altoDisplay

    def getFont(self) -> str:
        return self.font

    def renderizarImagen(self, url: str, x: int, y: int, escala: tuple[int] = None):
        imagen = image.load(url)
        if escala:
            imagen = transform.scale(imagen, escala)
        self.getWindow().blit(imagen, (x, y))
        display.update()

    def renderizarTexto(self, texto: str, size: int, color: tuple[int], x: int, y: int):
        typography = font.Font(self.getFont(), size)
        self.getWindow().blit(typography.render(texto, True, color), (x, y))
        display.update()
