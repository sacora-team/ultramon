from src.AppController import AppController
from platform import system
import ctypes
from src.constantes.sistemasOperativos import SistemasOperativos

sistema = system()

if sistema == SistemasOperativos.WINDOWS:
    appid = u"ultramon"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)


if __name__ == "__main__":
    AppController().iniciarJuego()
