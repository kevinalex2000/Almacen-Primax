from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame,messagebox
from tkinter.ttk import Style

from Shared.Helpers import Controls, Excel, Transform
from Shared.Constants import Constants

class ModuleClientes:
    
    def __init__(self,frame):
        self.frame = frame
        ## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
        Controls.colocar_titulo(frame, "Clientes")
        ##Creamos los Inputs para la creacion de los clientes
        ## Formulario
        self.crear_formulario()
        #Creacion de una tabla
        self.frame_tabla_clientes = Frame(frame, bg= Constants.get_bgcolor()) ## Creamos el frame para una tabla y colocamos el color de fondo
        self.frame_tabla_clientes.grid(columnspan=1, row=3, sticky='nsew', padx=10, pady=10) ## Indicamos posicion y espacio del frame para la tabla
        self.tabla_clientes = ttk.Treeview(self.frame_tabla_clientes)  ## Creamos Tabla instanciando TreeView
        self.tabla_clientes.grid(column=0, row=0, sticky='nsew') ## Indicamos posicion y espacio de la tabla dentro del frame
        ladoy = ttk.Scrollbar(self.frame_tabla_clientes, orient ='vertical', command = self.tabla_clientes.yview) ## Agregamos scrollbar vertical instanciando Scrollbar
        ladoy.grid(column = 1, row = 0, sticky='ns') ## Indicamos la posicion y espaciado del scrollbar

        self.tabla_clientes.configure(yscrollcommand = ladoy.set) ## Configuramos comportamiento del scrollbar con la tabla
        self.tabla_clientes['columns'] = ('Nombre', 'Numero de Celular', 'Direccion') ## Mencionamos las columnas tabla
        self.tabla_clientes.column('#0', minwidth=100, width=100, anchor='center') ## Colocamos Columna index
        self.tabla_clientes.column('Nombre', minwidth=100, width=180, anchor='center') ## Colocamos Columna Nombre
        self.tabla_clientes.column('Numero de Celular', minwidth=100,width=180, anchor='center') ## Colocamos Columna Numero de Celular
        self.tabla_clientes.column('Direccion', minwidth=100,width=180, anchor='center') ## Colocamos Columna Direccion

        self.tabla_clientes.heading('#0', text='Dni', anchor ='center') ## Colocamos Cabecera de columna Dni
        self.tabla_clientes.heading('Nombre', text='Nombre', anchor ='center') ## Colocamos Cabecera de columna Nombre
        self.tabla_clientes.heading('Numero de Celular', text='Numero de Celular', anchor ='center') ## Colocamos Cabecera de columna Numero de Celular
        self.tabla_clientes.heading('Direccion', text='Direccion', anchor ='center') ## Colocamos Cabecera de columna Direccion

        self.listar_datos_tabla()
    
    def crear_formulario(self):
        ## Formulario
        frame_formulario = Frame(self.frame, bg= Constants.get_bgcolor())
        frame_formulario.grid(column=0, row=1, sticky='nsew', padx=10) 
        #Dni
        label_dni=Label(frame_formulario, text="Dni:", bg= Constants.get_bgcolor())
        label_dni.grid(column=0, row=2, sticky='w')

        self.dni=StringVar()
        entry_dni = Entry(frame_formulario, width=30, textvariable=self.dni)
        entry_dni.grid(column=0, row=3, sticky='w')
        #Nombre
        label_nombre=Label(frame_formulario, text="Nombre:", bg= Constants.get_bgcolor())
        label_nombre.grid(column=1, row=2, sticky='w', padx=10)

        self.nombre=StringVar()
        entry_nombre = Entry(frame_formulario, width=30, textvariable=self.nombre)
        entry_nombre.grid(column=1, row=3, sticky='w', padx=10)
        #Numero Celular
        label_numero_celular=Label(frame_formulario, text="Numero de Celular:", bg= Constants.get_bgcolor())
        label_numero_celular.grid(column=2, row=2, sticky='w')

        self.numero_celular=StringVar()
        entry_numero_celular = Entry(frame_formulario, width=30, textvariable=self.numero_celular)
        entry_numero_celular.grid(column=2, row=3, sticky='w', padx=10)
        #Direccion
        label_direccion=Label(frame_formulario, text="Direccion:", bg= Constants.get_bgcolor())
        label_direccion.grid(column=3, row=2, sticky='w')

        self.direccion=StringVar()
        entry_direccion = Entry(frame_formulario, width=30, textvariable=self.direccion)
        entry_direccion.grid(column=3, row=3, sticky='w')

        frame_formulario_botones = Frame(self.frame, bg= Constants.get_bgcolor())
        frame_formulario_botones.grid(column=0, row=2, sticky='nsew', padx=10, pady=10) 
        Button(frame_formulario_botones, text="Agregar", command=self.btn_agregar_click).grid(column=0, row=3, sticky='w')
        Button(frame_formulario_botones, text="Modificar", command=self.btn_modificar_click).grid(column=1, row=3, sticky='w', padx=10)
        Button(frame_formulario_botones, text="Eliminar", command=self.btn_eliminar_click).grid(column=2, row=3, sticky='w')

    def btn_agregar_click(self):
        if self.validar_campos_vacios():
            if self.buscar_dni_existente(self.dni.get()):
                Controls.mandar_advertencia("El dni ya existe, por favor registre otro dni.")
            else:
                self.insertar_cliente(self.dni.get(),self.nombre.get(),int(self.numero_celular.get()),self.direccion.get())

    def btn_modificar_click(self):
        if self.validar_campos_vacios():
            if self.buscar_dni_existente(self.dni.get()):
                self.modificar_cliente(self.dni.get(),self.nombre.get(),int(self.numero_celular.get()))
            else:
                Controls.mandar_advertencia("El dni digitado no existe.")
                
    def btn_eliminar_click(self):
        if self.dni.get() != "":
            if self.buscar_dni_existente(self.dni.get()):
                self.eliminar_cliente(self.dni.get())
            else:
                Controls.mandar_advertencia("El dni digitado no existe.")
        else:
            Controls.mandar_advertencia("El dni no puede estar vacio.")

    def listar_datos_tabla(self):
        self.tabla_clientes.delete(*self.tabla_clientes.get_children())
        datos = Excel.obtener_excel("Data/Clientes.xlsx", "Hoja1")

        for fila in datos.values:
            arr_fila = []
            for celda in fila:
                arr_fila.append(celda)
            self.tabla_clientes.insert("", "end", text = arr_fila[0], values= (arr_fila[1], arr_fila[2], arr_fila[3]))

    def insertar_cliente(self, dni, nombre, numero_celular, direccion):
        datos = Excel.obtener_excel("Data/Clientes.xlsx", "Hoja1")

        values = Transform.dArray_to_array(datos.values)
        values.append([dni,nombre,numero_celular,direccion])

        Excel.guardar_excel("Data/Clientes.xlsx", "Hoja1", values, datos.columns)
        self.listar_datos_tabla()
        self.limpiar_campos()
        
    def modificar_cliente(self, dni, nombre, numero_celular):
        datos = Excel.obtener_excel("Data/Clientes.xlsx", "Hoja1")

        values = Transform.dArray_to_array(datos.values)

        for fila in values:
            if(fila[0] == int(dni)):
                fila[1] = nombre
                fila[2] = numero_celular

        Excel.guardar_excel("Data/Clientes.xlsx", "Hoja1", values, datos.columns)
        self.listar_datos_tabla()
        self.limpiar_campos()

    def eliminar_cliente(self, dni):
        datos = Excel.obtener_excel("Data/Clientes.xlsx", "Hoja1")

        values = []

        for fila in Transform.dArray_to_array(datos.values):
            if(fila[0] != int(dni)):
                values.append(fila)

        Excel.guardar_excel("Data/Clientes.xlsx", "Hoja1", values, datos.columns)
        self.listar_datos_tabla()
        self.limpiar_campos()

    def buscar_dni_existente(self, dni):
        datos = Excel.obtener_excel("Data/Clientes.xlsx", "Hoja1")
        for fila in datos.values:
            if(fila[0] == int(dni)):
                return True
        return False

    def validar_campos_vacios(self):
        resultado = False
        if self.dni.get() == "":
            Controls.mandar_advertencia("El dni no puede estar vacio")
        elif self.nombre.get() == "":
            Controls.mandar_advertencia("El nombre no puede estar vacio")
        elif self.numero_celular.get() == "":
            Controls.mandar_advertencia("El numero de celular no puede estar vacio")
        elif self.direccion.get() == "":
            Controls.mandar_advertencia("La direccion no puede estar vacia")
        else:
            resultado = True
        return resultado

    def limpiar_campos(self):
        self.dni.set("")
        self.nombre.set("")
        self.numero_celular.set("")
        self.direccion.set("")