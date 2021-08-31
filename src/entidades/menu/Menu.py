from pygame import Surface, Rect, display

##############
# PREVISORIO #
##############
class MenuPrincipal:
    def __init__(self, window: Surface) -> None:
        self.renderizado: bool = False
        self.window: Surface = window
        self.ultramonPos: tuple[int] = (self.getWindow().get_size()[0] // 2 - 170, self.getWindow().get_size()[1] // 6)
        self.jugarPos: tuple[int] = (self.getWindow().get_size()[0] // 2 - 70, window.get_size()[1] // 2 - 80)
        self.salirPos: tuple[int] = (window.get_size()[0] // 2 - 47, window.get_size()[1] // 2 + 80)
        self.offsetFlecha = -100
        self.flecha = Rect(self.getJugarPos()[0] + self.getOffsetFlecha(), self.getJugarPos()[1], 20, 20)
        self.estadoFlecha = "JUGAR"
        self.estadosFlecha: tuple[str] = (
            "JUGAR",
            "SALIR"
        )
        self.estadosMovimientosFlecha: tuple[str] = (
            "ARRIBA",
            "ABAJO"
        )
        
    def getFlecha(self) -> Rect:
        return self.flecha    
    
    def setFlecha(self, y: int) -> None:
        self.flecha.move(self.getFlecha().x, y)
    
    def getRenderizado(self) -> bool:
        return self.renderizado
        
    def getWindow(self) -> Surface:
        return self.window    
    
    def getOffsetFlecha(self) -> int:
        return self.offsetFlecha
    
    def getEstadoFlecha(self) -> str:
        return self.estadoFlecha
    
    def setEstadoFlecha(self, estado: str) -> None:
        estado = estado.upper()
        if estado not in self.estadosFlecha:
            return
        self.estadoFlecha = estado
    
    def getEstadosMovimientosFlecha(self) -> tuple[str]:
        return self.estadosMovimientosFlecha
    
    def getUltramonPos(self) -> tuple[int]:
        return self.ultramonPos
        
    def getJugarPos(self) -> tuple[int]:
        return self.jugarPos
    
    def getSalirPos(self) -> tuple[int]:
        return self.salirPos
    
    def moverFlecha(self, movimiento: str) -> None:
        # ARRIBA
        if movimiento == self.getEstadosMovimientosFlecha()[0]:
            print("Arriba")
            if self.getEstadoFlecha() == "JUGAR":
                print("me muevo a salir")
                self.setFlecha(self.getSalirPos()[1])
                self.setEstadoFlecha("SALIR")     
            elif self.getEstadoFlecha() == "SALIR":
                print("me muevo a jugar")
                self.setFlecha(self.getJugarPos()[1])
                self.setEstadoFlecha("JUGAR")       
        # ABAJO
        if movimiento == self.getEstadosMovimientosFlecha()[1]:
            print("abajo")
            if self.getEstadoFlecha() == "JUGAR":
                print("me muevo a salir")
                self.setFlecha(self.getSalirPos()[1])
                self.setEstadoFlecha("SALIR")     
            elif self.getEstadoFlecha() == "SALIR":
                print("me muevo a jugar")
                self.setFlecha(self.getJugarPos()[1])
                self.setEstadoFlecha("JUGAR")                
                 
        