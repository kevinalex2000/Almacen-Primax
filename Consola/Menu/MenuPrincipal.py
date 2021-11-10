from Helpers import Helpers
from Menu.MenuMantenimientoProductos import MenuMantenimientoProductos

class MenuPrincipal:
    
    def __init__(self):
        self.menuMantenimientoProductos = MenuMantenimientoProductos()
    
    def Mostrar(self):
        Helpers.Limpiar()
        Helpers.MensajeBienvenida()
        print ("\nMenu Principal: \n")
        print ("1 - Mantenimiento de Productos")
        print ("2 - Registrar Compras")
        print ("3 - Registrar Ventas")
        print ("4 - Estadisticas")
        print ("5 - Historial")
        print ("0 - salir\n")

        opcionElegida = input("Selecciona una opcion para continuar: ")
        
        result = True

        if opcionElegida == '1':
            result = self.menuMantenimientoProductos.Mostrar()
        elif opcionElegida == '0':
            return False
        else:
            Helpers.MensajeError("Ha escrito una opcion incorrecta.")
            input("Pulsa Enter para volver a intentar...")
            self.Mostrar()

        if result == False:
            return self.Mostrar()