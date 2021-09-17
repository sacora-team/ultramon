from pygame import Surface, image, transform
from ..base.Bloque import Bloque

class Agua(Bloque):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = 'assets/relieves/agua.png'
        self.caminable: bool = False
        
    def getSprite(self) -> str:
        return self.sprite