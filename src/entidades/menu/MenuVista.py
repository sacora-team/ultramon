from ..base.VistaBase import VistaBase


class MenuVista(VistaBase):
    def __init__(self) -> None:
        super().__init__()
        self.renderizado: bool = False
        
        # Cuan a la izquierda esta la flecha
        self.offsetFlecha: int = -100
        self.alturasFlecha: dict[str, int] = {
            "JUGAR": self.getAlto() // 3 - 60,
            "SALIR": self.getAlto() // 2 - 40,
        }

    def getEstado(self) -> bool:
        return self.renderizado

    def setEstado(self, estado: bool):
        self.renderizado = estado

    def getOffsetFlecha(self) -> int:
        return self.offsetFlecha

    def getAlturasFlecha(self) -> dict[str, int]:
        return self.alturasFlecha

    def setAlturaFlechaActual(self, altura: str) -> None:
        self.alturaFlechaActual = altura

    def renderizarMenuPrincipal(self, alturaFlecha: str) -> None:
        self.renderizarImagen(
            "assets/fondos/fondo1.png", 0, 0, (self.getAncho(), self.getAlto())
        )
        self.renderizarImagen(
            "assets/menu/arrow.png",
            self.getAncho() // 2 - 200 + self.getOffsetFlecha(),
            self.getAlturasFlecha()[alturaFlecha],
            (150, 100),
        )

        if alturaFlecha == "JUGAR":
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
        elif alturaFlecha == "SALIR":
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
