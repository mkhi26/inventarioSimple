# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from nucleo.Gui.GUIVerEditar_ui import Ui_VerEditar_ventana
class ventanaVerEditar (QMainWindow):

    def __init__(self, parent = None):

        
        super(ventanaVerEditar, self).__init__(parent)
        self.uiVerEditar = Ui_VerEditar_ventana()
        self.uiVerEditar.setupUi(self)