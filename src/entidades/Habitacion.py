class Habitacion():
    def __init__(self) -> None:
        self.cofreHallAbierto = False
        self.pokebolaHallAgarrada = False
        self.charmanderPrimeraAgarrado = False
        self.pikachuPrimeraAgarrado = False
        self.pajaroPrimeraAgarrado = False
        
    def getPajaroPrimeraAgarrado(self) -> bool:
        return self.pajaroPrimeraAgarrado
    
    def setPajaroPrimeraAgarrado(self, bool: bool) -> None:
        self.pajaroPrimeraAgarrado = bool
        
    def getCharmanderPrimeraAgarrado(self) -> bool:
        return self.charmanderPrimeraAgarrado
    
    def setCharmanderPrimeraAgarrada(self, bool: bool) -> None:
        self.charmanderPrimeraAgarrado = bool
        
    def getPikachuPrimeraAgarrado(self) -> bool:
        return self.pikachuPrimeraAgarrado
    
    def setPikachuPrimeraAgarrado(self, bool: bool) -> None:
        self.pikachuPrimeraAgarrado = bool
        
    def getPokebolaHallAgarrada(self) -> bool:
        return self.pokebolaHallAgarrada
    
    def setPokebolaHallAgarrada(self, bool: bool) -> None:
        self.pokebolaHallAgarrada = bool
        
    def getCofreHallAbierto(self) -> bool:
        return self.cofreHallAbierto
    
    def setCofreHallAbierto(self, bool: bool) -> None:
        self.cofreHallAbierto = bool