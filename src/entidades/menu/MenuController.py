from pygame import quit
from ..base.ControllerBase import ControllerBase
from .MenuView import MenuView


class MenuController(ControllerBase):
    def __init__(self) -> None:
        super().__init__()
        self.activado: bool = False
        self.view = MenuView()
        self.estadoFlecha = "JUGAR"

    def getView(self) -> MenuView:
        return self.view

    def getActivado(self) -> bool:
        return self.activado

    def setActivado(self, activado: bool) -> None:
        self.activado = activado

    def getEstadoFlecha(self):
        return self.estadoFlecha

    def setEstadoFlecha(self, estado: str):
        self.estadoFlecha = estado.upper()

    def loop(self) -> None:
        self.getView().renderizarMenuPrincipal("JUGAR")
        while self.getActivado():
            self.chequearEventos()
            if self.getUpKey():
                self.moverFlecha("ARRIBA")
                self.resetearKeys()
            if self.getDownKey():
                self.moverFlecha("ABAJO")
                self.resetearKeys()
            if self.getSelectKey():
                self.resetearKeys()
                if self.getEstadoFlecha() == "SALIR":
                    quit()
                elif self.getEstadoFlecha() == "JUGAR":
                    self.setActivado(False)

    def moverFlecha(self, movimiento: str):
        if movimiento.upper() == "ARRIBA":
            if self.getEstadoFlecha() == "JUGAR":
                self.setEstadoFlecha("SALIR")
            elif self.getEstadoFlecha() == "SALIR":
                self.setEstadoFlecha("JUGAR")
        elif movimiento.upper() == "ABAJO":
            if self.getEstadoFlecha() == "JUGAR":
                self.setEstadoFlecha("SALIR")
            elif self.getEstadoFlecha() == "SALIR":
                self.setEstadoFlecha("JUGAR")
        self.getView().renderizarMenuPrincipal(self.getEstadoFlecha())

    def activar(self) -> None:
        self.setActivado(True)
        self.loop()
