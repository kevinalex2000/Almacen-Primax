from tkinter import  Label

from Shared.Constants import Constants

class Controls:

    @staticmethod
    def colocarTitulo(frame, titulo):
        Label(frame, text = titulo, bg =Constants.getBgColor(), font=('Arial',16,'bold')).grid(column =0, row=0, sticky='w', pady=10, padx=10)
