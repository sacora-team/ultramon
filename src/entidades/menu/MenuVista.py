from ..base.VistaBase import VistaBase
from .EstadosFlecha import EstadosFlecha

class MenuVista(VistaBase):
    def __init__(self) -> None:
        super().__init__()
        self.renderizado: bool = False
        
        # Cuan a la izquierda esta la flecha
        self.offsetFlecha: int = -100
        self.alturasFlecha: dict[int, int] = {
            EstadosFlecha.JUGAR: self.getAlto() // 3 - 60,
            EstadosFlecha.SALIR: self.getAlto() // 2 - 40,
        }

    def getEstado(self) -> bool:
        return self.renderizado

    def setEstado(self, estado: bool) -> None:
        self.renderizado = estado

    def getOffsetFlecha(self) -> int:
        return self.offsetFlecha

    def getAlturasFlecha(self) -> dict[str, int]:
        return self.alturasFlecha

    def renderizarMenuPrincipal(self, alturaFlecha: int) -> None:
        self.renderizarImagen(
            "assets/fondos/fondo1.png", 0, 0, (self.getAncho(), self.getAlto())
        )
        self.renderizarImagen(
            "assets/menu/arrow.png",
            self.getAncho() // 2 - 200 + self.getOffsetFlecha(),
            self.getAlturasFlecha()[alturaFlecha],
            (150, 100),
        )

        if alturaFlecha == EstadosFlecha.JUGAR:
            self.renderizarImagen(
                "assets/menu/imagenesMenu/jugarEstado2.png",
                self.getAncho() // 2 - 200,
                self.getAlto() // 3 - 125,
                (400, 250),
            )
            self.renderizarImagen(
                "assets/menu/imagenesMenu/salirEstado1.png",
                self.getAncho() // 2 - 200,
                self.getAlto() // 2 - 90,
                (400, 200),
            )
        elif alturaFlecha == EstadosFlecha.SALIR:
            self.renderizarImagen(
                "assets/menu/imagenesMenu/jugarEstado1.png",
                self.getAncho() // 2 - 200,
                self.getAlto() // 3 - 125,
                (400, 250),
            )
            self.renderizarImagen(
                "assets/menu/imagenesMenu/salirEstado2.png",
                self.getAncho() // 2 - 200,
                self.getAlto() // 2 - 90,
                (400, 200),
            )
