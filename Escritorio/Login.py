
from tkinter import  Tk, Button, Entry, Label, ttk, BOTTOM
from tkinter import  StringVar
from tkinter.ttk import *
from App import Ventana
 
#Declaramos el index como variable para almacenar la funcion que llama a la ventana
index=Tk()
#Agregamos el titulo a la ventana
index.title("Iniciar Sesion")
#Definimos el tama�o de la ventana
index.minsize(height= 100, width=300)
index.geometry("300x125")
#Centramos la ventana
index.eval('tk::PlaceWindow . center')
#Hacemos que no pueda ser editable su tama�o
index.resizable(width=False, height=False)

#Declaramos la funcion Label que sera nuestra primera etiqueta
luser=Label(index, text="Ingrese nombre de usuario:")
#La funcion pack sirve para pintar la figura en la ventana 
luser.pack()

#Declaramos la variable de tipo cadena
user=StringVar()
#Se declara la caja de texto
euser=Entry(index, width=30, textvariable=user)
euser.pack()

lpas=Label(index, text="Ingrese la contrasena:")
lpas.pack()

pas=StringVar()
epas=Entry(index, width=30, textvariable=pas, show="*")
epas.pack()

#Creamos la funcion que validara los accesos
def ingresar():
    #Si el usuario es correcto
    if user.get()=="admin" and pas.get()=="admin":
        index.destroy()
        if __name__ == "__main__":
            #Hacemos el llamado de la nueva ventana
            ventana = Tk()
            ventana.title('Almacen de productos')
            ventana.minsize(height= 600, width=900)
            ventana.resizable(width=False, height=False)
            ventana.geometry('950x500+180+80')
            app = Ventana(ventana)
            app.mainloop()

    #Si el usuario en incorrecto
    else:
        obtener_error("Accesos incorrectos")

#Hacemos la creacion del boton  donde hacemos el llamado de la validacion
b1=Button(index, text="Entrar", command=ingresar)
b1.pack(side=BOTTOM)

def obtener_error(val):
    #Aca definimos el error 
    lacces=Label(index, text=val,foreground="red")
    lacces.pack()


index.mainloop()