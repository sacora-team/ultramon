from ..base.EntidadBase import EntidadBase


class Personaje(EntidadBase):
    def __init__(self) -> None:
        super().__init__()
        self.velocidad: int = 45
        self.py: int = 0
        self.px: int = 0
        
    def getVelocidad(self) -> int:
        return self.velocidad
    
    def getPosicionY(self) -> int:
        return self.py
    
    def getPosicionX(self) -> int:
        return self.px
    
    def setPosicionY(self, p: int) -> None:
        self.py = p
        
    def setPosicionX(self, p: int) -> None:
        self.px = p
        
    def mover(self, direccion: str):
        if direccion == self.getDirecciones().ARRIBA:
            self.setPosicionY(self.getPosicionY() + self.getVelocidad())
        elif direccion == self.getDirecciones().ABAJO:
            self.setPosicionY(self.getPosicionY() - self.getVelocidad())
        elif direccion == self.getDirecciones().DERECHA:
            self.setPosicionX(self.getPosicionX() + self.getVelocidad())
        elif direccion == self.getDirecciones().IZQUIERDA:
            self.setPosicionX(self.getPosicionX() - self.getVelocidad())