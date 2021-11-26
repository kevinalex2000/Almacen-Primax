from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame,messagebox
import matplotlib.pyplot as plt

from Shared.Helpers import Controls, Excel, Transform
from Shared.Constants import Constants

from datetime import datetime

class ModuleEstadisticas:

    def __init__(self,frame):

        self.frame = frame
        ## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
        Controls.colocar_titulo(frame, "Estadisticas")
        ##Creamos los Botones para la creacion de los clientes
        ## Formulario
        self.crear_formulario()
        

    def crear_formulario(self):
        ## Formulario
        frame_formulario_botones = Frame(self.frame, bg= Constants.get_bgcolor())
        frame_formulario_botones.grid(column=0, row=2, sticky='nsew', padx=10, pady=10) 
        Button(frame_formulario_botones, text="Productos Mas Vendidos", command=self.mostrar_producto_mas_vendidos).grid(column=0, row=3, sticky='w')
    
    def mostrar_producto_mas_vendidos(self):
        #Probamos las estadisticas
        datos = Excel.obtener_excel(Constants.get_url_excel_detalle_ventas(),"Hoja1")
        names = []
        values = []
        index = 0
        #Obtenemos los nombres de los productos
        for fila in datos.values:
            names.append(fila[1])
            index += 1
        #Obtenemos la cantidad de los productos
        for fila in datos.values:
            values.append(fila[2])
            index += 1

        plt.bar(names, values)
        plt.ylabel('Productos mas Vendidos')
        plt.show()