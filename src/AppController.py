from pygame import init
from .entidades.base.ControllerBase import ControllerBase
from .entidades.menu.MenuController import MenuController
from .constantes.estadosJuego import EstadosJuego

class AppController(ControllerBase):
    def __init__(self) -> None:
        super().__init__()
        self.menuPrincipal: MenuController = MenuController()
    
    def getMenuPrincipal(self) -> MenuController:
        return self.menuPrincipal
    
    def loop(self) -> None:
        while self.ejecutandose:
            if self.getEstado() == EstadosJuego.MENU:
                self.getMenuPrincipal().activar()
                self.setEstado(EstadosJuego.JUEGO)
            if self.getEstado() == EstadosJuego.JUEGO:
                pass