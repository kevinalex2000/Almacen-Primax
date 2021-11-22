from tkinter import  Label, messagebox
from tkinter.constants import FALSE
import pandas as pd
from pandas import ExcelWriter
from pandas.core.indexes.base import Index

from Shared.Constants import Constants

class Controls:

    @staticmethod
    def colocar_titulo(frame, titulo):
        Label(frame, text = titulo, bg =Constants.get_bgcolor(), font=('Arial',16,'bold')).grid(column =0, row=0, sticky='w', padx=10, pady=10)
    
    @staticmethod
    def mandar_advertencia(texto):
        messagebox.showwarning(title="Advertencia", message=texto)

class Excel:

    @staticmethod
    def guardar_excel(rutaExcel, hoja, datos, columnas):
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
    def obtener_excel(rutaExcel, hoja):
        df = pd.read_excel(rutaExcel, sheet_name=hoja);
        return df

class Transform:
    @staticmethod
    def dArray_to_array(darray):
        array = []
        for fila in darray:
            arrfila = []
            for valor in fila:
                arrfila.append(valor)
            array.append(arrfila)
        return array