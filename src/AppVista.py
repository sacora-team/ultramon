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
        
        self.habitacionActual = Habitaciones.HALL
        
        self.cofreHallAbierto = False
        self.pokebolaHallAgarrada = False
        
        self.definido = False
        self.renderizado = False
        
    def getDefinido(self):
        return self.definido
    
    def setDefinido(self, bool: bool):
        self.definido = bool
        
    def getBloque(self) -> Bloque:
        return self.bloque
    
    def getDireccionPersonaje(self) -> int:
        return self.getPersonaje().getDireccionActual()
    
    def getAnchoBloque(self) -> int:
        return self.getBloque().getAnchoBloque()
    
    def getAltoBloque(self) -> int:
        return self.getBloque().getAltoBloque()
    
    def getColumnaPersonaje(self) -> int:
        return self.getPersonaje().getColumnaPersonaje()
    
    def getFilaPersonaje(self) -> int:
        return self.getPersonaje().getFilaPersonaje()
    
    def getPokebolaHallAgarrada(self) -> bool:
        return self.pokebolaHallAgarrada
    
    def setPokebolaHallAgarrada(self, bool: bool) -> None:
        self.pokebolaHallAgarrada = bool
        
    def getCofreHallAbierto(self) -> bool:
        return self.cofreHallAbierto
    
    def setCofreHallAbierto(self, bool: bool) -> None:
        self.cofreHallAbierto = bool
    
    def getMapa(self) -> list:
        return self.mapa
    
    def getPersonaje(self) -> Personaje:
        return self.personaje

    def limpiarDefiniciones(self) -> None:
        self.mapa = []
        
    def comenzar(self):
        if self.definido or self.renderizado:
            return
        self.definirHabitacion()
        self.renderizarHabitacion(Imagenes.ASH_DER1)
    
    
    def definirHabitacion(self) -> None:
        """ Dada una habitacion, define sus bloques """
        
        # TODO: Modularizar
        
        if self.definido:
            return
                 
        if self.habitacionActual == Habitaciones.HALL:            
            
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
            
            if not self.getCofreHallAbierto():
                self.getMapa()[14 // 4][6] = Bloques.COFRE
            elif self.getCofreHallAbierto() and not self.getPokebolaHallAgarrada():
                self.getMapa()[14 // 4][6] = Bloques.POKEBOLA
            elif self.getCofreHallAbierto() and self.getPokebolaHallAgarrada:
                self.getMapa()[14 // 4][6] = Bloques.PASTO
            
            self.getMapa()[10][23] = Bloques.CAMBIO_A_PRIMERA
        elif self.habitacionActual == Habitaciones.PRIMERA:
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

            self.getMapa()[7][5] = Bloques.ARBOL
            self.getMapa()[7][7] = Bloques.ARBOL
            self.getMapa()[7][18] = Bloques.ARBOL
            self.getMapa()[7][16] = Bloques.ARBOL

            self.getMapa()[3][3] = Bloques.PIEDRA
            
            self.getMapa()[11][0] = Bloques.CAMBIO_A_HALL

            i = 0
            for i in range (0, 3):
                if i == 0:
                    self.getMapa()[4][3] = Bloques.PIEDRA
                    self.getMapa()[3][3] = Bloques.PASTO
                    i += 1
                    
                elif i == 1:
                    self.getMapa()[4][4] = Bloques.PIEDRA
                    self.getMapa()[4][3] = Bloques.PASTO
                    i += 1

                elif i == 2:
                    self.getMapa()[3][4] = Bloques.PIEDRA
                    self.getMapa()[4][4] = Bloques.PASTO
                    i += 1

                elif i == 3:
                    self.getMapa()[3][3] = Bloques.PIEDRA
                    self.getMapa()[3][4] = Bloques.PASTO
                    i = 0

        self.definido = True


    def renderizarHabitacion(self, imagenAsh: int) -> None:
        """" Dada una habitacion, la renderiza en pantalla """ 
        
        # TODO: Modulizar
        
        if self.renderizado:
            return
        
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
               
        self.renderizarImagen(imagenAsh, (self.getAnchoBloque() * self.getPersonaje().getColumnaPersonaje()), (self.getAltoBloque() * self.getPersonaje().getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            
        self.renderizado = True
        

    def onCambiarHabitacion(self, habitacion: int):
        """ Debe ejecutarse antes de querer cambiar de habitacion """
        self.definido = False
        self.renderizado = False
        self.limpiarDefiniciones()
        
        if self.habitacionActual == Habitaciones.HALL and habitacion == Habitaciones.PRIMERA:
            self.getPersonaje().setFilaPersonaje(self.getCantidadFilas() - 3)
            self.getPersonaje().setColumnaPersonaje(self.getCantidadColumnas() // 14)
            self.habitacionActual = Habitaciones.PRIMERA
            self.definirHabitacion()
            self.renderizarHabitacion(Imagenes.ASH_DER1)
            
        elif self.habitacionActual == Habitaciones.PRIMERA and habitacion == Habitaciones.HALL:
            self.getPersonaje().setFilaPersonaje(self.getCantidadFilas() - 4)
            self.getPersonaje().setColumnaPersonaje(self.getCantidadColumnas() // 2 + 10)
            self.habitacionActual = Habitaciones.HALL
            self.definirHabitacion()
            self.renderizarHabitacion(Imagenes.ASH_IZQ1)


    def moverPersonajeConVerificacion(self, direccion: int) -> None:
        """ Dada una direccion, verifica que sea caminable y mueve su posicion """

        # Verifica que el bloque sea pasto o tierra (caminables)
        # Cuando hace el movimiento, rellena el bloque anterior del personaje con el contenido del bloque sobre el que estaba        
        
        # TODO: Refactorizar
        
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
                
            self.getPersonaje().setDireccionActual(Direcciones.ABAJO)

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
                
            self.getPersonaje().setDireccionActual(Direcciones.ARRIBA)
                
            
        elif direccion == Direcciones.IZQUIERDA:
            # Renderiza pasto encima
            self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            
            # Cambia de hall a primera
            if self.habitacionActual == Habitaciones.PRIMERA and self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() - 1] == Bloques.CAMBIO_A_HALL:
                self.onCambiarHabitacion(Habitaciones.HALL)
            
            else: 
            
                # Mueve al personaje
                if self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() - 1] == Bloques.PASTO:
                    self.getPersonaje().moverPersonaje(direccion)
                    self.renderizarImagen(Imagenes.ASH_IZQ1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
                else:
                    # Cambia la direccion
                    self.renderizarImagen(Imagenes.ASH_IZQ1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            
            self.getPersonaje().setDireccionActual(Direcciones.IZQUIERDA)    
            
        elif direccion == Direcciones.DERECHA:
            # Renderiza pasto encima
            self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            
            # Cambia de hall a primera
            if self.habitacionActual == Habitaciones.HALL and self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() + 1] == Bloques.CAMBIO_A_PRIMERA:
                self.onCambiarHabitacion(Habitaciones.PRIMERA)
            
            else:
            
                # Mueve al personaje
                if self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() + 1] == Bloques.PASTO:
                    self.getPersonaje().moverPersonaje(direccion)
                    self.renderizarImagen(Imagenes.ASH_DER1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
                else:
                    # Cambia la direccion
                    self.renderizarImagen(Imagenes.ASH_DER1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))

            self.getPersonaje().setDireccionActual(Direcciones.DERECHA)


    def seleccionar(self) -> None:
        if self.getDireccionPersonaje() == Direcciones.ABAJO:
            
            # Se selecciona un arbol-pokebola
            if self.getMapa()[self.getFilaPersonaje() + 1][self.getColumnaPersonaje()] == Bloques.COFRE:
                self.getMapa()[14 // 4][6] = Bloques.POKEBOLA
                self.setCofreHallAbierto(True)
                self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() + self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))
                self.renderizarImagen(Imagenes.ULTRABALL, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() + self.getAltoBloque()), (self.getAnchoBloque() // 2, self.getAltoBloque() // 2))
            
            # Se selecciona una pokebola
            elif self.getMapa()[self.getFilaPersonaje() + 1][self.getColumnaPersonaje()] == Bloques.POKEBOLA:
                self.getMapa()[14 // 4][6] = Bloques.PASTO
                self.setPokebolaHallAgarrada(True)
                # TODO: Agregar pokebola a inventario
                self.renderizarImagen(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() + self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))

        elif self.getDireccionPersonaje() == Direcciones.ARRIBA:
            
            # Se selecciona un arbol-pokebola
            if self.getMapa()[self.getFilaPersonaje() - 1][self.getColumnaPersonaje()] == Bloques.COFRE:
                self.getMapa()[14 // 4][6] = Bloques.POKEBOLA
                self.setCofreHallAbierto(True)
                self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() - self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))
                self.renderizarImagen(Imagenes.ULTRABALL, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() - self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))
            
            # Se selecciona una pokebola
            elif self.getMapa()[self.getFilaPersonaje() - 1][self.getColumnaPersonaje()] == Bloques.POKEBOLA:
                self.getMapa()[14 // 4][6] = Bloques.PASTO
                self.setPokebolaHallAgarrada(True)
                # TODO: Agregar pokebola a inventario
                self.renderizarImagen(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() - self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))
            
        elif self.getDireccionPersonaje() == Direcciones.IZQUIERDA:
            
            # Se selecciona un arbol pokebola
            if self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() - 1] == Bloques.COFRE:
                self.getMapa()[14 // 4][6] = Bloques.POKEBOLA
                self.setCofreHallAbierto(True)
                self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje() - self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
                self.renderizarImagen(Imagenes.ULTRABALL, (self.getAnchoBloque() * self.getColumnaPersonaje() - self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))

            # Se selecciona una pokebola
            elif self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() - 1] == Bloques.POKEBOLA:
                self.getMapa()[14 // 4][6] = Bloques.PASTO
                self.setPokebolaHallAgarrada(True)
                # TODO: Agregar pokebola a inventario
                self.renderizarImagen(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje() - self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            
        elif self.getDireccionPersonaje() == Direcciones.DERECHA:
            
            # Se selecciona un arbol pokebola
            if self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() + 1] == Bloques.COFRE:
                self.getMapa()[14 // 4][6] = Bloques.POKEBOLA
                self.setCofreHallAbierto(True)
                self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje() + self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
                self.renderizarImagen(Imagenes.ULTRABALL, (self.getAnchoBloque() * self.getColumnaPersonaje() + self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
                
            # Se selecciona una pokebola
            elif self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() + 1] == Bloques.POKEBOLA:
                self.getMapa()[14 // 4][6] = Bloques.PASTO
                self.setPokebolaHallAgarrada(True)
                # TODO: Agregar pokebola a inventario
                self.renderizarImagen(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje() + self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))



    def zoom(self, accion: int):
        if accion == Zooms.MINIMIZAR:
            if self.getCantidadColumnas() != self.maxZoom:
                self.cantidadColumnas = self.cantidadColumnas + 1
                self.cantidadFilas = self.cantidadFilas + 1
                self.renderizado = False
                self.definido = False
                self.getBloque().actualizarMedidas(Zooms.MINIMIZAR)
                self.definirHabitacion()
                self.renderizarHabitacion(Imagenes.ASH_DER1)
        elif accion == Zooms.MAXIMIZAR:
            if self.getCantidadColumnas() != self.minZoom:
                self.cantidadColumnas = self.cantidadColumnas - 1
                self.cantidadFilas = self.cantidadFilas - 1
                self.renderizado = False
                self.definido = False
                self.getBloque().actualizarMedidas(Zooms.MAXIMIZAR)
                self.definirHabitacion()
                self.renderizarHabitacion(Imagenes.ASH_DER1)