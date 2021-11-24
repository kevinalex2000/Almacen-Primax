from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame,messagebox
from tkinter.ttk import Style

from Shared.Helpers import Controls, Excel, Transform
from Shared.Constants import Constants

class ModuleProductos:

    def __init__(self,frame):
        self.frame = frame
        self.HojaExcel = "Hoja1"

        ## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
        Controls.colocar_titulo(self.frame, "Productos")

        self.crear_formulario()

        self.crear_tabla()
        self.listar_datos_tabla()

    def crear_tabla(self):
        #Creacion de la tabla
        self.frame_tabla_productos = Frame(self.frame, bg= Constants.get_bgcolor()) ## Creamos el frame para una tabla y colocamos el color de fondo
        self.frame_tabla_productos.grid(columnspan=1, row=3, sticky='nsew', padx=10, pady=10) ## Indicamos posicion y espacio del frame para la tabla
        self.tabla_productos = ttk.Treeview(self.frame_tabla_productos)  ## Creamos Tabla instanciando TreeView
        self.tabla_productos.grid(column=0, row=0, sticky='nsew') ## Indicamos posicion y espacio de la tabla dentro del frame
        ladoy = ttk.Scrollbar(self.frame_tabla_productos, orient ='vertical', command = self.tabla_productos.yview) ## Agregamos scrollbar vertical instanciando Scrollbar
        ladoy.grid(column = 1, row = 0, sticky='ns') ## Indicamos la posicion y espaciado del scrollbar

        self.tabla_productos.configure(yscrollcommand = ladoy.set) ## Configuramos comportamiento del scrollbar con la tabla
        self.tabla_productos['columns'] = ('Nombre', 'Precio', 'Cantidad', 'Cantidad Inicial') ## Mencionamos las columnas tabla
        self.tabla_productos.column('#0', minwidth=100, width=120, anchor='center') ## Colocamos Columna index
        self.tabla_productos.column('Nombre', minwidth=100, width=130 , anchor='center') ## Colocamos Columna Nombre
        self.tabla_productos.column('Precio', minwidth=100, width=120 , anchor='center') ## Colocamos Columna Precio
        self.tabla_productos.column('Cantidad', minwidth=100, width=105, anchor='center') ## Colocamos Columna Cantidad
        self.tabla_productos.column('Cantidad Inicial', minwidth=100, width=105, anchor='center') ## Colocamos Columna Cantidad Inicial

        self.tabla_productos.heading('#0', text='Codigo', anchor ='center') ## Colocamos Cabecera de columna index
        self.tabla_productos.heading('Nombre', text='Nombre', anchor ='center') ## Colocamos Cabecera de columna Nombre
        self.tabla_productos.heading('Precio', text='Precio', anchor ='center') ## Colocamos Cabecera de columna Precio
        self.tabla_productos.heading('Cantidad', text='Cantidad', anchor ='center') ## Colocamos Cabecera de columna Cantidad
        self.tabla_productos.heading('Cantidad Inicial', text='Cantidad Inicial', anchor ='center') ## Colocamos Cabecera de columna Cantidad Inicial

    def crear_formulario(self):
        ## Formulario
        frame_formulario = Frame(self.frame, bg= Constants.get_bgcolor())
        frame_formulario.grid(column=0, row=1, sticky='nsew', padx=10) 

        label_codigo=Label(frame_formulario, text="Codigo:", bg= Constants.get_bgcolor())
        label_codigo.grid(column=0, row=2, sticky='w')
        self.codigo=StringVar()
        entry_codigo = Entry(frame_formulario, width=30, textvariable=self.codigo)
        entry_codigo.grid(column=0, row=3, sticky='w')
        
        label_nombre=Label(frame_formulario, text="Nombre:", bg= Constants.get_bgcolor())
        label_nombre.grid(column=1, row=2, sticky='w', padx=10)
        self.nombre=StringVar()
        entry_nombre = Entry(frame_formulario, width=30, textvariable=self.nombre)
        entry_nombre.grid(column=1, row=3, sticky='w', padx=10)
        
        label_precio=Label(frame_formulario, text="Precio:", bg= Constants.get_bgcolor())
        label_precio.grid(column=2, row=2, sticky='w')
        self.precio=StringVar()
        entry_precio = Entry(frame_formulario, width=30, textvariable=self.precio)
        entry_precio.grid(column=2, row=3, sticky='w')
        
        label_cantidad_inicial=Label(frame_formulario, text="Cantidad Inicial:", bg= Constants.get_bgcolor())
        label_cantidad_inicial.grid(column=3, row=2, sticky='w', padx=10)
        self.cantidad_inicial=StringVar()
        entry_cantidad_inicial = Entry(frame_formulario, width=30, textvariable=self.cantidad_inicial)
        entry_cantidad_inicial.grid(column=3, row=3, sticky='w', padx=10)

        frame_formulario_botones = Frame(self.frame, bg= Constants.get_bgcolor())
        frame_formulario_botones.grid(column=0, row=2, sticky='nsew', padx=10, pady=10) 
        Button(frame_formulario_botones, text="Agregar", command=self.btn_agregar_click).grid(column=0, row=3, sticky='w')
        Button(frame_formulario_botones, text="Modificar", command=self.btn_modificar_click).grid(column=1, row=3, sticky='w', padx=10)
        Button(frame_formulario_botones, text="Eliminar", command=self.btn_eliminar_click).grid(column=2, row=3, sticky='w')

    def btn_agregar_click(self):
        if self.validar_campos_vacios():
            if self.buscar_codigo_existente(self.codigo.get()):
                Controls.mandar_advertencia("El codigo ya existe, por favor registre otro codigo.")
            else:
                self.insertar_producto(self.codigo.get(),self.nombre.get(),float(self.precio.get()),int(self.cantidad_inicial.get()))

    def btn_modificar_click(self):
        if self.validar_campos_vacios(False):
            if self.buscar_codigo_existente(self.codigo.get()):
                self.modificar_producto(self.codigo.get(),self.nombre.get(),float(self.precio.get()))
            else:
                Controls.mandar_advertencia("El codigo digitado no existe.")
                
    def btn_eliminar_click(self):
        if self.codigo.get() != "":
            if self.buscar_codigo_existente(self.codigo.get()):
                self.eliminar_producto(self.codigo.get())
            else:
                Controls.mandar_advertencia("El codigo digitado no existe.")
        else:
            Controls.mandar_advertencia("El codigo no puede estar vacio.")

    def listar_datos_tabla(self):
        self.tabla_productos.delete(*self.tabla_productos.get_children())
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)

        for fila in datos.values:
            arr_fila = []
            for celda in fila:
                arr_fila.append(celda)
            self.tabla_productos.insert("", "end", text = arr_fila[0], values= (arr_fila[1], arr_fila[2], arr_fila[3], arr_fila[4]))

    def insertar_producto(self, codigo, nombre, precio, cantidad):
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)

        values = Transform.dArray_to_array(datos.values)
        values.append([codigo,nombre,precio,cantidad,cantidad])

        Excel.guardar_excel(Constants.get_url_excel_productos(), self.HojaExcel, values, datos.columns)
        self.listar_datos_tabla()
        self.limpiar_campos()
        
    def modificar_producto(self, codigo, nombre, precio):
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)

        values = Transform.dArray_to_array(datos.values)

        for fila in values:
            if(fila[0] == codigo):
                fila[1] = nombre
                fila[2] = precio

        Excel.guardar_excel(Constants.get_url_excel_productos(), self.HojaExcel, values, datos.columns)
        self.listar_datos_tabla()
        self.limpiar_campos()

    def eliminar_producto(self, codigo):
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)

        values = []

        for fila in Transform.dArray_to_array(datos.values):
            if(fila[0] != codigo):
                values.append(fila)

        Excel.guardar_excel(Constants.get_url_excel_productos(), self.HojaExcel, values, datos.columns)
        self.listar_datos_tabla()
        self.limpiar_campos()

    def buscar_codigo_existente(self, codigo):
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)
        for fila in datos.values:
            if(fila[0] == codigo):
                return True
        return False

    def validar_campos_vacios(self, cantidad_inicial_necesario = True):
        resultado = False
        if self.codigo.get() == "":
            Controls.mandar_advertencia("El codigo no puede estar vacio")
        elif self.nombre.get() == "":
            Controls.mandar_advertencia("El nombre no puede estar vacio")
        elif self.precio.get() == "":
            Controls.mandar_advertencia("El precio no puede estar vacio")
        elif self.cantidad_inicial.get() == "" and cantidad_inicial_necesario:
            Controls.mandar_advertencia("Agregar una cantidad inicial para continuar")
        else:
            resultado = True
        return resultado

    def limpiar_campos(self):
        self.codigo.set("")
        self.nombre.set("")
        self.precio.set("")
        self.cantidad_inicial.set("")

    
    def obtener_proveedores_combo(self):
        datos = Excel.obtener_excel(Constants.get_url_excel_proveedores(), self.HojaExcel)
        resultado = []
        index = 0
        for fila in datos.values:
            resultado.append(fila[0]+" - "+fila[1])
            index += 1
        return resultado

    def restar_stock_producto(self, codigo, cantidad):
        print("prueba")