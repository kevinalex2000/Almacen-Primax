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
        Button(frame_formulario_botones, text="Clientes Mas Frecuentes", command=self.mostrar_clientes_mas_frecuentes).grid(column=0, row=5, sticky='w')
        Button(frame_formulario_botones, text="Grafico de ventas mensuales", command=self.mostrar_ventas_mensuales).grid(column=0, row=7, sticky='w')

    def mostrar_ventas_mensuales(self):
        #Probamos las estadisticas
        datos = Excel.obtener_excel(Constants.get_url_excel_detalle_ventas(),"Hoja1")
        #Obtenemos la cantidad de las ventas realizadas en su totalidad
        totalventascantidad = datos.groupby(['Producto'])['Producto'].agg(self.obtener_cantidad)
        #Hacemos un foreach para obtener el array con la cantidad de ventas dentro del objeto 
        cantidadventas = []
        contador = 0
        for element in totalventascantidad:
            contador = contador + 1
            cantidadventas.append(contador)

        plt.plot(cantidadventas, totalventascantidad)
        plt.ylabel('Ventas Realizadas')
        plt.show()

    def mostrar_clientes_mas_frecuentes(self):
        #Probamos las estadisticas
        datos = Excel.obtener_excel(Constants.get_url_excel_ventas(),"Hoja1")
        #Obtenemos la cantidad de ventas que a tenido
        cantidadventascliente = datos.groupby(['Dni Cliente'])['Dni Cliente'].agg(self.obtener_cantidad).head(10)
        #Agrupamos los nombres del Producto
        nombrecliente = datos.groupby(['Nombre Cliente'])['Nombre Cliente'].agg(self.obtener_titulos).head(10)

        plt.bar(nombrecliente, cantidadventascliente)
        plt.ylabel('Clientes mas frecuentes')
        plt.show()

    def mostrar_producto_mas_vendidos(self):
        #Probamos las estadisticas
        datos = Excel.obtener_excel(Constants.get_url_excel_detalle_ventas(),"Hoja1")
        #Agrupamos y sumamos por productos
        productosagrupado = datos[datos['Cantidad'] > 0].groupby('Producto')['Cantidad'].sum()
        #Agrupamos los nombres del Producto
        nombreproductoagrupado = datos.groupby(['Producto'])['Producto'].agg(self.obtener_titulos)

        plt.bar(nombreproductoagrupado, productosagrupado)
        plt.ylabel('Productos mas Vendidos')
        plt.show()

    def obtener_titulos(self,values):
            if len(values) > 1:
                return values[0]
            else:
                return values

    def obtener_cantidad(self,values):
        return len(values)