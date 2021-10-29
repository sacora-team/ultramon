from pygame import display
from .entidades.base.VistaBase import VistaBase
from .entidades.base.Bloque import Bloque
from .constantes.imagenes import Imagenes
from .constantes.habitaciones import Habitaciones
from .constantes.bloques import Bloques
from .entidades.bloques.Personaje import Personaje
from .constantes.direcciones import Direcciones
from .constantes.zooms import Zooms


class AppVista(VistaBase):
    def __init__(self) -> None:
        super().__init__()
        self.mapa = []
        self.personaje = Personaje()
        self.bloque = Bloque()
        
        self.caminables = [Bloques.PASTO, Bloques.TIERRA]

        self.maxZoom = 24
        self.minZoom = 18
        
        self.definido = False
        self.renderizado = False
        
    def getDefinido(self):
        return self.definido
    
    def setDefinido(self, bool: bool):
        self.definido = bool
    
    def getRenderizado(self):
        return self.renderizado
    
    def setRenderizado(self, bool: bool):
        self.renderizado = bool
        
    def getBloque(self) -> Bloque:
        return self.bloque
    
    def getAnchoBloque(self) -> int:
        return self.getBloque().getAnchoBloque()
    
    def getAltoBloque(self) -> int:
        return self.getBloque().getAltoBloque()
    
    def getColumnaPersonaje(self) -> int:
        return self.getPersonaje().getColumnaPersonaje()
    
    def getFilaPersonaje(self) -> int:
        return self.getPersonaje().getFilaPersonaje()
    
    def getMapa(self) -> list:
        return self.mapa
    
    def getPersonaje(self) -> Personaje:
        return self.personaje
    
    def definirHabitacion(self, habitacion: int) -> None:
        """ Dada una habitacion, define sus bloques """
        if self.getDefinido():
            return
        
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
            self.getMapa()[14 // 4][6] = Bloques.ARBOL
            self.getMapa()[14 // 3][8] = Bloques.ARBOL

            if self.getMapa()[5][5] == Bloques.PERSONAJE:
                habitacion = Habitaciones.PRIMERA
        
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

            for fila in range(0, 14):
                for columna in range(22, 23):
                    self.getMapa()[fila][columna] = Bloques.PIEDRA

            self.getMapa()[7][5] = Bloques.ARBOL
            self.getMapa()[7][7] = Bloques.ARBOL
            self.getMapa()[7][18] = Bloques.ARBOL
            self.getMapa()[7][16] = Bloques.ARBOL

            self.getMapa()[11][0] = Bloques.PUERTA  # Puerta

        self.setDefinido(True)
    

    def renderizarHabitacion(self, habitacion: int) -> None:
        """" Dada una habitacion, la renderiza en pantalla """
        if self.getRenderizado():
            return
        
        self.limpiarPantalla()
        
        for fila in range(0, self.getCantidadFilas()):
            for columna in range(0, self.getCantidadColumnas()):
                if self.getMapa()[fila][columna] == Bloques.PASTO:
                    self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.AGUA:
                    self.renderizarImagenSinUpdate(Imagenes.AGUA, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.ARBOL:
                    self.renderizarImagenSinUpdate(Imagenes.ARBOL, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.FUENTE:
                    self.renderizarImagenSinUpdate(Imagenes.FUENTE, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.PIEDRA:
                    self.renderizarImagenSinUpdate(Imagenes.PIEDRA, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))
                if self.getMapa()[fila][columna] == Bloques.PUERTA:
                    self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * columna), (self.getAltoBloque() * fila), (self.getAnchoBloque(), self.getAltoBloque()))

        if habitacion == Habitaciones.HALL:
            self.renderizarImagen(Imagenes.ASH_DER1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))

        elif habitacion == Habitaciones.PRIMERA:
            self.renderizarImagen(Imagenes.ASH_DER1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            
        display.update()
            
        self.setRenderizado(True)
        

    def onCambiarHabitacion(self):
        """ Debe ejecutarse antes de querer cambiar de habitacion """
        self.definido = False
        self.renderizado = False


    def moverPersonajeConVerificacion(self, direccion: int) -> None:
        """ Dada una direccion, verifica que sea caminable y mueve su posicion """
        if direccion == Direcciones.ABAJO:
            # Renderiza pasto encima
            self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            # Mueve al personaje
            if self.getMapa()[self.getFilaPersonaje() + 1][self.getColumnaPersonaje()] == Bloques.PASTO:
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(Imagenes.ASH_FR1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            else:
                # Cambia la direccion
                self.renderizarImagen(Imagenes.ASH_FR1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))

        elif direccion == Direcciones.ARRIBA:
            # Renderiza pasto encima
            self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            # Mueve al personaje
            if self.getMapa()[self.getFilaPersonaje() - 1][self.getColumnaPersonaje()] == Bloques.PASTO:
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(Imagenes.ASH_REV1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            else:
                # Cambia la direccion
                self.renderizarImagen(Imagenes.ASH_REV1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
                
        elif direccion == Direcciones.IZQUIERDA:
            # Renderiza pasto encima
            self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            # Mueve al personaje
            if self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() - 1] == Bloques.PASTO:
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(Imagenes.ASH_IZQ1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            else:
                # Cambia la direccion
                self.renderizarImagen(Imagenes.ASH_IZQ1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
                
        elif direccion == Direcciones.DERECHA:
            # Renderiza pasto encima
            self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            # Mueve al personaje
            if self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() + 1] == Bloques.PASTO:
                self.getPersonaje().moverPersonaje(direccion)
                self.renderizarImagen(Imagenes.ASH_DER1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            else:
                # Cambia la direccion
                self.renderizarImagen(Imagenes.ASH_DER1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))

    def zoom(self, accion: int):
        if accion == Zooms.MINIMIZAR:
            if self.getCantidadColumnas() != self.maxZoom:
                self.cantidadColumnas = self.cantidadColumnas + 1
                self.cantidadFilas = self.cantidadFilas + 1
                self.renderizado = False
                self.definido = False
                self.getBloque().actualizarMedidas(Zooms.MINIMIZAR)
                self.definirHabitacion(Habitaciones.HALL)
                self.renderizarHabitacion(Habitaciones.HALL)
        elif accion == Zooms.MAXIMIZAR:
            if self.getCantidadColumnas() != self.minZoom:
                self.cantidadColumnas = self.cantidadColumnas - 1
                self.cantidadFilas = self.cantidadFilas - 1
                self.renderizado = False
                self.definido = False
                self.getBloque().actualizarMedidas(Zooms.MAXIMIZAR)
                self.definirHabitacion(Habitaciones.HALL)
                self.renderizarHabitacion(Habitaciones.HALL)