from ..base.Bloque import Bloque
from ...constantes.direcciones import Direcciones

class Personaje(Bloque):
    def __init__(self) -> None:
        super().__init__()
        self.spriteAbajo = 'assets/personajes/ash/frente1.png'
        self.spriteIzquierda = 'assets/personajes/ash/izquierda1.png'
        self.spriteDerecha = 'assets/personajes/ash/derecha1.png'
        self.spriteArriba = 'assets/personajes/ash/reversa1.png'
        self.filaPersonaje: int = self.getCantidadFilas() // 2
        self.columnaPersonaje: int = self.getCantidadColumnas() // 12
        self.direccionActual: int = Direcciones.DERECHA
        
    def getFilaPersonaje(self) -> int:
        return self.filaPersonaje
    
    def getColumnaPersonaje(self) -> int:
        return self.columnaPersonaje
    
    def setFilaPersonaje(self, fila: int) -> None:
        self.filaPersonaje = fila
        
    def setColumnaPersonaje(self, columna: int) -> None:
        self.columnaPersonaje = columna
        
    def getSpriteAbajo(self) -> str:
        return self.spriteAbajo
    
    def getSpriteArriba(self) -> str:
        return self.spriteArriba
    
    def getSpriteDerecha(self) -> str:
        return self.spriteDerecha
    
    def getSpriteIzquierda(self) -> str:
        return self.spriteIzquierda
    
    def moverPersonaje(self, direccion: int) -> None:
        if direccion == Direcciones.ABAJO:
            self.setFilaPersonaje(self.getFilaPersonaje() + 1)
        elif direccion == Direcciones.ARRIBA:
            self.setFilaPersonaje(self.getFilaPersonaje() - 1)
        elif direccion == Direcciones.IZQUIERDA:
            self.setColumnaPersonaje(self.getColumnaPersonaje() - 1)
        elif direccion == Direcciones.DERECHA:
            self.setColumnaPersonaje(self.getColumnaPersonaje() + 1)
            
        
            
            