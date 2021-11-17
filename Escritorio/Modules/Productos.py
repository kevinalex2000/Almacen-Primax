from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame

from Shared.Helpers import Controls

class ModuleProductos:

    def __init__(self,frame):
        ## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
        Controls.colocarTitulo(frame, "Productos")

        #Creacion de una tabla
        self.frame_tabla_productos = Frame(frame, bg= 'gray90') ## Creamos el frame para una tabla y colocamos el color de fondo
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