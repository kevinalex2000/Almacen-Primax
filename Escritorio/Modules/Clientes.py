from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame

from Shared.Helpers import Controls
import os
import pandas as pd

class ModuleClientes:
    
    def __init__(self,frame):
        self.frame = frame
        ## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
        Controls.colocarTitulo(frame, "Clientes")
        ##Creamos los Inputs para la creacion de los clientes
        ## Formulario
        frame_formulario = Frame(self.frame, bg= 'white')
        frame_formulario.grid(column=0, row=1, sticky='nsew', padx=10, pady=10) 
        #Dni
        label_dni=Label(frame_formulario, text="Dni:", bg= 'white')
        label_dni.grid(column=0, row=2, sticky='w')

        self.dni=StringVar()
        entry_dni = Entry(frame_formulario, width=30, textvariable=self.dni)
        entry_dni.grid(column=0, row=3, sticky='w')
        #Nombre
        label_nombre=Label(frame_formulario, text="Nombre:", bg= 'white')
        label_nombre.grid(column=1, row=2, sticky='w', padx=10)

        self.nombre=StringVar()
        entry_nombre = Entry(frame_formulario, width=30, textvariable=self.nombre)
        entry_nombre.grid(column=1, row=3, sticky='w', padx=10)
        #Numero Celular
        label_numero_celular=Label(frame_formulario, text="Numero de Celular:", bg= 'white')
        label_numero_celular.grid(column=2, row=2, sticky='w')

        self.numero_celular=StringVar()
        entry_numero_celular = Entry(frame_formulario, width=30, textvariable=self.numero_celular)
        entry_numero_celular.grid(column=2, row=3, sticky='w', padx=10)
        #Direccion
        label_direccion=Label(frame_formulario, text="Direccion:", bg= 'white')
        label_direccion.grid(column=3, row=2, sticky='w')

        self.direccion=StringVar()
        entry_direccion = Entry(frame_formulario, width=30, textvariable=self.direccion)
        entry_direccion.grid(column=3, row=3, sticky='w')

        frame_formulario_botones = Frame(self.frame, bg= 'white')
        frame_formulario_botones.grid(column=0, row=2, sticky='nsew', padx=10) 
        Button(frame_formulario_botones, text="Agregar", command=self.AgregarCliente).grid(column=0, row=3, sticky='w')
        Button(frame_formulario_botones, text="Modificar").grid(column=1, row=3, sticky='w', padx=10)
        Button(frame_formulario_botones, text="Eliminar").grid(column=2, row=3, sticky='w')
      
        #Validamos si existe el Excel 
        
        if(os.path.exists("Clientes.xlsx")):
             #Llamamos al Excel y cargamos la data
             self.dataClientes = Controls.ObtenerExcelClientes()
             self.MostrarInformacionCliente()
        else:
            #Llamamos a la funcion de crear el Excel 
            Controls.CrearExcelCliente()


    def AgregarCliente(self):
        #Traemos la data del Excel para concatenar
        #DNI
        listadodni = self.dataClientes['DNI'].values
        listadodni.append(self.dni)
        #Creamos el Array con la data ya creada
        data = {
            'DNI': [],
            'Nombre': [],
            'Numero de Celular': [],
            'Direccion': []}
        #Recorremos la data actual 
        self.dataClientes
        print(self.dataClientes)

    def MostrarInformacionCliente(self):
        #Mostramos la primera data 
        self.frame_tabla_clientes = Frame(self.frame, bg= 'gray90') 
        self.frame_tabla_clientes.grid(columnspan=2, row=5, sticky='nsew') 
        self.tabla_clientes = ttk.Treeview(self.frame_tabla_clientes)
        self.tabla_clientes.grid(column=0, row=0, sticky='nsew')
        ladoy = ttk.Scrollbar(self.frame_tabla_clientes, orient ='vertical', command = self.tabla_clientes.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_clientes['columns'] = self.dataClientes.columns.values.tolist()
        #Columna por defecto se oculta
        self.tabla_clientes.column('#0', width = 0, stretch = False)

        for i in self.dataClientes.columns.values.tolist():
           self.tabla_clientes.column(i, width = 200, anchor='center')
           self.tabla_clientes.heading(i, text = i, anchor='center')
        for index, row in self.dataClientes.iterrows():
           self.tabla_clientes.insert(parent = '',index = index,text = index, values = list(row))
