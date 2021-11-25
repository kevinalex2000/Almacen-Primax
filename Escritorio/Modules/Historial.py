from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame,messagebox

from Shared.Helpers import Controls, Excel, Transform
from Shared.Constants import Constants

from datetime import datetime


class ModuleHistorial:
    
    def __init__(self,frame):
        self.frame = frame
        self.HojaExcel = "Hoja1"
        Controls.colocar_titulo(frame, "Historial de Ingreso y salida")
        self.crear_tabla()
        self.llenar_datos_tabla()
        
    def crear_tabla(self):
        #Creacion de la tabla
        self.frame_tabla_historial = Frame(self.frame, bg= Constants.get_bgcolor()) ## Creamos el frame para una tabla y colocamos el color de fondo
        self.frame_tabla_historial.grid(columnspan=1, row=4, sticky='nsew', padx=10, pady=10) ## Indicamos posicion y espacio del frame para la tabla
        self.tabla_historial = ttk.Treeview(self.frame_tabla_historial)  ## Creamos Tabla instanciando TreeView
        self.tabla_historial.grid(column=0, row=0, sticky='nsew') ## Indicamos posicion y espacio de la tabla dentro del frame
        ladoy = ttk.Scrollbar(self.frame_tabla_historial, orient ='vertical', command = self.tabla_historial.yview) ## Agregamos scrollbar vertical instanciando Scrollbar
        ladoy.grid(column = 1, row = 0, sticky='ns') ## Indicamos la posicion y espaciado del scrollbar

        self.tabla_historial.configure(yscrollcommand = ladoy.set) ## Configuramos comportamiento del scrollbar con la tabla
        self.tabla_historial['columns'] = ('Fecha', 'Identificador Tercero', 'Tercero', 'Precio Total') ## Mencionamos las columnas tabla
        self.tabla_historial.column('#0', minwidth=50, width=80, anchor='center') ## Colocamos Columna index
        self.tabla_historial.column('Fecha', minwidth=100, width=200 , anchor='center') ## Colocamos Columna Nombre
        self.tabla_historial.column('Identificador Tercero', minwidth=100, width=200 , anchor='center') ## Colocamos Columna Precio
        self.tabla_historial.column('Tercero', minwidth=100, width=200 , anchor='center') ## Colocamos Columna Precio
        self.tabla_historial.column('Precio Total', minwidth=100, width=200, anchor='center') ## Colocamos Columna Cantidad

        self.tabla_historial.heading('#0', text='', anchor ='center') ## Colocamos Cabecera de columna index
        self.tabla_historial.heading('Fecha', text='Fecha', anchor ='center') ## Colocamos Cabecera de columna Nombre
        self.tabla_historial.heading('Identificador Tercero', text='ID Tercero', anchor ='center') ## Colocamos Cabecera de columna Precio
        self.tabla_historial.heading('Tercero', text='Tercero', anchor ='center') ## Colocamos Cabecera de columna Precio
        self.tabla_historial.heading('Precio Total', text='Precio Total', anchor ='center') ## Colocamos Cabecera de columna Cantidad

    def llenar_datos_tabla(self):
        self.tabla_historial.delete(*self.tabla_historial.get_children())

        datos_ventas = Excel.obtener_excel(Constants.get_url_excel_ventas(), self.HojaExcel)
        datos_compras = Excel.obtener_excel(Constants.get_url_excel_compras(), self.HojaExcel)

        datos_ventas = Transform.dArray_to_array(datos_ventas.values)
        datos_compras = Transform.dArray_to_array(datos_compras.values)

        datos_general = []

        for fila in datos_ventas:
            arr_fila = ["salida", fila[1], fila[2],fila[3],fila[4]]
            datos_general.append(arr_fila)
        for fila in datos_compras:
            arr_fila = ["ingreso", fila[1], fila[2],fila[3],fila[4]]
            datos_general.append(arr_fila)

        datos_general.sort()
        
        for dato in datos_general:
            self.tabla_historial.insert("", "end", text = dato[0], values= (dato[1], dato[2], dato[3], dato[4]))