from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame,messagebox
from tkinter.ttk import Style

from Shared.Helpers import Controls, Excel, Transform
from Shared.Constants import Constants

class DetallesHistorial:

    def __init__(self, tipo,codigo_historia,codigo_tercero,nombre_tercero, fecha):
        self.index=Tk()
        title = ""
        tercero = ""
        self.ruta_excel = ""

        if tipo == "ingreso":
            title = "Detalles de la Compra"
            tercero = "Proveedor"
            self.ruta_excel = Constants.get_url_excel_detalle_compras()
        elif tipo == "salida":
            title = "Detalles de la Venta"
            tercero = "Cliente"
            self.ruta_excel = Constants.get_url_excel_detalle_ventas()
        
        self.index.title(title+" " +codigo_historia)

        self.index.minsize(height= 500, width=400)
        self.index.resizable(width=False, height=False)
        
        self.frame_principal = Frame(self.index) ## Instanciamos nuevo Frame
        self.frame_principal.grid(column=1, row=1, sticky='nsew') ## Creamos la Grilla
        ## Configuramos el indice y espacio que ocupara
        self.frame_principal.columnconfigure(0, weight=1)
        self.frame_principal.rowconfigure(0, weight=1)

        self.frame_label = Frame(self.frame_principal)
        self.frame_label.grid(column=0, row=1, pady = 10, sticky='nsew') ## Creamos la Grilla

        lter= Label (self.frame_label, text=tercero+":")
        lter.grid(column=0, row=1, padx=10 , sticky='w')
        lter= Label (self.frame_label, text=nombre_tercero)
        lter.grid(column=1, row=1, padx=10 , sticky='w')

        lfecha= Label (self.frame_label, text="Fecha y Hora: ")
        lfecha.grid(column=0, row=2, padx=10 , pady = 5, sticky='w')
        lfecha= Label (self.frame_label, text=fecha)
        lfecha.grid(column=1, row=2, padx=10 , sticky='w')

        self.listar_tabla_detalles(codigo_historia)

        self.index.mainloop()

    def listar_tabla_detalles(self, codigo):

        self.frame_tabla_detalles = Frame(self.frame_principal, bg= Constants.get_bgcolor()) ## Creamos el frame para una tabla y colocamos el color de fondo
        self.frame_tabla_detalles.grid(columnspan=1, row=7, sticky='nsew', padx=10) ## Indicamos posicion y espacio del frame para la tabla
        self.tabla_detalles = ttk.Treeview(self.frame_tabla_detalles)  ## Creamos Tabla instanciando TreeView
        self.tabla_detalles.grid(column=0, row=0, sticky='nsew') ## Indicamos posicion y espacio de la tabla dentro del frame
        ladoy = ttk.Scrollbar(self.frame_tabla_detalles, orient ='vertical', command = self.tabla_detalles.yview) ## Agregamos scrollbar vertical instanciando Scrollbar
        ladoy.grid(column = 1, row = 0, sticky='ns') ## Indicamos la posicion y espaciado del scrollbar

        self.tabla_detalles.configure(yscrollcommand = ladoy.set) ## Configuramos comportamiento del scrollbar con la tabla
        self.tabla_detalles['columns'] = ('Nombre', 'Precio', 'Cantidad') ## Mencionamos las columnas tabla
        self.tabla_detalles.column('#0', minwidth=60, width=60, anchor='center') ## Colocamos Columna index
        self.tabla_detalles.column('Nombre', minwidth=100, width=130 , anchor='center') ## Colocamos Columna Nombre
        self.tabla_detalles.column('Precio', minwidth=100, width=120 , anchor='center') ## Colocamos Columna Precio
        self.tabla_detalles.column('Cantidad', minwidth=100, width=105, anchor='center') ## Colocamos Columna Cantidad

        self.tabla_detalles.heading('#0', text='Codigo', anchor ='center') ## Colocamos Cabecera de columna index
        self.tabla_detalles.heading('Nombre', text='Producto', anchor ='center') ## Colocamos Cabecera de columna Nombre
        self.tabla_detalles.heading('Precio', text='Cantidad', anchor ='center') ## Colocamos Cabecera de columna Precio
        self.tabla_detalles.heading('Cantidad', text='Precio Unitario', anchor ='center') ## Colocamos Cabecera de columna Cantidad

        datos = Excel.obtener_excel(self.ruta_excel, "Hoja1")
        values = Transform.dArray_to_array(datos.values)

        precio_total = 0

        for dato in values:
            if dato[5] == codigo:
                precio_total += float(dato[2])*float(dato[3])
                self.tabla_detalles.insert("", "end", text = dato[0], values= (dato[1], dato[2], dato[3]))

        
        lprecio_total= Label (self.frame_principal, text="Precio Total: "+str(precio_total),justify="right")
        lprecio_total.grid(column=0, row=8, padx=10 , pady = 10, sticky='w')