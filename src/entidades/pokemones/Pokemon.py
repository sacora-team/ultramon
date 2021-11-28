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

    def getAtaque(self):
        return self.ataques

    def atacar(self, nombre: str) -> None:
        if self.getEstado() == EstadosPokemon.VIVO:
            return self.getAtaque()

    def recibirAtaque(self, ataque: int) -> None:
        if ataque > self.getVida():
            self.setEstado(EstadosPokemon.MUERTO)
        else:
            self.setVida(self.getVida() - ataque)
        