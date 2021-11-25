from .Ataque import Ataque
from ...constantes.estadosPokemon import EstadosPokemon

class Pokemon():
    def __init__(self) -> None:
        self.ataques: Ataque = Ataque()
        self.vida = 50
        self.estado = EstadosPokemon()

    def getVida(self):
        return self.vida

    def setVida(self, vida: int):
        self.vida = vida
    
    def getEstado(self):
        return self.estado

    def setEstado(self, estado: int):
        self.estado = estado

    def atacar(self) -> None:
        pass

    def recibirAtaque(self, ataque: int) -> None:
        if ataque > self.getVida():
            self.setEstado(EstadosPokemon.MUERTO)
        else:
            self.setVida(self.getVida() - ataque)
        