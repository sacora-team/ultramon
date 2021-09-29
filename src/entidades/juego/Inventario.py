from pygame import init, display, draw, image, Surface, transform, font, mouse, event, QUIT, K_e, KEYDOWN, K_r

init()

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

    def renderizarRectangulo(self, color, posx, posy, tamañox, tamañoy) -> None:
        draw.rect(self.getWindow(), color, (posx, posy, tamañox, tamañoy))
        display.update()

    def renderizarTexto(self, texto: str, size: int, color: tuple[int], x: int, y: int) -> None:
        typography = font.Font(self.getFuente(), size)
        self.getWindow().blit(typography.render(texto, True, color), (x, y))
        display.update()
        
    def limpiarPantalla(self) -> None:
        self.getWindow().fill((0, 0, 0))
        display.update()

class Inventario(VistaBase):
    def __init__(self):
        super().__init__()
        self.bucle: bool = True
        self.estado: bool = False 
    
        self.casillero_1 = "assets/items/ultraball.png"
        self.casillero_2 = "assets/pokemones/bulbasur01.png"
        self.casillero_3 = "assets/pokemones/gato03.png"
        self.casillero_4 = "assets/inventario/cruz.png"
        self.casillero_5 = "assets/inventario/cruz.png"
        self.casillero_6 = "assets/inventario/cruz.png"

        self.casillas = [self.casillero_1, self.casillero_2, self.casillero_3,
                        self.casillero_4, self.casillero_5, self.casillero_6]

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getBucle(self):
        return self.bucle

    def setBucle(self, bucle: bool):
        self.bucle = bucle

    def getCasillero1(self):
        return self.casillero_1

    def setCasillero1(self, item: str):
        self.casillero_1 = item

    def getCasillero2(self):
        return self.casillero_2

    def setCasillero2(self, item: str):
        self.casillero_2 = item

    def getCasillero3(self):
        return self.casillero_3

    def setCasillero3(self, item: str):
        self.casillero_3 = item

    def getCasillero4(self):
        return self.casillero_4

    def setCasillero4(self, item: str):
        self.casillero_4 = item

    def getCasillero5(self):
        return self.casillero_5

    def setCasillero5(self, item: str):
        self.casillero_5 = item

    def getCasillero6(self):
        return self.casillero_6

    def setCasillero6(self, item: str):
        self.casillero_6 = item

    def getCasillas(self):
        return self.casillas

    def agregarItem(self, item: str):
        i = 0
        for i in 5:
            if self.getCasillas()[i] == "assets/inventario/cruz.png":
                self.casillas[i] = item
                i = 6
            elif self.getCasillas()[i] != "assets/inventario/cruz.png":
                i += 1

    def loop(self):
        while self.getBucle():
            for evento in event.get():
                if evento.type == QUIT:
                    self.setBucle(False)
                if evento.type == KEYDOWN:
                    if evento.key == K_e:
                        MARRON_INV = (77, 0, 0)
                        self.renderizarImagen("assets/inventario/inventario.png", 0, 0, (300, 200))

                        self.renderizarImagen(self.casillero_1, 25, 25, (70, 70)) # Casillero 1 
                        self.renderizarImagen(self.casillero_2, 115, 25, (70, 70)) # Casillero 2
                        self.renderizarImagen(self.casillero_3, 205, 25, (70, 70)) # Casillero 3
                        self.renderizarImagen(self.casillero_4, 25, 106, (70, 70)) # Casillero 4
                        self.renderizarImagen(self.casillero_5, 115, 106, (70, 70)) # Casillero 5
                        self.renderizarImagen(self.casillero_6, 205, 106, (70, 70)) # Casillero 6

                    if evento.key == K_r:
                        self.limpiarPantalla()        

Inventario().loop()
Inventario().agregarItem("assets/pokemones/pajarito01.png")


            




