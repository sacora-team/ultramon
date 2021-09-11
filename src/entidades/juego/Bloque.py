from pygame import transform, image

class Bloque:
    def __init__(self) -> None:
        self.ancho_bloque = 45
        self.alto_bloque = 45
        self.margen_bloque = 1
        
        self.pasto = transform.scale(image.load("assets/relieves/pasto.png"), (self.get_ancho_bloque(), self.get_alto_bloque()))  
        self.tierra = transform.scale(image.load("assets/relieves/tierra.png"), (self.get_ancho_bloque(), self.get_alto_bloque()))
        self.agua = transform.scale(image.load("assets/relieves/agua.png"), (self.get_ancho_bloque(), self.get_alto_bloque()))        
        self.arbol = transform.scale(image.load("assets/ambiente/arbol.png"), (self.get_ancho_bloque(), self.get_alto_bloque()))

    def get_ancho_bloque(self):
        return self.ancho_bloque

    def get_alto_bloque(self):
        return self.ancho_bloque

    def get_margen_bloque(self):
        return self.margen_bloque
