from tkinter import  Label
from tkinter.constants import FALSE
import pandas as pd
from pandas import ExcelWriter
from pandas.core.indexes.base import Index

from Shared.Constants import Constants

class Controls:

    @staticmethod
    def colocarTitulo(frame, titulo):
        Label(frame, text = titulo, bg ='white', font=('Arial',16,'bold')).grid(column =0, row=0, sticky='w')
    

    @staticmethod
    def CrearExcelCliente():
        data = {
            'DNI': [],
            'Nombre': [],
            'Numero de Celular': [],
            'Direccion': []}
        
        df = pd.DataFrame(data, columns = ['DNI', 'Nombre', 'Numero de Celular', 'Direccion'])

        df.to_excel('Clientes.xlsx', sheet_name='Cliente',index=FALSE)   

    @staticmethod
    def InsertarExcelCliente(arrayCliente):
        data = {
            'DNI': [],
            'Nombre': [],
            'Numero de Celular': [],
            'Direccion': []}
        
        df = pd.DataFrame(data, columns = ['DNI', 'Nombre', 'Numero de Celular', 'Direccion'])

        df.to_excel('Clientes.xlsx', sheet_name='Cliente',index=FALSE)   
    @staticmethod
    def ObtenerExcelClientes():
        df = pd.read_excel('Clientes.xlsx', sheet_name='Cliente');
        return df