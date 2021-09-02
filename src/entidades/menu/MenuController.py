from ..base.ControllerBase import ControllerBase
from .MenuView import MenuView

class MenuController(ControllerBase):
    def __init__(self) -> None:
        super().__init__()
        self.activado: bool = False
        self.view = MenuView()
    
    def getView(self) -> MenuView:
        return self.view
    
    def getActivado(self) -> bool:
        return self.activado
    
    def setActivado(self, activado: bool) -> None:
        self.activado = activado
    
    def loop(self) -> None:
        self.getView().renderizarMenuPrincipal()
        while self.getActivado():
            self.chequearEventos()
            if self.getUpKey():
                print("arriba")
                self.resetearKeys()
            if self.getDownKey():
                print("abajo")
                self.resetearKeys()
    
    def activar(self) -> None:
        self.setActivado(True)
        self.loop()