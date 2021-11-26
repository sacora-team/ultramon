from pygame import display

from .entidades.Habitacion import Habitacion
from .entidades.personaje.Inventario import Inventario
from .entidades.base.VistaBase import VistaBase
from .entidades.base.Bloque import Bloque
from .constantes.imagenes import Imagenes
from .constantes.habitaciones import Habitaciones
from .constantes.bloques import Bloques
from .entidades.personaje.Personaje import Personaje
from .constantes.direcciones import Direcciones
from .entidades.Mapa import Mapa
from .constantes.zooms import Zooms


class AppVista(VistaBase):
    def __init__(self) -> None:
        super().__init__()
        self.mapa = Mapa()
        self.personaje = Personaje()
        self.bloque = Bloque()

        self.maxZoom = 24
        self.minZoom = 18
        
        self.habitacionActual = Habitaciones.HALL
        
        self.definido = False
        self.renderizado = False
        
    def getDefinido(self):
        return self.definido
    
    def setDefinido(self, bool: bool):
        self.definido = bool
        
    def getBloque(self) -> Bloque:
        return self.bloque
    
    def getHabitacionClase(self) -> Habitacion:
        return self.getMapaClase().getHabitacion()
    
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
    
    def getInventarioAsh(self) -> Inventario:
        return self.getPersonaje().getInventario()
    
    def getMapaClase(self) -> Mapa:
        return self.mapa
    
    def getMapa(self) -> list[list[Bloque]]:
        return self.mapa.getMapa()
    
    def getPersonaje(self) -> Personaje:
        return self.personaje

    def limpiarDefiniciones(self) -> None:
        self.getMapaClase().limpiarDefiniciones()
        
    def comenzar(self):
        if self.definido or self.renderizado:
            return
        self.definirHabitacion()
        self.renderizarHabitacion(Imagenes.ASH_DER1)
    
    
    def definirHabitacion(self) -> None:
        """ Dada una habitacion, define sus bloques """
        
        if self.definido:
            return
        
        self.getMapaClase().definirHabitacion(self.habitacionActual)

        self.definido = True


    def renderizarHabitacion(self, imagenAsh: int) -> None:
        """" Dada una habitacion, la renderiza en pantalla """
        
        if self.renderizado:
            return
        
        self.getMapaClase().renderizarHabitacion(imagenAsh, self.getColumnaPersonaje(), self.getFilaPersonaje())
            
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
        
        if direccion == Direcciones.ABAJO:
            # Renderiza pasto encima
            self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            # Mueve al personaje
            if self.getMapa()[self.getFilaPersonaje() + 1][self.getColumnaPersonaje()].getTipo() == Bloques.PASTO:
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
            if self.getMapa()[self.getFilaPersonaje() - 1][self.getColumnaPersonaje()].getTipo() == Bloques.PASTO:
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
            if self.habitacionActual == Habitaciones.PRIMERA and self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() - 1].getTipo() == Bloques.CAMBIO_A_HALL:
                self.onCambiarHabitacion(Habitaciones.HALL)
            
            else: 
            
                # Mueve al personaje
                if self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() - 1].getTipo() == Bloques.PASTO:
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
            if self.habitacionActual == Habitaciones.HALL and self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() + 1].getTipo() == Bloques.CAMBIO_A_PRIMERA:
                self.onCambiarHabitacion(Habitaciones.PRIMERA)
            
            else:
            
                # Mueve al personaje
                if self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() + 1].getTipo() == Bloques.PASTO:
                    self.getPersonaje().moverPersonaje(direccion)
                    self.renderizarImagen(Imagenes.ASH_DER1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
                else:
                    # Cambia la direccion
                    self.renderizarImagen(Imagenes.ASH_DER1, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))

            self.getPersonaje().setDireccionActual(Direcciones.DERECHA)


    def seleccionar(self) -> None:
        """ Se ejecuta cuando se clickea enter """
        if self.getDireccionPersonaje() == Direcciones.ABAJO:
            
            # Se selecciona un arbol-pokebola
            if self.getMapa()[self.getFilaPersonaje() + 1][self.getColumnaPersonaje()].getTipo() == Bloques.COFRE:
                self.getMapa()[14 // 4][6].setTipo(Bloques.POKEBOLA)
                self.getHabitacionClase().setCofreHallAbierto(True)
                self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() + self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))
                self.renderizarImagen(Imagenes.ULTRABALL, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() + self.getAltoBloque()), (self.getAnchoBloque() // 2, self.getAltoBloque() // 2))
            
            # Se selecciona una pokebola
            elif self.getMapa()[self.getFilaPersonaje() + 1][self.getColumnaPersonaje()].getTipo() == Bloques.POKEBOLA:
                self.getMapa()[14 // 4][6].setTipo(Bloques.PASTO)
                self.getHabitacionClase().setPokebolaHallAgarrada(True)
                
                if (self.getInventarioAsh().inventarioConEspacio()):
                    self.getInventarioAsh().agregarItem(Bloques.POKEBOLA)
                
                self.renderizarImagen(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() + self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))

        elif self.getDireccionPersonaje() == Direcciones.ARRIBA:
            
            # Se selecciona un arbol-pokebola
            if self.getMapa()[self.getFilaPersonaje() - 1][self.getColumnaPersonaje()].getTipo() == Bloques.COFRE:
                self.getMapa()[14 // 4][6].setTipo(Bloques.POKEBOLA)
                self.getHabitacionClase().setCofreHallAbierto(True)
                self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() - self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))
                self.renderizarImagen(Imagenes.ULTRABALL, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() - self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))
            
            # Se selecciona una pokebola
            elif self.getMapa()[self.getFilaPersonaje() - 1][self.getColumnaPersonaje()].getTipo() == Bloques.POKEBOLA:
                self.getMapa()[14 // 4][6].setTipo(Bloques.PASTO)
                self.getHabitacionClase().setPokebolaHallAgarrada(True)
                
                if (self.getInventarioAsh().inventarioConEspacio()):
                    self.getInventarioAsh().agregarItem(Bloques.POKEBOLA)
                
                self.renderizarImagen(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() - self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))
            
            # Se selecciona un charmander
            elif self.getMapa()[self.getFilaPersonaje() - 1][self.getColumnaPersonaje()].getTipo() == Bloques.CHARMANDER:
                self.getMapa()[14 // 4][6].setTipo(Bloques.PASTO)
                self.getHabitacionClase().setCharmanderPrimeraAgarrada(True)
                
                if (self.getInventarioAsh().inventarioConEspacio()):
                    self.getInventarioAsh().agregarItem(Bloques.CHARMANDER)
                
                self.renderizarImagen(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() - self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))
                
            # Se selecciona un pikachu
            elif self.getMapa()[self.getFilaPersonaje() - 1][self.getColumnaPersonaje()].getTipo() == Bloques.PIKACHU:
                self.getMapa()[14 // 4][6].setTipo(Bloques.PASTO)
                self.getHabitacionClase().setPikachuPrimeraAgarrado(True)
                
                if (self.getInventarioAsh().inventarioConEspacio()):
                    self.getInventarioAsh().agregarItem(Bloques.PIKACHU)
                
                self.renderizarImagen(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() - self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))
            
            # Se selecciona un pajaro
            elif self.getMapa()[self.getFilaPersonaje() - 1][self.getColumnaPersonaje()].getTipo() == Bloques.PAJARO:
                self.getMapa()[14 // 4][6].setTipo(Bloques.PASTO)
                self.getHabitacionClase().setPajaroPrimeraAgarrado(True)
                
                if (self.getInventarioAsh().inventarioConEspacio()):
                    self.getInventarioAsh().agregarItem(Bloques.PAJARO)
                
                self.renderizarImagen(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje()), (self.getAltoBloque() * self.getFilaPersonaje() - self.getAltoBloque()), (self.getAnchoBloque(), self.getAltoBloque()))
            
        elif self.getDireccionPersonaje() == Direcciones.IZQUIERDA:
            
            # Se selecciona un arbol pokebola
            if self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() - 1].getTipo() == Bloques.COFRE:
                self.getMapa()[14 // 4][6].setTipo(Bloques.POKEBOLA)
                self.getHabitacionClase().setCofreHallAbierto(True)
                self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje() - self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
                self.renderizarImagen(Imagenes.ULTRABALL, (self.getAnchoBloque() * self.getColumnaPersonaje() - self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))

            # Se selecciona una pokebola
            elif self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() - 1].getTipo() == Bloques.POKEBOLA:
                self.getMapa()[14 // 4][6].setTipo(Bloques.PASTO)
                self.getHabitacionClase().setPokebolaHallAgarrada(True)
                
                if (self.getInventarioAsh().inventarioConEspacio()):
                    self.getInventarioAsh().agregarItem(Bloques.POKEBOLA)
                
                self.renderizarImagen(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje() - self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
            
        elif self.getDireccionPersonaje() == Direcciones.DERECHA:
            
            # Se selecciona un arbol pokebola
            if self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() + 1].getTipo() == Bloques.COFRE:
                self.getMapa()[14 // 4][6].setTipo(Bloques.POKEBOLA)
                self.getHabitacionClase().setCofreHallAbierto(True)
                self.renderizarImagenSinUpdate(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje() + self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
                self.renderizarImagen(Imagenes.ULTRABALL, (self.getAnchoBloque() * self.getColumnaPersonaje() + self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))
                
            # Se selecciona una pokebola
            elif self.getMapa()[self.getFilaPersonaje()][self.getColumnaPersonaje() + 1].getTipo() == Bloques.POKEBOLA:
                self.getMapa()[14 // 4][6].setTipo(Bloques.PASTO)
                self.getHabitacionClase().setPokebolaHallAgarrada(True)
                
                if (self.getInventarioAsh().inventarioConEspacio()):
                    self.getInventarioAsh().agregarItem(Bloques.POKEBOLA)
                
                self.renderizarImagen(Imagenes.PASTO, (self.getAnchoBloque() * self.getColumnaPersonaje() + self.getAnchoBloque()), (self.getAltoBloque() * self.getFilaPersonaje()), (self.getAnchoBloque(), self.getAltoBloque()))


    def zoom(self, accion: int):
        """ Zoom del juego """
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