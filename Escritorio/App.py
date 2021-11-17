from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame

from Modules.Productos import ModuleProductos
from Modules.Compras import ModuleCompras
from Modules.Clientes import ModuleClientes
from Modules.Ventas import ModuleVentas

class Ventana(Frame):

	## Metodo de Inicializacion
	def __init__(self, master, *args):

		## Construimos el atributo master como contenedor principal
		super().__init__( master,*args)

		## Configuramos distribucion de Master
		self.master.columnconfigure(1, weight=1)
		self.master.rowconfigure(1, weight=1)
		
		## Creamos frame principal
		self.frame_principal = Frame(self.master) ## Instanciamos nuevo Frame
		self.frame_principal.grid(column=1, row=1, sticky='nsew') ## Creamos la Grilla
		## Configuramos el indice y espacio que ocupara
		self.frame_principal.columnconfigure(0, weight=1)
		self.frame_principal.rowconfigure(0, weight=1)

		## Creamos Las paginas que ocuparan toda la ventana
		self.crear_paginas()

	## Cre las paginas con el menu superior
	def crear_paginas(self):
		## Creamos el estilo para la pagina
		estilo_paginas = ttk.Style() ## Instanciamos el estilo nuevo
		estilo_paginas.configure("TNotebook", padding=0, borderwidth=0) ## Configuramos el nombre del estilo
		estilo_paginas.theme_use('default') ## Colocamos tema por defecto
		estilo_paginas.configure("TNotebook",  background="#EEEEEE", borderwidth=0) ## Colocamos el color de fondo de la barra del menu
		estilo_paginas.configure("TNotebook.Tab", background="#F9F9F9", borderwidth=0) ## Colocamos el color de fondo del Tab
		estilo_paginas.map(
					"TNotebook.Tab", 
					 background=[("selected", '#06A42E')], 
					 foreground=[("selected", 'white')]); ## Colocamos el color de fondo del Tab y el color del texto cuando estan seleccionados

		## Creamos las paginas
		self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook') ## Instanciamos las paginas y colocamos el estilo
		self.paginas.grid(column=0,row=0, sticky='nsew') ## Indicamos el espaciado y ubicacion

		## Empezamos a crear los frames con ubicacion en paginas
		self.frame_inicio = Frame(self.paginas, bg='white')
		self.frame_productos = Frame(self.paginas, bg='white')
		self.frame_compras = Frame(self.paginas, bg='white')
		self.frame_ventas = Frame(self.paginas, bg='white')
		self.frame_clientes = Frame(self.paginas, bg='white')
		self.frame_estadisticas = Frame(self.paginas, bg='white')
		self.frame_historial = Frame(self.paginas, bg='white')

		## Agregamos los Tabs en el Menu superior con el texto y el frame que mostrara al estar activo
		self.paginas.add(self.frame_inicio, text='Inicio')
		self.paginas.add(self.frame_productos, text='Productos')
		self.paginas.add(self.frame_compras, text='Compras')
		self.paginas.add(self.frame_ventas, text='Ventas')
		self.paginas.add(self.frame_clientes, text='Clientes')
		self.paginas.add(self.frame_estadisticas, text='Estadisticas')
		self.paginas.add(self.frame_historial, text='Historial')
		
		## Agregamos controles a los frames
		ModuleProductos(self.frame_productos)
		ModuleCompras(self.frame_compras)
		ModuleClientes(self.frame_clientes)
		ModuleVentas(self.frame_ventas)