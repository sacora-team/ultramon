from pygame import Surface, image, transform
from ..base.Bloque import Bloque

class Pasto(Bloque):
    def __init__(self) -> None:
        super().__init__()
        self.sprite = 'assets/relieves/pasto.png'
        
    def getSprite(self) -> str:
        return self.sprite