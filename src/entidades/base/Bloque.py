from pygame import Surface

from ...constantes.bloques import Bloques
from .VistaBase import VistaBase


class Bloque(VistaBase):
    def __init__(self) -> None:
        super().__init__()
        self.tipo: int = None
        self.anchoBloque: int = self.getAncho() // self.getCantidadColumnas()
        self.altoBloque: int = self.getAlto() // self.getCantidadFilas()
        self.caminable: bool = True
        
    def getTipo(self) -> int:
        return self.tipo
    
    def setTipo(self, tipo: int) -> None:
        self.tipo = tipo
        
    def actualizarMedidas(self, accion: bool) -> None:
        if accion == 1:
            self.cantidadColumnas = self.cantidadColumnas + 1
            self.cantidadFilas = self.cantidadFilas + 1            
        if accion == 2:
            self.cantidadColumnas = self.cantidadColumnas - 1
            self.cantidadFilas = self.cantidadFilas - 1
        
        self.anchoBloque = self.getAncho() // self.cantidadColumnas
        self.altoBloque = self.getAlto() // self.cantidadFilas

    def getAltoBloque(self) -> int:
        return self.altoBloque
    
    def getAnchoBloque(self) -> int:
        return self.anchoBloque
    
    def getCaminable(self) -> bool:
        return self.caminable