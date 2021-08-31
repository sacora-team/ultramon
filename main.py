import ctypes
from src.ControllerBase import ControllerBase

appid = u"ultramon"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

if __name__ == "__main__":
    ControllerBase().iniciarJuego()
