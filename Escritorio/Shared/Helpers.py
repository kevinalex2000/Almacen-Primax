from tkinter import  Label

class Controls:

    @staticmethod
    def colocarTitulo(frame, titulo):
        Label(frame, text = titulo, bg ='white', font=('Arial',16,'bold')).grid(column =0, row=0, sticky='w')
