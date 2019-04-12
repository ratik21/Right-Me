# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'short_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from final import Big_Dialog
import typo
import pyxhook
import sys,os
from functools import partial


newhook=pyxhook.HookManager()
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
big_window = Big_Dialog()
big_dialog = QtWidgets.QDialog()
big_window.setupUi(big_dialog)
big_dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        #Dialog.resize(102, 31)
        Dialog.setFixedSize(30, 30)
        self.button = QtWidgets.QPushButton(Dialog)
        #self.button.setGeometry(QtCore.QRect(0, 0, 92, 35))
        self.button.setGeometry(QtCore.QRect(0, 0, 30, 30))
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        #Dialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        #Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setStyleSheet(".QLineEdit {border-radius: 10000px;}")
        self.button.setText("")
        self.button.setObjectName("button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

def keyPress(event):
	global Dialog,newhook,app
	if event.Ascii == 96:
		newhook.cancel()
		Dialog.close()

def show_big_window(big_window_obj):
	big_window_obj.exec_()

def set_list(word_list):
	big_dialog.show()
	big_window.sug_list.clear()
	big_window.sug_list.addItems(word_list)

def change_selection():
	typo.change('corrector')
	big_dialog.hide()

def start_gui():
    global Dialog,app
    ui = Ui_Dialog()
    ui.setupUi(Dialog)	
    Dialog.show()
    ui.button.clicked.connect(partial(show_big_window, big_dialog))
    big_window.pushButton.clicked.connect(partial(change_selection))
    newhook.KeyDown=keyPress
    newhook.HookKeyboard()
    newhook.start()
    typo.main()
    sys.exit(app.exec_())
