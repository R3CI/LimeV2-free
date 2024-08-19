from core import *

class cmd:
    def title(title: str):
        ctypes.windll.kernel32.SetConsoleTitleW(title)

    def cls():
        os.system('cls')