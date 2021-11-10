from Menu.MenuMantenimientoProductos import MenuMantenimientoProductos

class MenuPrincipal:
    
    def __init__(self):
        self.menuMantenimientoProductos = MenuMantenimientoProductos()
    
    def Mostrar(self):
        print ("\nMenu Principal: \n")
        print ("1 - Mantenimiento de Productos")
        print ("2 - Registrar Compras")
        print ("3 - Registrar Ventas")
        print ("4 - Estadisticas")
        print ("5 - Historial")
        print ("0 - salir\n")

        opcionElegida = input("Selecciona una opcion para continuar: ")
        
        if opcionElegida == '1':
            self.menuMantenimientoProductos.Mostrar()
