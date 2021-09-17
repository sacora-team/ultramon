from ..base.Bloque import Bloque
from ...constantes.direcciones import Direcciones

class Personaje(Bloque):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = 'assets/personajes/ash/frente1.png'
        self.filaPersonaje: int = self.getCantidadFilas() // 2
        self.columnaPersonaje: int = self.getCantidadColumnas() // 12
        
    def getFilaPersonaje(self) -> int:
        return self.filaPersonaje
    
    def getColumnaPersonaje(self) -> int:
        return self.columnaPersonaje
    
    def setFilaPersonaje(self, fila: int) -> None:
        self.filaPersonaje = fila
        
    def setColumnaPersonaje(self, columna: int) -> None:
        self.columnaPersonaje = columna
        
    def getSprite(self) -> str:
        return self.sprite
    
    def moverPersonaje(self, direccion: int) -> None:
        if direccion == Direcciones.ABAJO:
            self.setFilaPersonaje(self.getFilaPersonaje() + 1)
        elif direccion == Direcciones.ARRIBA:
            self.setFilaPersonaje(self.getFilaPersonaje() - 1)
        elif direccion == Direcciones.IZQUIERDA:
            self.setColumnaPersonaje(self.getColumnaPersonaje() - 1)
        elif direccion == Direcciones.DERECHA:
            self.setColumnaPersonaje(self.getColumnaPersonaje() + 1)
            
        
            
            