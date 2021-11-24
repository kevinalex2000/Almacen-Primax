from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame,IntVar

from Shared.Helpers import Controls, Excel
from Shared.Constants import Constants

class ModuleVentas:

    def __init__(self,frame):
        self.frame = frame
        ## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
        Controls.colocar_titulo(frame, "Ventas")
        ## Formulario
        self.crear_formulario()
        ##Creamos la tabla
        #Creacion de una tabla
        self.frame_tabla_ventas = Frame(frame, bg= Constants.get_bgcolor()) 
        self.frame_tabla_ventas.grid(columnspan=1, row=8, sticky='nsew', padx=10, pady=10) 
        self.tabla_ventas = ttk.Treeview(self.frame_tabla_ventas)  
        self.tabla_ventas.grid(column=0, row=0, sticky='nsew') 
        ladoy = ttk.Scrollbar(self.frame_tabla_ventas, orient ='vertical', command = self.tabla_ventas.yview) 
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla_ventas.configure(yscrollcommand = ladoy.set) 
        self.tabla_ventas['columns'] = ('Producto', 'Cantidad', 'Precio Unitario', 'Precio Total') 
        self.tabla_ventas.column('#0', minwidth=100, width=100, anchor='center')
        self.tabla_ventas.column('Producto', minwidth=100, width=180, anchor='center') 
        self.tabla_ventas.column('Cantidad', minwidth=100,width=180, anchor='center')
        self.tabla_ventas.column('Precio Unitario', minwidth=100,width=180, anchor='center')
        self.tabla_ventas.column('Precio Total', minwidth=100,width=180, anchor='center')

        self.tabla_ventas.heading('#0', text='Codigo Producto ', anchor ='center') 
        self.tabla_ventas.heading('Producto', text='Producto', anchor ='center') 
        self.tabla_ventas.heading('Cantidad', text='Cantidad', anchor ='center') 
        self.tabla_ventas.heading('Precio Unitario', text='Precio Unitario', anchor ='center')
        self.tabla_ventas.heading('Precio Total', text='Precio Total', anchor ='center')


    def crear_formulario(self):
        #Agregamos Subtitulo de Asignacion de Cliente para la venta
        Label(self.frame, text = 'Asigne el cliente al que se le realizara la venta:', bg = Constants.get_bgcolor(), font=('Arial',10,'bold')).grid(column =0, row=1, sticky='w', padx=10, pady=10)
        ## Formulario para la asignacion del DNI
        self.frame_formulario = Frame(self.frame, bg= Constants.get_bgcolor())
        self.frame_formulario.grid(column=0, row=2, sticky='nsew', padx=10) 
        #Dni
        label_dni=Label(self.frame_formulario, text="Dni:", bg= Constants.get_bgcolor())
        label_dni.grid(column=0, row=3, sticky='w')

        self.dni=StringVar()
        entry_dni = Entry(self.frame_formulario, width=30, textvariable=self.dni)
        entry_dni.grid(column=0, row=4, sticky='w')
        #Agregamos el boton para Buscar el Cliente
        Button(self.frame_formulario, text="Asignar", command=self.btn_asignar_cliente).grid(column=1, row=4, sticky='w')

        #IdProducto
        label_producto=Label(self.frame_formulario, text="Id Producto:", bg= Constants.get_bgcolor())
        label_producto.grid(column=0, row=6, sticky='w')

        self.producto=StringVar()
        entry_producto = Entry(self.frame_formulario, width=30, textvariable=self.producto)
        entry_producto.grid(column=0, row=7, sticky='w')
        #IdProducto
        label_cantidad=Label(self.frame_formulario, text="Cantidad:", bg= Constants.get_bgcolor())
        label_cantidad.grid(column=1, row=6, sticky='w')

        self.cantidad=StringVar()
        entry_cantidad = Entry(self.frame_formulario, width=30, textvariable=self.cantidad)
        entry_cantidad.grid(column=1, row=7, sticky='w')
         #Agregamos el boton para Agregar el producto
        Button(self.frame_formulario, text="Agregar", command=self.btn_agregar_producto).grid(column=2, row=7, sticky='w')
        Button(self.frame_formulario, text="Eliminar", command=self.btn_eliminar_producto).grid(column=2, row=7, sticky='w')
        Button(self.frame_formulario, text="Crear Venta", command=self.btn_crear_venta).grid(column=5, row=7, sticky='w')
    
    def btn_crear_venta(self):
        ##Agregamos la informacion de la tabla a los Excel
        print(self.tabla_ventas.get_children())


    def btn_asignar_cliente(self):
        if self.dni.get() == "":
            return Controls.mandar_advertencia("Asigne un cliente")
        #Buscamos el dni en el Excel de Clientes
        datos = Excel.obtener_excel("Data/Clientes.xlsx", "Hoja1")
        for fila in datos.values:
            if(fila[0] == int(self.dni.get())):
                valores = fila
                return self.MostrarAsignacion(valores)
        Controls.mandar_advertencia("El dni no existe, por favor registre al Cliente.")

    def btn_eliminar_producto(self):
        if self.producto.get() == "":
            return Controls.mandar_advertencia("Asigne un codigo de Producto")
        #Buscamos el producto en la tabla para eliminarlo 


    def btn_agregar_producto(self):
        if self.producto.get() == "":
            return Controls.mandar_advertencia("Asigne un codigo de Producto")
        elif self.cantidad.get() == "":
            return Controls.mandar_advertencia("Debe asignar una cantidad del producto")
        #Buscamos el producto en el Excel de Producto
        datos = Excel.obtener_excel("Data/Productos.xlsx", "Hoja1")
        for fila in datos.values:
            if(fila[0] == self.producto.get()):
                valores = fila
                return self.AgregarProductoTable(valores)
        Controls.mandar_advertencia("El producto no existe, por favor registre el producto.")
   
    def MostrarAsignacion(self,valores):
        #Creamos los Input bloqueados que cargaran la data del cliente
        #Nombre
        label_nombre=Label(self.frame_formulario, text="Nombre:", bg= Constants.get_bgcolor())
        label_nombre.grid(column=3, row=3, sticky='w')

        nombre = StringVar()
        nombre.set(valores[1])
        entry_nombre = Entry(self.frame_formulario, width=30, textvariable=nombre,state='disabled')
        entry_nombre.grid(column=3, row=4, sticky='w', padx=10, pady=10)

        #Telefono
        label_telefono=Label(self.frame_formulario, text="Telefono:", bg= Constants.get_bgcolor())
        label_telefono.grid(column=4, row=3, sticky='w')

        telefono = StringVar()
        telefono.set(valores[2])
        entry_telefono = Entry(self.frame_formulario, width=30, textvariable=telefono,state='disabled')
        entry_telefono.grid(column=4, row=4, sticky='w', padx=10, pady=10)

    def AgregarProductoTable(self,valores):
        #Validamos el stock del producto
        cantidad = int(self.cantidad.get())
        if valores[3] < cantidad:
            return Controls.mandar_advertencia("No hay stock del Producto")
        precio_total = valores[2] * cantidad
        self.tabla_ventas.insert("", "end", text = valores[0], values= (valores[1], cantidad, valores[2], precio_total))
        self.LimpiarInputs()
    
    def LimpiarInputs(self):
        self.producto.set("")
        self.cantidad.set("")