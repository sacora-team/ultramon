from pygame import mixer

from .entidades.base.ControllerBase import ControllerBase
from .entidades.menu.MenuController import MenuController
from .entidades.personaje.PersonajeController import PersonajeController
from .constantes.estadosJuego import EstadosJuego

class AppController(ControllerBase):
    def __init__(self) -> None:
        super().__init__()
        self.onInicializarController()
        self.menuPrincipal: MenuController = MenuController()
        self.personaje: PersonajeController = PersonajeController()
    
    def onInicializarController(self) -> None:
        mixer.Channel(0).play(mixer.Sound("./assets/sonidos/opening.wav"))
    
    def getMenuPrincipal(self) -> MenuController:
        return self.menuPrincipal
    
    def getPersonaje(self) -> PersonajeController:
        return self.personaje
    
    def loop(self) -> None:
        while self.ejecutandose:
            if self.getEstado() == EstadosJuego.MENU:
                self.getMenuPrincipal().activar()
                self.setEstado(EstadosJuego.JUEGO)
            if self.getEstado() == EstadosJuego.JUEGO:
                self.getPersonaje().activar()