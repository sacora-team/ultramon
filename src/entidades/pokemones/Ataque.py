from ...constantes.ataques import Ataques

class Ataque:
    def __init__(self) -> None:
        self.ataque: list = [Ataques.LIVIANO, Ataques.INTENSO]

    def getAtaque(self) -> list:
        return self.ataque

    def generarAtaque(self, tipo: str, nombre: str, daño: int) -> None:
        if tipo == Ataques.LIVIANO:
            return nombre, self.getAtaque(tipo)
        elif tipo == Ataques.INTENSO:
            return nombre, self.getAtaque(tipo) * 1,5