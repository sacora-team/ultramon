from pygame import quit
from ..base.ControllerBase import ControllerBase
from .MenuVista import MenuVista
from .Menu import Menu
from .EstadosFlecha import EstadosFlecha


class MenuController(ControllerBase):
    def __init__(self) -> None:
        super().__init__()
        self.view = MenuVista()
        self.entidad = Menu()

    def getVista(self) -> MenuVista:
        return self.view

    def getEntidad(self) -> Menu:
        return self.entidad

    def loop(self) -> None:
        self.getVista().renderizarMenuPrincipal(EstadosFlecha.JUGAR)
        while self.getActivado():
            self.chequearEventos()
            if self.getArriba():
                self.moverFlecha(self.getEntidad().getDirecciones().ARRIBA)
                self.resetearKeys()
            if self.getAbajo():
                self.moverFlecha(self.getEntidad().getDirecciones().ARRIBA)
                self.resetearKeys()
            if self.getSeleccionar():
                self.resetearKeys()
                if self.getEntidad().getEstadoFlecha() == EstadosFlecha.SALIR:
                    quit()
                elif self.getEntidad().getEstadoFlecha() == EstadosFlecha.JUGAR:
                    self.setActivado(False)

    def moverFlecha(self, direccion: int):
        self.getEntidad().moverFlecha(direccion)
        self.getVista().renderizarMenuPrincipal(self.getEntidad().getEstadoFlecha())

    def activar(self) -> None:
        """ Se activa el ciclo de vida de la instancia """
        self.setActivado(True)
        self.loop()
