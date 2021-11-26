from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame,messagebox

from Shared.Helpers import Controls, Excel, Transform
from Shared.Constants import Constants

from datetime import datetime


class ModuleVentas:

    def __init__(self,frame):

        self.frame = frame
        ## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
        Controls.colocar_titulo(frame, "Ventas")
        self.HojaExcel = "Hoja1"
        self.datos_tabla = []
        self.precio_total = 0

        self.crear_formulario()
        self.crear_tabla()

    def crear_formulario(self):
        ## Formulario
        frame_formulario = Frame(self.frame, bg= Constants.get_bgcolor())
        frame_formulario.grid(column=0, row=1, sticky='nsew', padx=10) 

        label_codigo=Label(frame_formulario, text="Seleccione un Cliente:", bg= Constants.get_bgcolor())
        label_codigo.grid(column=0, row=2, sticky='w')
        self.combo_cliente = ttk.Combobox(frame_formulario, width=30)
        self.combo_cliente.grid(column=0, row=3, sticky='w')
        self.combo_cliente["values"] = self.obtener_clientes_combo()
        
        label_codigo=Label(frame_formulario, text="Producto:", bg= Constants.get_bgcolor())
        label_codigo.grid(column=0, row=4, sticky='w')
        self.codigo=StringVar()
        self.combo_productos = ttk.Combobox(frame_formulario, width=30)
        self.combo_productos.grid(column=0, row=5, sticky='w')
        self.combo_productos["values"] = self.obtener_productos_combo()
        self.combo_productos.bind("<<ComboboxSelected>>", self.producto_seleccionado)
        
        label_precio=Label(frame_formulario, text="Precio Unitario:", bg= Constants.get_bgcolor())
        label_precio.grid(column=2, row=4, sticky='w', padx=10)
        self.precio=StringVar()
        entry_precio = Entry(frame_formulario, width=30, textvariable=self.precio,state='disabled')
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
        self.frame_tabla_venta = Frame(self.frame, bg= Constants.get_bgcolor()) ## Creamos el frame para una tabla y colocamos el color de fondo
        self.frame_tabla_venta.grid(columnspan=1, row=4, sticky='nsew', padx=10, pady=10) ## Indicamos posicion y espacio del frame para la tabla
        self.tabla_venta = ttk.Treeview(self.frame_tabla_venta)  ## Creamos Tabla instanciando TreeView
        self.tabla_venta.grid(column=0, row=0, sticky='nsew') ## Indicamos posicion y espacio de la tabla dentro del frame
        ladoy = ttk.Scrollbar(self.frame_tabla_venta, orient ='vertical', command = self.tabla_venta.yview) ## Agregamos scrollbar vertical instanciando Scrollbar
        ladoy.grid(column = 1, row = 0, sticky='ns') ## Indicamos la posicion y espaciado del scrollbar

        self.tabla_venta.configure(yscrollcommand = ladoy.set) ## Configuramos comportamiento del scrollbar con la tabla
        self.tabla_venta['columns'] = ('Producto', 'Precio', 'Cantidad', 'Precio Total') ## Mencionamos las columnas tabla
        self.tabla_venta.column('#0', minwidth=100, width=120, anchor='center') ## Colocamos Columna index
        self.tabla_venta.column('Producto', minwidth=100, width=130 , anchor='center') ## Colocamos Columna Nombre
        self.tabla_venta.column('Precio', minwidth=100, width=120 , anchor='center') ## Colocamos Columna Precio
        self.tabla_venta.column('Cantidad', minwidth=100, width=105, anchor='center') ## Colocamos Columna Cantidad
        self.tabla_venta.column('Precio Total', minwidth=100, width=105, anchor='center') ## Colocamos Columna Precio Total

        self.tabla_venta.heading('#0', text='Codigo', anchor ='center') ## Colocamos Cabecera de columna index
        self.tabla_venta.heading('Producto', text='Producto', anchor ='center') ## Colocamos Cabecera de columna Nombre
        self.tabla_venta.heading('Precio', text='Precio', anchor ='center') ## Colocamos Cabecera de columna Precio
        self.tabla_venta.heading('Cantidad', text='Cantidad', anchor ='center') ## Colocamos Cabecera de columna Cantidad
        self.tabla_venta.heading('Precio Total', text='Precio Total', anchor ='center') ## Colocamos Cabecera de columna Precio Total

        
        Button(self.frame, text="Finalizar Venta", command=self.finalizar_compra).grid(columnspan=1, row=5, sticky='nsew', padx=10, pady=10)

    def obtener_clientes_combo(self):
        datos = Excel.obtener_excel(Constants.get_url_excel_clientes(), self.HojaExcel)
        resultado = []
        index = 0
        for fila in datos.values:
            resultado.append(str(fila[0])+" - "+fila[1])
            index += 1
        resultado.sort()
        return resultado
    
    def obtener_productos_combo(self):
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)
        resultado = []
        index = 0
        for fila in datos.values:
            resultado.append(fila[0]+" - "+fila[1])
            index += 1
        resultado.sort()
        return resultado

    def agregar_producto(self):
        if self.validar_formulario() == True:
            combo_producto = self.combo_productos.get()
            arr_producto = combo_producto.split("-")
            codigo_producto = arr_producto[0].strip()
            ##Validamos el stock del producto   
            if self.validar_stock(codigo_producto):
                return Controls.mandar_advertencia("No hay stock del Producto")
            
            nombre_producto = arr_producto[1].strip()
            nueva = True
            for fila in self.datos_tabla:
                if fila[0] == codigo_producto:
                    nueva_cantidad = int(fila[3]) + int(self.cantidad.get())
                    fila[2] = self.precio.get()
                    fila[3] = nueva_cantidad
                    fila[4] = float(nueva_cantidad) * float(self.precio.get())
                    nueva = False
                    if self.validar_stock_existente(codigo_producto,nueva_cantidad):
                        return Controls.mandar_advertencia("No hay stock del Producto")
            if nueva:
                self.datos_tabla.append([codigo_producto,nombre_producto, self.precio.get(), self.cantidad.get(), float(self.precio.get())*float(self.cantidad.get())])
            self.listar_datos_tabla()
            self.limpiar_campos()

    def validar_stock(self,codigo_producto):
        resultado = False
        ##Validamos el stock del producto        
        cantidad_validar = int(self.cantidad.get())
        #Buscamos el producto en el Excel de Producto
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)
        for fila in datos.values:
                if(fila[0] == codigo_producto):
                    if fila[3] < cantidad_validar:
                        resultado = True
        return resultado

    def validar_stock_existente(self,codigo_producto,cantidad_validar):
        resultado = False
        ##Validamos el stock del producto        
        #Buscamos el producto en el Excel de Producto
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)
        for fila in datos.values:
                if(fila[0] == codigo_producto):
                    if fila[3] < cantidad_validar:
                        resultado = True
        return resultado

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

    def validar_formulario(self):
        resultado = False
        if self.combo_productos.get() == "":
            Controls.mandar_advertencia("El nombre no puede estar vacio")
        elif self.precio.get() == "":
            Controls.mandar_advertencia("El precio no puede estar vacio")
        elif self.cantidad.get() == "":
            Controls.mandar_advertencia("La cantidad no puede ser vacia")
        else:
            resultado = True
        return resultado
    
    def listar_datos_tabla(self):
        self.tabla_venta.delete(*self.tabla_venta.get_children())
        precio_total = 0
        for fila in self.datos_tabla:
            arr_fila = []
            for celda in fila:
                arr_fila.append(celda)
            self.tabla_venta.insert("", "end", text = arr_fila[0], values= (arr_fila[1], arr_fila[2], arr_fila[3], arr_fila[4]))
            precio_total += float(arr_fila[4])
        self.precio_total = precio_total

    def limpiar_campos(self):
        self.combo_productos.set("")
        self.precio.set("")
        self.cantidad.set("")

    def finalizar_compra(self):
        if self.combo_cliente.get() != "":
            if len(self.datos_tabla)>0:

                combo_cliente = self.combo_cliente.get()
                arr_cliente = combo_cliente.split("-")
                codigo_cliente = arr_cliente[0].strip()
                nombre_cliente = arr_cliente[1].strip()

                datos_ventas = Excel.obtener_excel(Constants.get_url_excel_ventas(), self.HojaExcel)
                datos_detalle_ventas = Excel.obtener_excel(Constants.get_url_excel_detalle_ventas(),self.HojaExcel)

                d_ventas = Transform.dArray_to_array(datos_ventas.values)
                d_detalle_ventas = Transform.dArray_to_array(datos_detalle_ventas.values)

                codigo_venta = "V"+ str(len(d_ventas) + 1).zfill(4)
                fecha_venta = datetime.today().strftime('%d/%m/%Y %H:%M')

                d_ventas.append([codigo_venta,fecha_venta,codigo_cliente,nombre_cliente, float(self.precio_total)])

                for fila in self.datos_tabla:
                    codigo_producto = fila[0]
                    nombre_producto = fila[1]
                    cantidad = float(fila[3])
                    precio = float(fila[2])
                    d_detalle_ventas.append([codigo_producto,nombre_producto,cantidad,precio,precio*cantidad, codigo_venta])
                    self.sumar_stock(codigo_producto,cantidad)
            
                Excel.guardar_excel(Constants.get_url_excel_ventas(), self.HojaExcel, d_ventas, datos_ventas.columns)
                Excel.guardar_excel(Constants.get_url_excel_detalle_ventas(), self.HojaExcel, d_detalle_ventas, datos_detalle_ventas.columns)
            
                
                self.limpiar_campos()
                self.combo_cliente.set("")
                self.tabla_venta.delete(*self.tabla_venta.get_children())

                Controls.mandar_informacion("Venta guardada exitosamente")     
            
            else:
                Controls.mandar_advertencia("Agregue productos para la venta")
        else:
            Controls.mandar_advertencia("Seleccione un cliente para la venta")

    def sumar_stock(self,codigo, cantidad):
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)
        values = Transform.dArray_to_array(datos.values)
        for value in values:
            if value[0] == codigo:
                value[3] = int(value[3])-int(cantidad)
                
        Excel.guardar_excel(Constants.get_url_excel_productos(), self.HojaExcel, values, datos.columns)

    def producto_seleccionado(self,arg):
        value = self.combo_productos.get()
        producto = value.split(" - ")
        #Buscamos el producto en el Excel de Producto
        datos = Excel.obtener_excel(Constants.get_url_excel_productos(), self.HojaExcel)
        for fila in datos.values:
            if(fila[0] == producto[0]):
                valores = fila
                self.precio.set(valores[2])
                
        