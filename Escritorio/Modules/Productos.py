from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame
from tkinter.ttk import Style

from Shared.Helpers import Controls, Excel
from Shared.Constants import Constants

class ModuleProductos:

    def __init__(self,frame):
        self.frame = frame

        ## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
        Controls.colocarTitulo(frame, "Productos")

        self.crear_formulario()

        #Creacion de una tabla
        self.frame_tabla_productos = Frame(frame, bg= Constants.getBgColor()) ## Creamos el frame para una tabla y colocamos el color de fondo
        self.frame_tabla_productos.grid(columnspan=1, row=3, sticky='nsew', padx=10, pady=10) ## Indicamos posicion y espacio del frame para la tabla
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

        self.listar_datos_tabla()

    def crear_formulario(self):
        ## Formulario
        frame_formulario = Frame(self.frame, bg= Constants.getBgColor())
        frame_formulario.grid(column=0, row=1, sticky='nsew', padx=10) 

        label_codigo=Label(frame_formulario, text="Codigo:", bg= Constants.getBgColor())
        label_codigo.grid(column=0, row=2, sticky='w')

        self.codigo=StringVar()
        entry_codigo = Entry(frame_formulario, width=30, textvariable=self.codigo)
        entry_codigo.grid(column=0, row=3, sticky='w')
        
        label_nombre=Label(frame_formulario, text="Nombre:", bg= Constants.getBgColor())
        label_nombre.grid(column=1, row=2, sticky='w', padx=10)

        self.nombre=StringVar()
        entry_nombre = Entry(frame_formulario, width=30, textvariable=self.nombre)
        entry_nombre.grid(column=1, row=3, sticky='w', padx=10)
        
        label_precio=Label(frame_formulario, text="Precio:", bg= Constants.getBgColor())
        label_precio.grid(column=2, row=2, sticky='w')

        self.precio=StringVar()
        entry_precio = Entry(frame_formulario, width=30, textvariable=self.precio)
        entry_precio.grid(column=2, row=3, sticky='w')

        frame_formulario_botones = Frame(self.frame, bg= Constants.getBgColor())
        frame_formulario_botones.grid(column=0, row=2, sticky='nsew', padx=10, pady=10) 
        Button(frame_formulario_botones, text="Agregar").grid(column=0, row=3, sticky='w')
        Button(frame_formulario_botones, text="Modificar").grid(column=1, row=3, sticky='w', padx=10)
        Button(frame_formulario_botones, text="Eliminar").grid(column=2, row=3, sticky='w')

    def listar_datos_tabla(self):
        self.tabla_productos.delete(*self.tabla_productos.get_children())

        datos = Excel.ObtenerExcel("Data/Productos.xlsx", "Hoja1")

        for fila in datos.values:
            arr_fila = []
            for celda in fila:
                arr_fila.append(celda)
            self.tabla_productos.insert("", "end", text = arr_fila[0], values= (arr_fila[1], arr_fila[2], arr_fila[3]))

    def insertar_producto(self, codigo, nombre, precio, cantidad):
        
        datos = Excel.ObtenerExcel("Data/Productos.xlsx", "Hoja1")
        nueva_data = datos.values.append([codigo,nombre,precio,cantidad])