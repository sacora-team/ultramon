from ..base.ControllerBase import ControllerBase
from .PersonajeVista import PersonajeVista
from .Personaje import Personaje


class PersonajeController(ControllerBase):
    def __init__(self) -> None:
        super().__init__()
        self.entidad = Personaje()
        self.vista = PersonajeVista()
        
    def getVista(self) -> PersonajeVista:
        return self.vista

    def getEntidad(self) -> Personaje:
        return self.entidad
        
    def getActivado(self) -> bool:
        return self.activado

    def setActivado(self, activado: bool) -> None:
        self.activado = activado
        
    def loop(self) -> None:
        self.getVista().limpiarPantalla()
            
    def activar(self) -> None:
        """ Se activa el ciclo de vida de la instancia """
        self.setActivado(True)
        self.loop()