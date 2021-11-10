
#!/usr/bin/python
# -*- coding: utf-8 -*-

from Menu.MenuPrincipal import MenuPrincipal
from Helpers import Helpers
import os

menuPrincipal = MenuPrincipal()
helpers = Helpers()

loginExitoso = False
print("\nIniciar Sesión para continuar...")

while loginExitoso == False:
	
	usuario = input("\nNombre de Usuario: ")
	contraseña = input("Contraseña: ")

	if (usuario == "admin" and contraseña == "admin"):
		loginExitoso = True
	else:
		print("\nEl usuario o contraseña no coinciden.")
		input("Pulsa Enter para volver a intentar...")

helpers.Clear()

print ("\n!Bienvenido a los Almacenes¡")
menuPrincipal.Mostrar()
