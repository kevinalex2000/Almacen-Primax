from Helpers import Helpers

class MenuMantenimientoProductos:

    def __init__(self):
        self.helpers = Helpers()

    def Mostrar(self):
        self.helpers.Clear()
        print ("\nMantenimiento de Productos: \n")
        print ("1 - Editar")
        print ("2 - Eliminar")
        print ("0 - Salir\n")

        opcionElegida = input("Selecciona una opcion para continuar: ")
        