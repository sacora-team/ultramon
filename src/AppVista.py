from .entidades.base.VistaBase import VistaBase
from .constantes.habitaciones import Habitaciones
from .constantes.bloques import Bloques
from .entidades.bloques.Agua import Agua
from .entidades.bloques.Fuente import Fuente
from .entidades.bloques.Arbol import Arbol
from .entidades.bloques.Tierra import Tierra 
from .entidades.bloques.Pasto import Pasto


class AppVista(VistaBase):
    def __init__(self) -> None:
        super().__init__()
        self.dimensiones: tuple = (self.getAncho() - self.getCantidadFilas(), self.getAlto() - self.getCantidadColumnas())
        self.mapa = []
        self.tierra = Tierra()
        self.arbol = Arbol()
        self.agua = Agua()
        self.fuente = Fuente()
        self.pasto = Pasto()
        
        self.definido = False
        self.renderizado = False
        
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
    
    def getDimensiones(self) -> tuple:
        return self.dimensiones
    
    def definirHabitacion(self, habitacion: int) -> None:
        """ Dada una habitacion, define sus bloques """
        if self.definido:
            return
        
        if habitacion == Habitaciones.HALL:
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
        if self.renderizado:
            return
        
        self.limpiarPantalla()
        
        for fila in range(0, self.getCantidadFilas()):
            for columna in range(0, self.getCantidadColumnas()):
                if self.getMapa()[fila][columna] == Bloques.PASTO:
                    self.renderizarImagen(self.getPasto().getSprite(), (self.getPasto().getAnchoBloque() * columna), (self.getPasto().getAltoBloque() * fila), (self.getPasto().getAnchoBloque(), self.getPasto().getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.AGUA:
                    self.renderizarImagen(self.getAgua().getSprite(), (self.getAgua().getAnchoBloque() * columna), (self.getAgua().getAltoBloque() * fila), (self.getAgua().getAnchoBloque(), self.getAgua().getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.ARBOL:
                    self.renderizarImagen(self.getArbol().getSprite(), (self.getArbol().getAnchoBloque() * columna), (self.getArbol().getAltoBloque() * fila), (self.getArbol().getAnchoBloque(), self.getArbol().getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.FUENTE:
                    self.renderizarImagen(self.getFuente().getSprite(), (self.getFuente().getAnchoBloque() * columna), (self.getFuente().getAltoBloque() * fila), (self.getFuente().getAnchoBloque(), self.getFuente().getAltoBloque()))
        self.renderizado = True
    