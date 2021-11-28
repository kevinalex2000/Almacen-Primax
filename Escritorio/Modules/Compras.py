from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame,messagebox

from Shared.Helpers import Controls, Excel, Transform, Validacion
from Shared.Constants import Constants

from datetime import datetime


class ModuleCompras:

    def __init__(self,frame):

        self.frame = frame
        ## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
        Controls.colocar_titulo(frame, "Compras")
        self.HojaExcel = "Hoja1"
        self.datos_tabla = []
        self.precio_total = 0

        self.crear_formulario()
        self.crear_tabla()

    def crear_formulario(self):
        ## Formulario
        frame_formulario = Frame(self.frame, bg= Constants.get_bgcolor())
        frame_formulario.grid(column=0, row=1, sticky='nsew', padx=10) 

        label_codigo=Label(frame_formulario, text="Seleccione un Proveedor:", bg= Constants.get_bgcolor())
        label_codigo.grid(column=0, row=2, sticky='w')
        self.combo_proveedor = ttk.Combobox(frame_formulario, width=30)
        self.combo_proveedor.grid(column=0, row=3, sticky='w')
        self.combo_proveedor["values"] = self.obtener_proveedores_combo()
        
        label_codigo=Label(frame_formulario, text="Producto:", bg= Constants.get_bgcolor())
        label_codigo.grid(column=0, row=4, sticky='w')
        self.codigo=StringVar()
        self.combo_productos = ttk.Combobox(frame_formulario, width=30)
        self.combo_productos.grid(column=0, row=5, sticky='w')
        self.combo_productos["values"] = self.obtener_productos_combo()
        
        label_precio=Label(frame_formulario, text="Precio Unitario:", bg= Constants.get_bgcolor())
        label_precio.grid(column=2, row=4, sticky='w', padx=10)
        self.precio=StringVar()
        entry_precio = Entry(frame_formulario, width=30, textvariable=self.precio)
        entry_precio.grid(column=2, row=5, sticky='w', padx=10)
        
        label_cantidad=Label(frame_formulario, text="Cantidad:", bg= Constants.get_bgcolor())
        label_cantidad.grid(column=3, row=4, sticky='w')
        self.cantidad=StringVar()
        entry_cantidad = Entry(frame_formulario, width=30, textvariable=self.cantidad)
        entry_cantidad.grid(column=3, row=5, sticky='w')

        frame_formulario_botones = Frame(self.frame, bg= Constants.get_bgcolor())
        frame_formulario_botones.grid(column=0, row=2, sticky='nsew', padx=10, pady=10) 
        Button(frame_formulario_botones, text="Agregar", command = self.agregar_producto).grid(column=0, row=3, sticky='w')
        Button(frame_formulario_botones, text="Quitar", command = self.quitar_producto).grid(column=1, row=3, sticky='w', padx=10)

    def crear_tabla(self):
        #Creacion de la tabla
        self.frame_tabla_compra = Frame(self.frame, bg= Constants.get_bgcolor()) ## Creamos el frame para una tabla y colocamos el color de fondo
        self.frame_tabla_compra.grid(columnspan=1, row=4, sticky='nsew', padx=10, pady=10) ## Indicamos posicion y espacio del frame para la tabla
        self.tabla_compra = ttk.Treeview(self.frame_tabla_compra)  ## Creamos Tabla instanciando TreeView
        self.tabla_compra.grid(column=0, row=0, sticky='nsew') ## Indicamos posicion y espacio de la tabla dentro del frame
        ladoy = ttk.Scrollbar(self.frame_tabla_compra, orient ='vertical', command = self.tabla_compra.yview) ## Agregamos scrollbar vertical instanciando Scrollbar
        ladoy.grid(column = 1, row = 0, sticky='ns') ## Indicamos la posicion y espaciado del scrollbar

        self.tabla_compra.configure(yscrollcommand = ladoy.set) ## Configuramos comportamiento del scrollbar con la tabla
        self.tabla_compra['columns'] = ('Producto', 'Precio', 'Cantidad', 'Precio Total') ## Mencionamos las columnas tabla
        self.tabla_compra.column('#0', minwidth=100, width=120, anchor='center') ## Colocamos Columna index
        self.tabla_compra.column('Producto', minwidth=100, width=130 , anchor='center') ## Colocamos Columna Producto
        self.tabla_compra.column('Precio', minwidth=100, width=120 , anchor='center') ## Colocamos Columna Precio
        self.tabla_compra.column('Cantidad', minwidth=100, width=105, anchor='center') ## Colocamos Columna Cantidad
        self.tabla_compra.column('Precio Total', minwidth=100, width=105, anchor='center') ## Colocamos Columna Precio Total

        self.tabla_compra.heading('#0', text='Codigo', anchor ='center') ## Colocamos Cabecera de columna index
        self.tabla_compra.heading('Producto', text='Producto', anchor ='center') ## Colocamos Cabecera de columna Producto
        self.tabla_compra.heading('Precio', text='Precio', anchor ='center') ## Colocamos Cabecera de columna Precio
        self.tabla_compra.heading('Cantidad', text='Cantidad', anchor ='center') ## Colocamos Cabecera de columna Cantidad
        self.tabla_compra.heading('Precio Total', text='Precio Total', anchor ='center') ## Colocamos Cabecera de columna Precio Total

        
        Button(self.frame, text="Finalizar Compra", command=self.finalizar_compra).grid(columnspan=1, row=5, sticky='nsew', padx=10, pady=10) ## Creamos boton Finalizar compra

    ## Obtiene proveedores para combobox
    def obtener_proveedores_combo(self):
        datos = Excel.obtener_excel(Constants.get_url_excel_proveedores(), self.HojaExcel)
        resultado = []
        index = 0
        for fila in datos.values:
            resultado.append(fila[0]+" - "+fila[1])
            index += 1
        return resultado
    
    def obtener_productos_combo(self):
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)
        resultado = []
        index = 0
        for fila in datos.values:
            resultado.append(fila[0]+" - "+fila[1])
            index += 1
        return resultado
    
    ## Agrega producto en tabla
    def agregar_producto(self):
        if self.validar_formulario() == True:
            combo_producto = self.combo_productos.get()
            arr_producto = combo_producto.split("-")
            codigo_producto = arr_producto[0].strip()
            nombre_producto = arr_producto[1].strip()
            nueva = True
            for fila in self.datos_tabla:
                if fila[0] == codigo_producto:
                    nueva_cantidad = int(fila[3]) + int(self.cantidad.get())
                    fila[2] = self.precio.get()
                    fila[3] = nueva_cantidad
                    fila[4] = float(nueva_cantidad) * float(self.precio.get())
                    nueva = False
            if nueva:
                self.datos_tabla.append([codigo_producto,nombre_producto, self.precio.get(), self.cantidad.get(), float(self.precio.get())*float(self.cantidad.get())])
            self.listar_datos_tabla()
            self.limpiar_campos()

    ## Quita producto de la tabla
    def quitar_producto(self):
        if self.combo_productos.get() != "":
            combo_producto = self.combo_productos.get()
            arr_producto = combo_producto.split("-")
            codigo_producto = arr_producto[0].strip()
            nuevos_datos = []
            for fila in self.datos_tabla:
                if fila[0] != codigo_producto:
                    nuevos_datos.append(fila)
            self.datos_tabla = nuevos_datos
            self.listar_datos_tabla()
        else:
            Controls.mandar_advertencia("Seleccione un producto")

    ## Valida el formulario
    def validar_formulario(self):
        resultado = False
        if self.combo_productos.get() == "":
            Controls.mandar_advertencia("El nombre no puede estar vacio")
        elif self.precio.get() == "":
            Controls.mandar_advertencia("El precio no puede estar vacio")
        elif self.cantidad.get() == "":
            Controls.mandar_advertencia("La cantidad no puede ser vacia")
        elif Validacion.validar_cadena_como_decimal(self.precio.get()) == False:
            Controls.mandar_advertencia("El precio debe ser un numero")
        elif Validacion.validar_cadena_como_entero(self.cantidad.get()) == False:
            Controls.mandar_advertencia("la cantidad debe ser un numero entero")
        else:
            resultado = True
        return resultado
    
    ## Lista datos guardados temporalmente en tabla
    def listar_datos_tabla(self):
        self.tabla_compra.delete(*self.tabla_compra.get_children())
        precio_total = 0
        for fila in self.datos_tabla:
            arr_fila = []
            for celda in fila:
                arr_fila.append(celda)
            self.tabla_compra.insert("", "end", text = arr_fila[0], values= (arr_fila[1], arr_fila[2], arr_fila[3], arr_fila[4]))
            precio_total += float(arr_fila[4])
        self.precio_total = precio_total

    ## Limpia los campos
    def limpiar_campos(self):
        self.combo_productos.set("")
        self.precio.set("")
        self.cantidad.set("")

    ## Guarda la compra en los excels
    def finalizar_compra(self):
        if self.combo_proveedor.get() != "":
            if len(self.datos_tabla)>0:

                combo_proveedor = self.combo_proveedor.get()
                arr_proveedor = combo_proveedor.split("-")
                codigo_proveedor = arr_proveedor[0].strip()
                nombre_proveedor = arr_proveedor[1].strip()

                datos_compras = Excel.obtener_excel(Constants.get_url_excel_compras(), self.HojaExcel)
                datos_detalle_compras = Excel.obtener_excel(Constants.get_url_excel_detalle_compras(),self.HojaExcel)

                d_compras = Transform.dArray_to_array(datos_compras.values)
                d_detalle_compras = Transform.dArray_to_array(datos_detalle_compras.values)

                codigo_compra = "D"+ str(len(d_compras) + 1).zfill(4)
                fecha_compra = datetime.today().strftime('%d/%m/%Y %H:%M')

                d_compras.append([codigo_compra,fecha_compra,codigo_proveedor,nombre_proveedor, float(self.precio_total)])

                for fila in self.datos_tabla:
                    codigo_producto = fila[0]
                    nombre_producto = fila[1]
                    cantidad = float(fila[3])
                    precio = float(fila[2])
                    d_detalle_compras.append([codigo_producto,nombre_producto,cantidad,precio,precio*cantidad, codigo_compra])
                    self.sumar_stock(codigo_producto,cantidad)
            
                Excel.guardar_excel(Constants.get_url_excel_compras(), self.HojaExcel, d_compras, datos_compras.columns)
                Excel.guardar_excel(Constants.get_url_excel_detalle_compras(), self.HojaExcel, d_detalle_compras, datos_detalle_compras.columns)
            
                self.limpiar_campos()
                self.combo_proveedor.set("")
                self.tabla_compra.delete(*self.tabla_compra.get_children())

                Controls.mandar_informacion("Compra guardada exitosamente")     
            
            else:
                Controls.mandar_advertencia("Agregue productos para la compra")
        else:
            Controls.mandar_advertencia("Seleccione un proveedor para la compra")

    ## Aumenta el stock del producto
    def sumar_stock(self,codigo, cantidad):
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)
        values = Transform.dArray_to_array(datos.values)
        for value in values:
            if value[0] == codigo:
                value[3] = int(value[3])+int(cantidad)
                
        Excel.guardar_excel(Constants.get_url_excel_productos(), self.HojaExcel, values, datos.columns)