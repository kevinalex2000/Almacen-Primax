
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from Menu.MenuPrincipal import MenuPrincipal
from Helpers import Helpers

menuPrincipal = MenuPrincipal()

loginExitoso = False
print("\nIniciar Sesión para continuar...")

while loginExitoso == False:
	
	usuario = input("\nNombre de Usuario: ")
	contraseña = input("Contraseña: ")

	if (usuario == "admin" and contraseña == "admin"):
		loginExitoso = True
	else:
		Helpers.MensajeError("\nEl usuario o contraseña no coinciden.")
		input("Pulsa Enter para volver a intentar...")

result = menuPrincipal.Mostrar()

if result == False:
	sys.exit()