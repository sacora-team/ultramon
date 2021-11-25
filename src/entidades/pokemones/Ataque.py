from ...constantes.ataques import Ataques

class Ataque:
    def __init__(self) -> None:
        self.ataque: list = [Ataques.LIVIANO, Ataques.INTENSO]

    def getAtaque(self) -> list:
        return self.ataque
    
    def generarAtaque(self, nombre: str, daño: int) -> None:
        pass