from pygame import mixer

from .AppVista import AppVista
from .constantes.habitaciones import Habitaciones
from .constantes.direcciones import Direcciones
from .entidades.base.ControllerBase import ControllerBase
from .entidades.menu.MenuController import MenuController
from .constantes.estadosJuego import EstadosJuego

class AppController(ControllerBase):
    def __init__(self) -> None:
        super().__init__()
        self.onInicializarController()
        self.vista: AppVista = AppVista()
        self.menuPrincipal: MenuController = MenuController()
    
    def onInicializarController(self) -> None:
        mixer.Channel(0).play(mixer.Sound("./assets/sonidos/opening.wav"))
        mixer.Channel(0).set_volume(0.1)
        
    def getVista(self) -> AppVista:
        return self.vista
    
    def getMenuPrincipal(self) -> MenuController:
        return self.menuPrincipal
    
    def loop(self) -> None:
        while self.ejecutandose:
            if self.getEstado() == EstadosJuego.MENU:
                self.getMenuPrincipal().activar()
                self.setEstado(EstadosJuego.JUEGO)
            if self.getEstado() == EstadosJuego.JUEGO:
                self.getVista().definirHabitacion(Habitaciones.HALL)
                self.getVista().renderizarHabitacion(Habitaciones.HALL)
                self.chequearEventos()
                if self.getArriba():
                    self.getVista().moverPersonajeConVerificacion(Direcciones.ARRIBA)
                    self.resetearKeys()
                if self.getAbajo():
                    self.getVista().moverPersonajeConVerificacion(Direcciones.ABAJO)
                    self.resetearKeys()
                if self.getIzquierda():
                    self.getVista().moverPersonajeConVerificacion(Direcciones.IZQUIERDA)
                    self.resetearKeys()
                if self.getDerecha():
                    self.getVista().moverPersonajeConVerificacion(Direcciones.DERECHA)
                    self.resetearKeys()