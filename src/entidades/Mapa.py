from .base.VistaBase import VistaBase
from .base.Bloque import Bloque
from .Habitacion import Habitacion
from ..constantes.bloques import Bloques
from ..constantes.imagenes import Imagenes
from ..constantes.habitaciones import Habitaciones

class Mapa(VistaBase):
    def __init__(self) -> None:
        self.mapa = []
        self.habitacion = Habitacion()
        self.bloque = Bloque()
        super().__init__()
        
    def getMapa(self) -> list:
        return self.mapa
    
    def getBloque(self) -> Bloque:
        return self.bloque
    
    def getHabitacion(self) -> Habitacion:
        return self.habitacion
    
    def limpiarDefiniciones(self) -> None:
        self.mapa = []
        
    def getAnchoBloque(self) -> int:
        return self.getBloque().getAnchoBloque()
    
    def getAltoBloque(self) -> int:
        return self.getBloque().getAltoBloque()
    
    def renderizarHabitacion(self, imagenAsh, columnaPersonaje, filaPersonaje) -> None:
        for fila in range(0, self.getCantidadFilas()):
            for columna in range(0, self.getCantidadColumnas()):
                if self.getMapa()[fila][columna] in [Bloques.COFRE, Bloques.PASTO, Bloques.CAMBIO_A_PRIMERA, Bloques.CAMBIO_A_HALL]:
                    self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.AGUA:
                    self.renderizarImagenSinUpdate(Imagenes.AGUA, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] in [Bloques.ARBOL, Bloques.ARBOL_POKEBOLA]:
                    self.renderizarImagenSinUpdate(Imagenes.ARBOL, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.FUENTE:
                    self.renderizarImagenSinUpdate(Imagenes.FUENTE, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.PIEDRA:
                    self.renderizarImagenSinUpdate(Imagenes.PIEDRA, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.POKEBOLA:
                    self.renderizarImagenSinUpdate(Imagenes.ULTRABALL, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.COFRE:
                    self.renderizarImagenSinUpdate(Imagenes.COFRE, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.CHARMANDER:
                    self.renderizarImagenSinUpdate(Imagenes.CHARMANDER, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.PIKACHU:
                    self.renderizarImagenSinUpdate(Imagenes.PIKACHU, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.PAJARO:
                    self.renderizarImagenSinUpdate(Imagenes.PAJARO, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.MAESTRO:
                    self.renderizarImagenSinUpdate(Imagenes.MAESTRO, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.COMPAÑERA:
                    self.renderizarImagenSinUpdate(Imagenes.COMPAÑERA, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
               
        self.renderizarImagen(imagenAsh, (self.getAnchoBloque() * columnaPersonaje), (self.getAltoBloque() * filaPersonaje), (self.getAnchoBloque(), self.getAltoBloque()))
        
    
    
    def definirHabitacion(self, habitacion: int) -> None:
        """ Dada una habitacion, define sus bloques """
        if habitacion == Habitaciones.HALL:
            
            for fila in range(0, 14):
                self.getMapa().append([])
                for columna in range(0, 24):
                    self.getMapa()[fila].append(Bloques.PASTO)
        
            for fila in range(1, 2):
                for columna in range(0, 24):
                    self.getMapa()[fila][columna] = Bloques.AGUA
        
            for fila in range(12, 13):
                for columna in range(0, 24):
                    self.getMapa()[fila][columna] = Bloques.AGUA

            for fila in range(0, 1):
                for columna in range(0, 24):
                    self.getMapa()[fila][columna] = Bloques.ARBOL
        
            for fila in range(13, 14):
                for columna in range(0, 24):
                    self.getMapa()[fila][columna] = Bloques.ARBOL

            for fila in range(0, 14):
                for columna in range(0, 1):
                    self.getMapa()[fila][columna] = Bloques.ARBOL

            for fila in range(0, 14):
                for columna in range(23, 24):
                    self.getMapa()[fila][columna] = Bloques.ARBOL

            self.getMapa()[10][23] = Bloques.PASTO
            self.getMapa()[7][12] = Bloques.FUENTE
            self.getMapa()[14 // 3][8] = Bloques.ARBOL
            self.getMapa()[4][21] = Bloques.MAESTRO
            self.getMapa()[7][21] = Bloques.COMPAÑERA
            
            if not self.getHabitacion().getCofreHallAbierto():
                self.getMapa()[14 // 4][6] = Bloques.COFRE
            elif self.getHabitacion().getCofreHallAbierto() and not self.getHabitacion().getPokebolaHallAgarrada():
                self.getMapa()[14 // 4][6] = Bloques.POKEBOLA
            elif self.getHabitacion().getCofreHallAbierto() and self.getHabitacion().getPokebolaHallAgarrada:
                self.getMapa()[14 // 4][6] = Bloques.PASTO
            
            self.getMapa()[10][23] = Bloques.CAMBIO_A_PRIMERA
        
        elif habitacion == Habitaciones.PRIMERA:
            
            for fila in range(0, 24):
                self.getMapa().append([])
                for columna in range(0, 24):
                    self.getMapa()[fila].append(Bloques.PASTO)

            for fila in range(5, 8):
                for columna in range(10, 13):
                    self.getMapa()[fila][columna] = Bloques.AGUA

            for fila in range(0, 14):
                for columna in range(0, 1):
                    self.getMapa()[fila][columna] = Bloques.ARBOL

            for fila in range(0, 1):
                for columna in range(1, 24):
                    self.getMapa()[fila][columna] = Bloques.PIEDRA

            for fila in range(13, 14):
                for columna in range(1, 24):
                    self.getMapa()[fila][columna] = Bloques.PIEDRA

            for fila in range(0, 14):
                for columna in range(23, 24):
                    self.getMapa()[fila][columna] = Bloques.PIEDRA

            for fila in range(1, 2):
                for columna in range(8, 14):
                    self.getMapa()[fila][columna] = Bloques.AGUA

            for fila in range(5, 6):
                for columna in range(4, 8):
                    self.getMapa()[fila][columna] = Bloques.AGUA

            for fila in range(6, 8):
                for columna in range(8, 9):
                    self.getMapa()[fila][columna] = Bloques.AGUA

            for fila in range(8, 10):
                for columna in range(8, 9):
                    self.getMapa()[fila][columna] = Bloques.AGUA

            for fila in range(14, 16):
                for columna in range(8, 9):
                    self.getMapa()[fila][columna] = Bloques.AGUA

            for fila in range(9, 10):
                for columna in range(9, 22):
                    self.getMapa()[fila][columna] = Bloques.AGUA

            for fila in range(3, 4):
                for columna in range(15, 20):
                    self.getMapa()[fila][columna] = Bloques.AGUA

            self.getMapa()[2][8] = Bloques.AGUA
            self.getMapa()[2][14] = Bloques.AGUA
            self.getMapa()[3][8] = Bloques.AGUA
            self.getMapa()[3][10] = Bloques.AGUA
            self.getMapa()[3][12] = Bloques.AGUA
            self.getMapa()[3][14] = Bloques.AGUA
            self.getMapa()[1][14] = Bloques.AGUA
            self.getMapa()[4][8] = Bloques.AGUA
            self.getMapa()[4][14] = Bloques.AGUA
            self.getMapa()[5][8] = Bloques.AGUA
            self.getMapa()[5][14] = Bloques.AGUA
            self.getMapa()[6][4] = Bloques.AGUA
            self.getMapa()[5][4] = Bloques.AGUA
            self.getMapa()[8][4] = Bloques.AGUA
            self.getMapa()[7][4] = Bloques.AGUA
            self.getMapa()[8][5] = Bloques.AGUA
            self.getMapa()[8][9] = Bloques.AGUA
            self.getMapa()[8][10] = Bloques.AGUA
            self.getMapa()[6][14] = Bloques.AGUA
            self.getMapa()[6][15] = Bloques.AGUA
            self.getMapa()[6][16] = Bloques.AGUA
            self.getMapa()[6][17] = Bloques.AGUA
            self.getMapa()[6][18] = Bloques.AGUA
            self.getMapa()[6][19] = Bloques.AGUA
            self.getMapa()[5][19] = Bloques.AGUA
            self.getMapa()[5][20] = Bloques.AGUA
            self.getMapa()[8][21] = Bloques.AGUA
            self.getMapa()[7][14] = Bloques.AGUA
            self.getMapa()[7][15] = Bloques.AGUA
            self.getMapa()[3][20] = Bloques.AGUA
            self.getMapa()[4][20] = Bloques.AGUA
            self.getMapa()[2][10] = Bloques.AGUA
            self.getMapa()[2][12] = Bloques.AGUA

            self.getMapa()[5][14] = Bloques.PASTO

            self.getMapa()[7][5] = Bloques.ARBOL
            self.getMapa()[7][7] = Bloques.ARBOL
            self.getMapa()[7][18] = Bloques.ARBOL
            self.getMapa()[7][16] = Bloques.ARBOL
            self.getMapa()[3][3] = Bloques.PIEDRA

            if not self.getHabitacion().getCharmanderPrimeraAgarrado():
                self.getMapa()[2][9] = Bloques.CHARMANDER
                
            if not self.getHabitacion().getPikachuPrimeraAgarrado():
                self.getMapa()[2][11] = Bloques.PIKACHU
                
            if not self.getHabitacion().getPajaroPrimeraAgarrado():
                self.getMapa()[2][13] = Bloques.PAJARO

            self.getMapa()[11][0] = Bloques.CAMBIO_A_HALL