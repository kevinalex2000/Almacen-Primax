import os
from Static.Colores import Colores

class Helpers:
    
    @staticmethod
    def Limpiar():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def MensajeBienvenida():
        print(Colores.OK + "\n¡Bienvenido a los Almacenes!" + Colores.RESET)

    @staticmethod
    def MensajeError(texto):
        print(Colores.FAIL + texto + Colores.RESET)