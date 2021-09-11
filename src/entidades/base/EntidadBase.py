from ...constantes.direcciones import Direcciones


class EntidadBase:
    def __init__(self) -> None:
        self.direcciones: Direcciones = Direcciones
        
    def getDirecciones(self) -> Direcciones:
        return self.direcciones