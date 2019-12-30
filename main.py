"""Esta es la clase principal, mediante ella se ejecuta todo el proyecto.

"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets
from nucleo.Gui.GUIPrincipal_ui import Ui_MainWindow
from nucleo.guiVerEditar import ventanaVerEditar
from nucleo.guiAgregarInventario import VentanaAgregar
from nucleo.guiAcercaDe import VentanaAcercaDe
from nucleo.guiDialogo import DialogoConfirmacion


from nucleo.LinkedList import *
from nucleo.Producto import *


from nucleo.Gui.recursos_rc import *

class guiPrincipal(QMainWindow):
    def __init__(self,):
        super(guiPrincipal, self).__init__()

        

        # Se inisializa la ventana principal
        self.uiPrincipal = Ui_MainWindow()
        self.uiPrincipal.setupUi(self)

        # Se crean las instancias de las ventanas secundarias

        """
            Se crean instancias de las ventanas secundarias,
            para gestionarlas desde la ventana principal:
            1. self.uiAgregar: Es la instancia de la ventana Agregar a inventario.
            2. self.uiEditar: Es la instancia de la ventana ver y editar
            3. Falta el arbol binario de costos
            4. self.uiAcercaDe: Es la instancia de la ventana "Acerca de"

        """
        self.uiAgregar = VentanaAgregar()  # Instancia de la ventana "Agregar a inventario"
        self.uiEditar = ventanaVerEditar()  # Instancia de la ventana "ver y editar inventario"
        self.uiAcercaDe = VentanaAcercaDe() # Instancia de la ventana " Acerca de"
        self.uiDialogoConfirmacion = DialogoConfirmacion() # Es una instancia del dialogo de confirmacion



        self.listaProductos = self.uiAgregar.getLista()

        # Eventos de botones para la pantalla principal:

        """
            1. Evento Boton agregar a inventario: 
                Al hacer click en este boton se abrira la ventana para agregar elementos al inventario.
            2.Evento Boton Ver y editar inventario:
                Al hacer click en este boton se abrira la ventana para ver y editar los productos en inventario.
            3. Evento Boton Arbol binario de costos:
                Al hacer click en este boton se abrira la ventana para ver el arbol binario de costo
        
            4. Evento Boton Acerca de:
                Al hacer click en este boton se conectara con la ventana " Acerca de"
        """

        self.uiPrincipal.btnAgregarInventario.clicked.connect(self.eventoBtnAgregarInventario) # 1. Evento del boton "Agregar a inventario"
        self.uiPrincipal.btnVerEditar.clicked.connect(self.eventoBtnEditar) # 2. Evento del boton " Ver y editar inventario"
        self.uiPrincipal.btnAcercaDe.clicked.connect(self.eventoBtnAcercaDe) # 4. Evento del boton " Acerca de"


        # Evento para los botones de la ventana Agregar

        """
        Eventos de los botones de la ventana Agregar
        1. Agregar a inventario: Al hacer click en agregar se agregara el objeto al inventario
        2. Cancelar: Al hacer click en  cancelar se cancelara la accion de agregar

        """
        self.uiAgregar.uiAgregar.btnAgregar.clicked.connect(self.eventoBtnGuargar)





    # Funciones para conectar ventanas:


    """
        nombre: eventoBtnAgregarInventario
        parametros: no recibe parametros
        Retorno: Retorna True en caso de que la operacion se realiza con exito, False en caso contrario.
        Descripcion: Esta funcion permite conectar la ventana para Agregar productos desde la ventana principal.
    """

    def eventoBtnAgregarInventario(self):
        self.uiAgregar.show()
        return True

    """
        nombre: eventoBtnEditar
        parametros: no recibe parametros
        Retorno: Retorna True en caso de que la operacion se realiza con exito, False en caso contrario.
        Descripcion: Esta funcion permite conectar la ventana para ver y editar productos desde la ventana principal.
    """
    def eventoBtnEditar(self):   
        self.uiEditar.show()
        return True
    """
        nombre: eventoBtnAcercaDe
        parametros: no recibe parametros
        Retorno: Retorna True en caso de que la operacion se realiza con exito, False en caso contrario.
        Descripcion: Esta funcion permite conectar la ventana Acerca de desde la ventana principal.
    """

    def eventoBtnAcercaDe(self):
        self.uiAcercaDe.show()
        return True



    # Funciones para Gestionar Los productos agregados en la lista.

    def eventoBtnGuargar(self):
        self.uiDialogoConfirmacion.uiDialogo.label.setText("¿Agregar?")
        self.uiDialogoConfirmacion.show()
        
        resultado = self.uiDialogoConfirmacion.result()
        print(resultado)
        if( self.uiDialogoConfirmacion.uiDialogo.btnBox.clicked):
            print("se agregara")
        else:
            print("No se agregara")
        return False



    

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = guiPrincipal()
    main.show()
    sys.exit(app.exec_()) 