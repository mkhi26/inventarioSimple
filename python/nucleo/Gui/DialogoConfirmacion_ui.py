# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogoConfirmacion.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
"""
Este es el script generado atravez de PyQt5 designer, este codigo no se modifica, para acceder a el se 
utiliza la Clase DialogoConfirmacion.

"""


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogConfirmation(object):
    def setupUi(self, DialogConfirmation):
        DialogConfirmation.setObjectName("DialogConfirmation")
        DialogConfirmation.resize(411, 180)
        self.btnBox = QtWidgets.QDialogButtonBox(DialogConfirmation)
        self.btnBox.setGeometry(QtCore.QRect(30, 110, 341, 32))
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnBox.setObjectName("btnBox")
        self.label = QtWidgets.QLabel(DialogConfirmation)
        self.label.setGeometry(QtCore.QRect(130, 50, 101, 31))
        self.label.setObjectName("label")


        self.retranslateUi(DialogConfirmation)
        self.btnBox.accepted.connect(DialogConfirmation.accept)
        self.btnBox.rejected.connect(DialogConfirmation.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogConfirmation)

    def retranslateUi(self, DialogConfirmation):
        _translate = QtCore.QCoreApplication.translate
        DialogConfirmation.setWindowTitle(_translate("DialogConfirmation", "Diálogo de confirmación"))
        self.label.setText(_translate("DialogConfirmation", "¿Esta seguro?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogConfirmation = QtWidgets.QDialog()
    ui = Ui_DialogConfirmation()
    ui.setupUi(DialogConfirmation)
    DialogConfirmation.show()
    sys.exit(app.exec_())
