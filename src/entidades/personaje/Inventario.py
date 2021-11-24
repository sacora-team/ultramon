class Inventario():
    def __init__(self) -> None:
        self.inventario: list = []
        
    def getInventario(self) -> list:
        return self.inventario
    
    def inventarioConEspacio(self) -> bool:
        return len(self.getInventario()) < 6
      
    def agregarItem(self, item) -> None:
        self.inventario.append(item)
        print(self.getInventario())