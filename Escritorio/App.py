# Menu Lateral desplegable y base de datos MySQL
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren
# https://www.youtube.com/watch?v=01W_qYxnHbI&t=525s

from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame
import time

class Ventana(Frame):
	def __init__(self, master, *args):
		super().__init__( master,*args)

		self.menu = True
		self.color = True

		self.codigo = StringVar()
		self.nombre = StringVar()
		self.modelo = StringVar()
		self.precio = StringVar()
		self.cantidad = StringVar()
		self.buscar = StringVar()
		self.buscar_actualiza =  StringVar()
		self.id = StringVar()

		## Colores
		self.color_frame_inicial = "#11BF5E"
		self.color_frame_top = "white"
		self.color_frame_menu = "#36A05F"
		self.color_active_frame_menu = "#11BF5E"
		
		self.frame_principal = Frame(self.master)
		self.frame_principal.grid(column=1, row=1, sticky='nsew')
		self.master.columnconfigure(1, weight=1)
		self.master.rowconfigure(1, weight=1)
		self.frame_principal.columnconfigure(0, weight=1)
		self.frame_principal.rowconfigure(0, weight=1)

		self.widgets()
	
	def rellenar_frame_inicio(self):
		Label(self.frame_inicio, bg=self.color_frame_inicial, text= 'Almacenes GKOP', fg= 'white', font= ('Arial', 12, 'bold')).grid(column=1, row=2, padx=20, pady=10)

	def pantalla_inicial(self):
		self.paginas.select([self.frame_uno])

	def pantalla_datos(self):
		self.paginas.select([self.frame_dos])
		self.frame_dos.columnconfigure(0, weight=1)
		self.frame_dos.columnconfigure(1, weight=1)
		self.frame_dos.rowconfigure(2, weight=1)
		self.frame_tabla_uno.columnconfigure(0, weight=1)
		self.frame_tabla_uno.rowconfigure(0, weight=1)

	def pantalla_escribir(self):
		self.paginas.select([self.frame_tres])
		self.frame_tres.columnconfigure(0, weight=1)
		self.frame_tres.columnconfigure(1, weight=1)

	def pantalla_actualizar(self):
		self.paginas.select([self.frame_cuatro])	
		self.frame_cuatro.columnconfigure(0, weight=1)
		self.frame_cuatro.columnconfigure(1, weight=1)

	def pantalla_buscar(self):
		self.paginas.select([self.frame_cinco])
		self.frame_cinco.columnconfigure(0, weight=1)
		self.frame_cinco.columnconfigure(1, weight=1)
		self.frame_cinco.columnconfigure(2, weight=1)
		self.frame_cinco.rowconfigure(2, weight=1)
		self.frame_tabla_dos.columnconfigure(0, weight=1)
		self.frame_tabla_dos.rowconfigure(0, weight=1)

	def pantalla_ajustes(self):
		self.paginas.select([self.frame_seis])

	def widgets(self):

		#############################  CREAR  PAGINAS  ##############################
		estilo_paginas = ttk.Style()
		estilo_paginas.configure("TNotebook", padding=0, borderwidth=0)
		estilo_paginas.theme_use('default')
		estilo_paginas.configure("TNotebook",  background="#EEEEEE", borderwidth=0)
		estilo_paginas.configure("TNotebook.Tab", background="#F9F9F9", borderwidth=0)
		estilo_paginas.map("TNotebook", background=[("selected", '#06A42E')])
		estilo_paginas.map("TNotebook.Tab", background=[("selected", '#06A42E')], foreground=[("selected", 'white')]);

		#CREACCION DE LAS PAGINAS 
		self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook') #, style = 'TNotebook'
		self.paginas.grid(column=0,row=0, sticky='nsew')
		self.frame_uno = Frame(self.paginas, bg='white')
		self.frame_dos = Frame(self.paginas, bg='white')
		self.frame_tres = Frame(self.paginas, bg='white')
		self.frame_cuatro = Frame(self.paginas, bg='white')
		self.frame_cinco = Frame(self.paginas, bg='white')
		self.frame_seis = Frame(self.paginas, bg='white')
		self.frame_siete = Frame(self.paginas, bg='white')
		self.paginas.add(self.frame_uno, text='Inicio')
		self.paginas.add(self.frame_dos, text='Productos')
		self.paginas.add(self.frame_tres, text='Compras')
		self.paginas.add(self.frame_cuatro, text='Ventas')
		self.paginas.add(self.frame_cinco, text='Clientes')
		self.paginas.add(self.frame_seis, text='Estadisticas')
		self.paginas.add(self.frame_siete, text='Historial')


		##############################         PAGINAS       #############################################


		######################## VENTANA PRINCIPAL #################
		
		######################## MOSTRAR TODOS LOS PRODUCTOS DE LA BASE DE DATOS MYSQL #################
		Label(self.frame_dos, text= 'Administrar Productos', bg='white',  font= ('Arial', 16, 'bold'), justify=LEFT).grid(column =0, row=0, sticky='w')
		
		#TABLA UNO 
		self.frame_tabla_uno = Frame(self.frame_dos, bg= 'gray90')
		self.frame_tabla_uno.grid(columnspan=1, row=2, sticky='nsew')		
		self.tabla_uno = ttk.Treeview(self.frame_tabla_uno) 
		self.tabla_uno.grid(column=0, row=0, sticky='nsew')
		ladox = ttk.Scrollbar(self.frame_tabla_uno, orient = 'horizontal', command= self.tabla_uno.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = ttk.Scrollbar(self.frame_tabla_uno, orient ='vertical', command = self.tabla_uno.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.tabla_uno.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
		self.tabla_uno['columns'] = ('Nombre', 'Precio', 'Cantidad')
		self.tabla_uno.column('#0', minwidth=100, width=120, anchor='center')
		self.tabla_uno.column('Nombre', minwidth=100, width=130 , anchor='center')
		self.tabla_uno.column('Precio', minwidth=100, width=120 , anchor='center')
		self.tabla_uno.column('Cantidad', minwidth=100, width=105, anchor='center')

		self.tabla_uno.heading('#0', text='Codigo', anchor ='center')
		self.tabla_uno.heading('Nombre', text='Nombre', anchor ='center')
		self.tabla_uno.heading('Precio', text='Precio', anchor ='center')
		self.tabla_uno.heading('Cantidad', text='Cantidad', anchor ='center')
		self.tabla_uno.bind("<<TreeviewSelect>>", self.obtener_fila) 

		######################## COMPRAS #################
		Label(self.frame_tres, text = 'Compras', bg ='white', font=('Arial',16,'bold')).grid(column =0, row=0, sticky='w')

		########################   ACTUALIZAR LOS PRODUCTOS REGISTRADOS     #################
		######################## BUSCAR y ELIMINAR DATOS #################

	def datos_totales(self):
		datos = self.base_datos.mostrar_productos()
		self.tabla_uno.delete(*self.tabla_uno.get_children())
		i = -1
		for dato in datos:
			i= i+1
			self.tabla_uno.insert('',i, text = datos[i][1:2], values=datos[i][2:6])


	def agregar_datos(self):
		codigo = self.codigo.get()
		nombre = self.nombre.get()
		modelo = self.modelo.get()
		precio = self.precio.get()
		cantidad = self.cantidad.get()
		datos = (nombre, modelo, precio, cantidad)
		if codigo and nombre and modelo and precio and cantidad !='':
			self.tabla_uno.insert('',0, text = codigo, values=datos)
			self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad)
			self.aviso_guardado['text'] = 'Datos Guardados'
			self.limpiar_datos()
			self.aviso_guardado.update()						
			time.sleep(1) 
			self.aviso_guardado['text'] = ''						
		else:
			self.aviso_guardado['text'] = 'Ingrese todos los datos'
			self.aviso_guardado.update()
			time.sleep(1) 
			self.aviso_guardado['text'] = ''

	def actualizar_datos(self):
		dato = self.buscar_actualiza.get()
		dato = str("'" + dato + "'")
		nombre_buscado = self.base_datos.busca_producto(dato)

		if nombre_buscado == []:
			self.aviso_actualizado['text'] = 'No existe'			
			self.indica_busqueda.update()						
			time.sleep(1) 
			self.limpiar_datos()
			self.aviso_actualizado['text'] = ''
		else:
			i = -1
			for dato in nombre_buscado:
				i= i+1
				self.id.set(nombre_buscado[i][0])
				self.codigo.set(nombre_buscado[i][1])
				self.nombre.set(nombre_buscado[i][2])
				self.modelo.set(nombre_buscado[i][3])
				self.precio.set(nombre_buscado[i][4])
				self.cantidad.set(nombre_buscado[i][5])


	def actualizar_tabla(self):	
		Id = self.id.get() 	
		codigo = self.codigo.get()
		nombre = self.nombre.get()
		modelo = self.modelo.get()
		precio = self.precio.get()
		cantidad = self.cantidad.get()
		self.base_datos.actualiza_productos(Id, codigo, nombre, modelo, precio, cantidad)		
		self.aviso_actualizado['text'] = 'Datos Actualizados'			
		self.indica_busqueda.update()						
		time.sleep(1) 
		self.aviso_actualizado['text'] = ''
		self.limpiar_datos()
		self.buscar_actualiza.set('')
				
	def limpiar_datos(self):
		self.codigo.set('')
		self.nombre.set('')
		self.modelo.set('')
		self.precio.set('')
		self.cantidad.set('')

	def buscar_nombre(self):
		nombre_producto = self.buscar.get()
		nombre_producto = str("'" + nombre_producto + "'")
		nombre_buscado = self.base_datos.busca_producto(nombre_producto)

		if nombre_buscado == []:
			self.indica_busqueda['text'] = 'No existe'
			self.indica_busqueda.update()						
			time.sleep(1) 
			self.indica_busqueda['text'] =''

		i = -1
		for dato in nombre_buscado:
			i= i+1
			self.tabla_dos.insert('',i, text = nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])


	def eliminar_fila(self):
		fila = self.tabla_dos.selection()
		if len(fila) !=0:
			self.tabla_dos.delete(fila)
			nombre = ("'"+ str(self.nombre_borrar) + "'")
			self.base_datos.elimina_productos(nombre)
			self.indica_busqueda['text'] = 'Eliminado'
			self.indica_busqueda.update()						
			self.tabla_dos.delete(*self.tabla_dos.get_children())
			time.sleep(1)
			self.indica_busqueda['text'] =''
			self.limpiar_datos()
		else:
			self.indica_busqueda['text'] = 'No se Elimino'
			self.indica_busqueda.update()
			self.tabla_dos.delete(*self.tabla_dos.get_children())						
			time.sleep(1) 
			self.indica_busqueda['text'] =''
			self.buscar.set('')
			self.limpiar_datos()

	def obtener_fila(self, event):
		current_item = self.tabla_dos.focus()
		if not current_item:
			return
		data = self.tabla_dos.item(current_item)
		self.nombre_borrar = data['values'][0]




