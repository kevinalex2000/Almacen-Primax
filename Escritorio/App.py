from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame

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
		self.frame_uno = Frame(self.paginas, bg='white')
		self.frame_dos = Frame(self.paginas, bg='white')
		self.frame_tres = Frame(self.paginas, bg='white')
		self.frame_cuatro = Frame(self.paginas, bg='white')
		self.frame_cinco = Frame(self.paginas, bg='white')
		self.frame_seis = Frame(self.paginas, bg='white')
		self.frame_siete = Frame(self.paginas, bg='white')

		## Agregamos los Tabs en el Menu superior con el texto y el frame que mostrara al estar activo
		self.paginas.add(self.frame_uno, text='Inicio')
		self.paginas.add(self.frame_dos, text='Productos')
		self.paginas.add(self.frame_tres, text='Compras')
		self.paginas.add(self.frame_cuatro, text='Ventas')
		self.paginas.add(self.frame_cinco, text='Clientes')
		self.paginas.add(self.frame_seis, text='Estadisticas')
		self.paginas.add(self.frame_siete, text='Historial')
		
		## Agregamos controles a los frames
		self.agregar_controles_frame_productos()
		self.agregar_controles_frame_compras()

	## Agrega los controles al frame_dos
	def agregar_controles_frame_productos(self):
		## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
		Label(self.frame_dos, text= 'Administrar Productos', bg='white',  font= ('Arial', 16, 'bold'), justify=LEFT).grid(column =0, row=0, sticky='w')
		
		#Creacion de una tabla
		self.frame_tabla_productos = Frame(self.frame_dos, bg= 'gray90') ## Creamos el frame para una tabla y colocamos el color de fondo
		self.frame_tabla_productos.grid(columnspan=1, row=2, sticky='nsew') ## Indicamos posicion y espacio del frame para la tabla
		self.tabla_productos = ttk.Treeview(self.frame_tabla_productos)  ## Creamos Tabla instanciando TreeView
		self.tabla_productos.grid(column=0, row=0, sticky='nsew') ## Indicamos posicion y espacio de la tabla dentro del frame
		ladoy = ttk.Scrollbar(self.frame_tabla_productos, orient ='vertical', command = self.tabla_productos.yview) ## Agregamos scrollbar vertical instanciando Scrollbar
		ladoy.grid(column = 1, row = 0, sticky='ns') ## Indicamos la posicion y espaciado del scrollbar

		self.tabla_productos.configure(yscrollcommand = ladoy.set) ## Configuramos comportamiento del scrollbar con la tabla
		self.tabla_productos['columns'] = ('Nombre', 'Precio', 'Cantidad') ## Mencionamos las columnas tabla
		self.tabla_productos.column('#0', minwidth=100, width=120, anchor='center') ## Colocamos Columna index
		self.tabla_productos.column('Nombre', minwidth=100, width=130 , anchor='center') ## Colocamos Columna Nombre
		self.tabla_productos.column('Precio', minwidth=100, width=120 , anchor='center') ## Colocamos Columna Precio
		self.tabla_productos.column('Cantidad', minwidth=100, width=105, anchor='center') ## Colocamos Columna Cantidad

		self.tabla_productos.heading('#0', text='Codigo', anchor ='center') ## Colocamos Cabecera de columna index
		self.tabla_productos.heading('Nombre', text='Nombre', anchor ='center') ## Colocamos Cabecera de columna Nombre
		self.tabla_productos.heading('Precio', text='Precio', anchor ='center') ## Colocamos Cabecera de columna Precio
		self.tabla_productos.heading('Cantidad', text='Cantidad', anchor ='center') ## Colocamos Cabecera de columna Cantidad
		
	## Agrega los controles al frame_tres
	def agregar_controles_frame_compras(self):
		## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
		Label(self.frame_tres, text = 'Compras', bg ='white', font=('Arial',16,'bold')).grid(column =0, row=0, sticky='w')
