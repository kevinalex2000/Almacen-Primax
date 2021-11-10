
#!/usr/bin/python
# -*- coding: utf-8 -*-

from Menu import Menu

menu = Menu()

loginExitoso = False
print("Iniciar Sesión para continuar...")

while loginExitoso == False:
	
	usuario = input("\nNombre de Usuario: ")
	contraseña = input("Contraseña: ")

	if (usuario == "admin" and contraseña == "admin"):
		loginExitoso = True
	else:
		print("\nEl usuario o contraseña no coinciden.")
		input("Pulsa Enter para volver a intentar...")
		
menu.Principal()

input("Selecciona una opcion para continuar: ")