from .Ataques import Ataque
from ...constantes.estadosPokemon import EstadosPokemon

class Pokemon(Bloque):
    def __init__(self) -> None:
        super().__init__()
        self.ataques: Ataques = Ataque()
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
        