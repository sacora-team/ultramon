from src.AppController import AppController
from platform import system
from ctypes import windll
from src.constantes.sistemasOperativos import SistemasOperativos

sistema = system()

# Se cambia el id de la aplicacion para que windows no superponga el del juego
if sistema == SistemasOperativos.WINDOWS:
    appid = u"ultramon"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)


if __name__ == "__main__":
    AppController().iniciarJuego()
