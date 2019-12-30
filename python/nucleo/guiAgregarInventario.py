# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from nucleo.Gui.GUIAgregar_ui import Ui_MainWindow
from nucleo.LinkedList import *
from nucleo.Producto import *
from nucleo.guiDialogo import DialogoConfirmacion
class VentanaAgregar(QMainWindow):

    def __init__(self, parent = None):

        
        super(VentanaAgregar, self).__init__(parent)
        self.uiAgregar = Ui_MainWindow()
        self.uiAgregar.setupUi(self)
        self.uiDialogoConfirmacion = DialogoConfirmacion() # Es una instancia del dialogo de confirmacion
        self.listaProductos = LinkedList()


    """
        Metodos set y get de la lista de productos.
    """

    def getLista(self):
        lista = self.listaProductos
        return lista

    def setLista(self, lista):
        self.listaProductos = lista
        return True




    """
    Nombre: agregarProductos
    Parametros: No recibe parametros.
    Retorno: Retorna True en caso de que se agregue correctamente, False en caso contrario.
    Descripcion: Esta funcion agrega objetos de tipo producto a la lista enlazada.

    """

    def agregarProductos(self):
    

        # 1. Primero obtenemos los valores de los textBox y comboBox
        nombreProducto = self.uiAgregar.txtNombre.text()
        costoProducto = float(self.uiAgregar.txtCosto.text())
        tipoMoneda = str(self.uiAgregar.cbxMoneda.currentText())
        descripcionProducto = self.uiAgregar.txtDescripcion.toPlainText()
        idProducto = (int(self.listaProductos.GetSize()))
        """ 
        1.Se crea la instancia del objeto producto:
        2. Se asignan los valores a los atributos mediante los metodos set
         
        """
        agregarObjProducto = Producto() # Se crea la instancia
        # Se asignan valores a las variables mediante los metodos set

        agregarObjProducto.setNombreProducto(nombreProducto)
        agregarObjProducto.setCosto(costoProducto)
        agregarObjProducto.setMoneda(tipoMoneda)
        agregarObjProducto.setDescripcion(descripcionProducto)
        agregarObjProducto.setIdProducto(idProducto)

            
        self.listaProductos.LinkedListAdd(agregarObjProducto) # Se agrega el objeto a la Lista

        return True



