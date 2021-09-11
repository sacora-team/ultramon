from pygame import (
    init,
    event,
    QUIT,
    KEYDOWN,
    K_RETURN,
    K_ESCAPE,
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
)

from ...constantes.estadosJuego import EstadosJuego


class ControllerBase:
    def __init__(self) -> None:
        init()
        self.ejecutandose: bool = True
        self.estado: int = EstadosJuego.MENU
        self.estados: EstadosJuego = EstadosJuego
        self.arriba: bool = False
        self.abajo: bool = False
        self.izquierda: bool = False
        self.derecha: bool = False
        self.seleccionar: bool = False
        self.atras: bool = False

    def onInicializarController(self) -> None:
        """ Codigo que se ejecutaria al inicializar la instancia """
        raise NotImplementedError

    def getEjecutandose(self) -> bool:
        return self.ejecutandose

    def setEjecutandose(self, bool: bool) -> None:
        self.ejecutandose = bool

    def getEstado(self) -> str:
        return self.estado

    def setEstado(self, estado: int) -> None:
        self.estado = estado

    def iniciarJuego(self) -> None:
        self.loop()

    def loop(self) -> None:
        """ Codigo que se ejecutaria durante el ciclo de vida entero de la instancia """
        raise NotImplementedError

    def chequearEventos(self) -> None:
        """ Lee que teclas se presionan """
        for evento in event.get():
            if evento.type == QUIT:
                self.setEjecutandose(False)
            if evento.type == KEYDOWN:
                if evento.key == K_RETURN:
                    self.setSeleccionar(True)
                if evento.key == K_ESCAPE:
                    self.setAtras(True)
                if evento.key == K_DOWN:
                    self.setAbajo(True)
                if evento.key == K_UP:
                    self.setArriba(True)
                if evento.key == K_LEFT:
                    self.setIzquierda(True)
                if evento.key == K_RIGHT:
                    self.setDerecha(True)

    def resetearKeys(self) -> None:
        self.setArriba(False)
        self.setAbajo(False)
        self.setIzquierda(False)
        self.setDerecha(False)
        self.setSeleccionar(False)
        self.setAtras(False)

    ######################
    #       TECLAS       #
    ######################
    def setArriba(self, estado: bool) -> None:
        self.arriba = estado

    def setAbajo(self, estado: bool) -> None:
        self.abajo = estado

    def setIzquierda(self, estado: bool) -> None:
        self.izquierda = estado

    def setDerecha(self, estado: bool) -> None:
        self.derecha = estado

    def setSeleccionar(self, estado: bool) -> None:
        self.seleccionar = estado

    def setAtras(self, estado: bool) -> None:
        self.atras = estado

    def getArriba(self) -> bool:
        return self.arriba

    def getAbajo(self) -> bool:
        return self.abajo

    def getIzquierda(self) -> bool:
        return self.izquierda

    def getDerecha(self) -> bool:
        return self.derecha

    def getSeleccionar(self) -> bool:
        return self.seleccionar

    def getAtras(self) -> bool:
        return self.atras
