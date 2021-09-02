from ..base.ViewBase import ViewBase

class MenuView(ViewBase):
    def __init__(self) -> None:
        super().__init__()
        self.renderizado: bool = False

    def getEstado(self) -> bool:
        return self.renderizado
    
    def setEstado(self, estado: bool):
        self.renderizado = estado

    def renderizarMenuPrincipal(self) -> None:
        self.renderizarImagen("assets/fondos/fondo1.png", 0, 0, (self.getAncho(), self.getAlto()))
        self.renderizarImagen("assets/menu/imagenesMenu/jugarEstado1.png", self.getAncho() // 2 - 200, self.getAlto() // 3 - 125, (400, 250))
        self.renderizarImagen("assets/menu/imagenesMenu/salirEstado1.png", self.getAncho() // 2 - 200, self.getAlto() // 2 - 90, (400, 180))
        