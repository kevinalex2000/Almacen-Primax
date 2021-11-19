from tkinter import  Label, messagebox
from tkinter.constants import FALSE
import pandas as pd
from pandas import ExcelWriter
from pandas.core.indexes.base import Index

from Shared.Constants import Constants

class Controls:

    @staticmethod
    def colocarTitulo(frame, titulo):
        Label(frame, text = titulo, bg =Constants.getBgColor(), font=('Arial',16,'bold')).grid(column =0, row=0, sticky='w', padx=10, pady=10)
    
    @staticmethod
    def MandarAdvertencia(texto):
        messagebox.showwarning(title="Advertencia", message=texto)

class Excel:

    @staticmethod
    def GuardarExcel(rutaExcel, hoja, datos, columnas):
        data = {}

        for columna in columnas:
            data[columna] = []

        for fila in datos:
            i = 0
            for celda in fila:
                data[columnas[i]].append(celda)
                i += 1
        
        df = pd.DataFrame(data, columns = columnas)
        df.to_excel(rutaExcel, sheet_name=hoja,index=FALSE)

    @staticmethod
    def ObtenerExcel(rutaExcel, hoja):
        df = pd.read_excel(rutaExcel, sheet_name=hoja);
        return df

class Transform:
    @staticmethod
    def dArrayToArray(darray):
        array = []
        for fila in darray:
            arrfila = []
            for valor in fila:
                arrfila.append(valor)
            array.append(arrfila)
        return array