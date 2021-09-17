from pygame import display
from .entidades.base.VistaBase import VistaBase
from .constantes.habitaciones import Habitaciones
from .constantes.bloques import Bloques
from .entidades.bloques.Agua import Agua
from .entidades.bloques.Fuente import Fuente
from .entidades.bloques.Arbol import Arbol
from .entidades.bloques.Tierra import Tierra 
from .entidades.bloques.Pasto import Pasto
from .entidades.bloques.Personaje import Personaje
from .constantes.direcciones import Direcciones


class AppVista(VistaBase):
    def __init__(self) -> None:
        super().__init__()
        self.mapa = []
        self.tierra = Tierra()
        self.arbol = Arbol()
        self.agua = Agua()
        self.fuente = Fuente()
        self.pasto = Pasto()
        self.personaje = Personaje()
        
        self.caminables = [Bloques.PASTO, Bloques.TIERRA]
        
        self.definido = False
        self.renderizado = False
        
    def getCaminables(self) -> list:
        return self.caminables    
    
    def getTierra(self) -> Tierra:
        return self.tierra
        
    def getArbol(self) -> Arbol:
        return self.arbol
        
    def getAgua(self) -> Agua:
        return self.agua
        
    def getFuente(self) -> Fuente:
        return self.fuente
    
    def getPasto(self) -> Pasto:
        return self.pasto
    
    def getMapa(self) -> list:
        return self.mapa
    
    def getPersonaje(self) -> Personaje:
        return self.personaje
    
    def definirHabitacion(self, habitacion: int) -> None:
        """ Dada una habitacion, define sus bloques """
        
        # TODO: Modularizar
        
        if habitacion == Habitaciones.HALL:
            if self.definido:
                return
            
            for fila in range(0, self.getCantidadFilas()):
                self.getMapa().append([])
                for columna in range(0, self.getCantidadColumnas()):
                    self.getMapa()[fila].append(Bloques.PASTO)
        
            for fila in range(1, 2):
                for columna in range(0, self.getCantidadColumnas()):
                    self.getMapa()[fila][columna] = Bloques.AGUA
        
            for fila in range(12, 13):
                for columna in range(0, self.getCantidadColumnas()):
                    self.getMapa()[fila][columna] = Bloques.AGUA
        
            for fila in range(0, 1):
                for columna in range(0, self.getCantidadColumnas()):
                    self.getMapa()[fila][columna] = Bloques.ARBOL
        
            for fila in range(13, 14):
                for columna in range(0, self.getCantidadColumnas()):
                    self.getMapa()[fila][columna] = Bloques.ARBOL
                    
            self.getMapa()[self.getCantidadFilas() // 2][self.getCantidadColumnas() // 2] = Bloques.FUENTE
        
            self.definido = True

    
    def renderizarHabitacion(self, habitacion: int) -> None:
        """" Dada una habitacion, la renderiza en pantalla """ 
        
        # TODO: Modulizar
               
        if habitacion == Habitaciones.HALL:
            if self.renderizado:
                return
            
            self.limpiarPantalla()
            
            for fila in range(0, self.getCantidadFilas()):
                for columna in range(0, self.getCantidadColumnas()):
                    if self.getMapa()[fila][columna] == Bloques.PASTO:
                        self.renderizarImagenSinUpdate(self.getPasto().getSprite(), (self.getPasto().getAnchoBloque() * columna), (self.getPasto().getAltoBloque() * fila), (self.getPasto().getAnchoBloque(), self.getPasto().getAltoBloque()))
                    if self.getMapa()[fila][columna] == Bloques.AGUA:
                        self.renderizarImagenSinUpdate(self.getAgua().getSprite(), (self.getAgua().getAnchoBloque() * columna), (self.getAgua().getAltoBloque() * fila), (self.getAgua().getAnchoBloque(), self.getAgua().getAltoBloque()))
                    if self.getMapa()[fila][columna] == Bloques.ARBOL:
                        self.renderizarImagenSinUpdate(self.getArbol().getSprite(), (self.getArbol().getAnchoBloque() * columna), (self.getArbol().getAltoBloque() * fila), (self.getArbol().getAnchoBloque(), self.getArbol().getAltoBloque()))
                    if self.getMapa()[fila][columna] == Bloques.FUENTE:
                        self.renderizarImagenSinUpdate(self.getFuente().getSprite(), (self.getFuente().getAnchoBloque() * columna), (self.getFuente().getAltoBloque() * fila), (self.getFuente().getAnchoBloque(), self.getFuente().getAltoBloque()))
            
            display.update()

            # Renderizo el personaje en la habitación
            self.renderizarImagen(self.getPersonaje().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
        
            self.renderizado = True
        
    def moverPersonajeConVerificacion(self, direccion: int) -> None:
        """ Dada una direccion, verifica que sea caminable y mueve su posicion """

        # Verifica que el bloque sea pasto o tierra (caminables)
        # Cuando hace el movimiento, rellena el bloque anterior del personaje con el contenido del bloque sobre el que estaba        
        
        # TODO: Refactorizar
        
        if direccion == Direcciones.ABAJO:
            if self.getMapa()[self.getPersonaje().getFilaPersonaje() + 1][self.getPersonaje().getColumnaPersonaje()] == Bloques.PASTO:
                self.renderizarImagenSinUpdate(self.getPasto().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(self.getPersonaje().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
            elif self.getMapa()[self.getPersonaje().getFilaPersonaje() + 1][self.getPersonaje().getColumnaPersonaje()] == Bloques.TIERRA:
                self.renderizarImagenSinUpdate(self.getTierra().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(self.getPersonaje().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
        elif direccion == Direcciones.ARRIBA:
            if self.getMapa()[self.getPersonaje().getFilaPersonaje() - 1][self.getPersonaje().getColumnaPersonaje()] == Bloques.PASTO:
                self.renderizarImagenSinUpdate(self.getPasto().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(self.getPersonaje().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
            elif self.getMapa()[self.getPersonaje().getFilaPersonaje() - 1][self.getPersonaje().getColumnaPersonaje()] == Bloques.TIERRA:
                self.renderizarImagenSinUpdate(self.getTierra().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(self.getPersonaje().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
        elif direccion == Direcciones.IZQUIERDA:
            if self.getMapa()[self.getPersonaje().getFilaPersonaje()][self.getPersonaje().getColumnaPersonaje() - 1] == Bloques.PASTO:
                self.renderizarImagenSinUpdate(self.getPasto().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(self.getPersonaje().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
            elif self.getMapa()[self.getPersonaje().getFilaPersonaje()][self.getPersonaje().getColumnaPersonaje() - 1] == Bloques.TIERRA:
                self.renderizarImagenSinUpdate(self.getTierra().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(self.getPersonaje().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
        elif direccion == Direcciones.DERECHA:
            if self.getMapa()[self.getPersonaje().getFilaPersonaje()][self.getPersonaje().getColumnaPersonaje() + 1] == Bloques.PASTO:
                self.renderizarImagenSinUpdate(self.getPasto().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(self.getPersonaje().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
            elif self.getMapa()[self.getPersonaje().getFilaPersonaje()][self.getPersonaje().getColumnaPersonaje() + 1] == Bloques.TIERRA:
                self.renderizarImagenSinUpdate(self.getTierra().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(self.getPersonaje().getSprite(), (self.getPersonaje().getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getPersonaje().getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getPersonaje().getAnchoBloque(), self.getPersonaje().getAltoBloque()))
        