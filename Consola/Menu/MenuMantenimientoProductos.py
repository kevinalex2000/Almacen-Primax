from Helpers import Helpers

class MenuMantenimientoProductos:
        
    def Mostrar(self):

        Helpers.Limpiar()
        Helpers.MensajeBienvenida()
        print ("\nMantenimiento de Productos: \n")
        print ("1 - Editar")
        print ("2 - Eliminar")
        print ("0 - Atras\n")

        opcionElegida = input("Selecciona una opcion para continuar: ")
        
        if opcionElegida == '0':
            return False
        else:
            Helpers.MensajeError("Ha escrito una opcion incorrecta.")
            input("Pulsa Enter para volver a intentar...")
            return self.Mostrar()