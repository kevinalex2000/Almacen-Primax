from tkinter import  Label, messagebox
from tkinter.constants import FALSE
import pandas as pd
from pandas import ExcelWriter
from pandas.core.indexes.base import Index

from Shared.Constants import Constants

class Controls:

    ## Coloca titulo en frame
    @staticmethod
    def colocar_titulo(frame, titulo):
        Label(frame, text = titulo, bg =Constants.get_bgcolor(), font=('Arial',16,'bold')).grid(column =0, row=0, sticky='w', padx=10, pady=10)

    ## Manda mensaje de advertencia    
    @staticmethod
    def mandar_advertencia(texto):
        messagebox.showwarning(title="Advertencia", message=texto)

    ## Manda mensaje de informacion
    @staticmethod
    def mandar_informacion(texto):
        messagebox.showinfo(title="Informacion", message=texto)

class Excel:

    ## Guarda datos en un excel
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

    ## Obtiene datos en un excel
    @staticmethod
    def obtener_excel(rutaExcel, hoja):
        df = pd.read_excel(rutaExcel, sheet_name=hoja);
        return df

class Transform:
    ## Transforma datos de un excel en array
    @staticmethod
    def dArray_to_array(darray):
        array = []
        for fila in darray:
            arrfila = []
            for valor in fila:
                arrfila.append(valor)
            array.append(arrfila)
        return array

class Validacion:
    ## Valida cadena en cantidad de caracteres
    @staticmethod
    def validar_n_caracteres(cadena, n):
        if(len(cadena) == int(n)):
            return True
        else:
            return False

    ## Valida si cadena es entero
    @staticmethod
    def validar_cadena_como_entero(cadena):
        return True if cadena.isdigit() else False
    
    ## Valida si cadena es entero o decimal
    @staticmethod
    def validar_cadena_como_decimal(cadena):
        try:
            float(cadena)
            return True
        except:
            return False