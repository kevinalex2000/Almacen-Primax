from tkinter import  Tk, Button, Entry, Label, ttk, PhotoImage, LEFT
from tkinter import  StringVar,Scrollbar,Frame

from Shared.Helpers import Controls

class ModuleClientes:

    def __init__(self,frame):
        ## Agregamos Titulo instanciando un elemento Label e indicandole su posicion
        Controls.colocarTitulo(frame, "Clientes")