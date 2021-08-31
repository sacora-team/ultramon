from pygame import (
    init,
    event,
    mixer,
    QUIT,
    KEYDOWN,
    K_RETURN,
    K_ESCAPE,
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
)

from .ViewBase import ViewBase


class ControllerBase:
    def __init__(self) -> None:
        init()
        self.ViewBase = ViewBase()
        self.ejecutandose: bool = True
        self.estado: str = "MENU"
        self.estados: tuple[str] = ("MENU", "JUEGO")
        self.setUpKey(False)
        self.setDownKey(False)
        self.setLeftKey(False)
        self.setRightKey(False)
        self.setSelectKey(False)
        self.setPauseKey(False)
        mixer.Channel(0).play(mixer.Sound("./assets/sonidos/opening.mp3"))

    def getView(self) -> ViewBase:
        return self.ViewBase

    def getEjecutandose(self) -> bool:
        return self.ejecutandose

    def setEjecutandose(self, bool: bool) -> None:
        self.ejecutandose = bool

    def getEstado(self) -> str:
        return self.estado

    def setEstado(self, estado: str) -> None:
        estado = estado.upper()
        if estado not in self.estados:
            raise ValueError(
                estado + " no es un estado permitido en " + str(self.estados)
            )
        self.estado = estado

    def iniciarJuego(self) -> None:
        self.loop()

    def loop(self) -> None:
        while self.ejecutandose:
            self.checkearEventos()

            if self.estado == "MENU":
                if self.getSelectKey():
                    print("Seleccionado!")
                    self.resetearKeys()
                elif self.getUpKey():
                    print("Arriba!")
                    self.resetearKeys()
                elif self.getDownKey():
                    print("Abajo!")
                    self.resetearKeys()

            if self.getEstado() == "JUEGO":
                pass

    def checkearEventos(self) -> None:
        for evento in event.get():
            if evento.type == QUIT:
                self.setEjecutandose(False)
            if evento.type == KEYDOWN:
                if evento.key == K_RETURN:
                    self.setSelectKey(True)
                if evento.key == K_ESCAPE:
                    self.setPauseKey(True)
                if evento.key == K_DOWN:
                    self.setDownKey(True)
                if evento.key == K_UP:
                    self.setUpKey(True)
                if evento.key == K_LEFT:
                    self.setLeftKey(True)
                if evento.key == K_RIGHT:
                    self.setRightKey(True)

    def resetearKeys(self) -> None:
        self.setUpKey(False)
        self.setDownKey(False)
        self.setLeftKey(False)
        self.setRightKey(False)
        self.setSelectKey(False)
        self.setPauseKey(False)

    ######################
    #       TECLAS       #
    ######################
    def setUpKey(self, estado: bool) -> None:
        self.upKey = estado

    def setDownKey(self, estado: bool) -> None:
        self.downKey = estado

    def setLeftKey(self, estado: bool) -> None:
        self.leftKey = estado

    def setRightKey(self, estado: bool) -> None:
        self.rightKey = estado

    def setSelectKey(self, estado: bool) -> None:
        self.startKey = estado

    def setPauseKey(self, estado: bool) -> None:
        self.backKey = estado

    def getUpKey(self) -> bool:
        return self.upKey

    def getDownKey(self) -> bool:
        return self.downKey

    def getLeftKey(self) -> bool:
        return self.leftKey

    def getRightKey(self) -> bool:
        return self.rightKey

    def getSelectKey(self) -> bool:
        return self.startKey

    def getPauseKey(self) -> bool:
        return self.backKey
