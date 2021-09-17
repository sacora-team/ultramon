from pygame import Surface
from .VistaBase import VistaBase

class Bloque(VistaBase):
    def __init__(self) -> None:
        super().__init__()
        self.anchoBloque: int = self.getAncho() // self.getCantidadColumnas()
        self.altoBloque: int = self.getAlto() // self.getCantidadFilas()
        self.caminable: bool = True
        
    def getAltoBloque(self) -> int:
        return self.altoBloque
    
    def getAnchoBloque(self) -> int:
        return self.anchoBloque
    
    def getCaminable(self) -> bool:
        return self.caminable