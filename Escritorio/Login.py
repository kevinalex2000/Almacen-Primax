
from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, BOTTOM
from tkinter import  StringVar,Scrollbar,Frame
from tkinter.ttk import *
from App import Ventana
 
 
index=Tk()
index.title("LOGIN")
index.geometry("300x125")
index.resizable(width=False, height=False)

luser=Label(index, text="Ingrese nombre de usuario:")
luser.pack()

user=StringVar()
euser=Entry(index, width=30, textvariable=user)
euser.pack()

lpas=Label(index, text="Ingrese la contrasena:")
lpas.pack()

pas=StringVar()
epas=Entry(index, width=30, textvariable=pas, show="*")
epas.pack()


def ingresar():
    if user.get()=="admin" and pas.get()=="admin":
        index.destroy()
        if __name__ == "__main__":
            ventana = Tk()
            ventana.title('Almacen de productos')
            ventana.minsize(height= 600, width=900)
            ventana.geometry('1000x500+180+80')
            app = Ventana(ventana)
            app.mainloop()

    else:
        ObtenerError("Accesos incorrectos")
   
b1=Button(index, text="Entrar", command=ingresar)
b1.pack(side=BOTTOM)

def ObtenerError(val):
    #Aca definimos el error 
    #val=StringVar()
    lacces=Label(index, text=val,foreground="red")
    lacces.pack()


index.mainloop()