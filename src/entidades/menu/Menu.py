from ..base.EntidadBase import EntidadBase
from .EstadosFlecha import EstadosFlecha

class Menu(EntidadBase):
    def __init__(self) -> None:
        super().__init__()
        self.estadoFlecha = EstadosFlecha.JUGAR
    
    def getEstadoFlecha(self) -> int:
        return self.estadoFlecha

    def setEstadoFlecha(self, estado: int) -> None:
        self.estadoFlecha = estado
        
    def moverFlecha(self, direccion: int) -> None:
        """ Cambia el estado de la flecha dependiendo de su estado actual """
        if direccion == self.getDirecciones().ARRIBA:
            if self.getEstadoFlecha() == EstadosFlecha.JUGAR:
                self.setEstadoFlecha(EstadosFlecha.SALIR)
            elif self.getEstadoFlecha() == EstadosFlecha.SALIR:
                self.setEstadoFlecha(EstadosFlecha.JUGAR)
        elif direccion == self.getDirecciones().ABAJO:
            if self.getEstadoFlecha() == EstadosFlecha.JUGAR:
                self.setEstadoFlecha(EstadosFlecha.SALIR)
            elif self.getEstadoFlecha() == EstadosFlecha.SALIR:
                self.setEstadoFlecha(EstadosFlecha.JUGAR)