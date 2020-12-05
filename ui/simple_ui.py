# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\git_code\material_io\ui\simple_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from Qt import QtCore, QtGui, QtWidgets
from ui.refactor_widget import LineEdit


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(617, 122)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.file_path_line = QtWidgets.QLineEdit(Form)
        self.file_path_line.setObjectName("file_path_line")
        self.horizontalLayout.addWidget(self.file_path_line)
        self.selecet_path_btn = QtWidgets.QToolButton(Form)
        self.selecet_path_btn.setObjectName("selecet_path_btn")
        self.horizontalLayout.addWidget(self.selecet_path_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.export_btn = QtWidgets.QPushButton(Form)
        self.export_btn.setObjectName("export_btn")
        self.verticalLayout.addWidget(self.export_btn)
        self.import_btn = QtWidgets.QPushButton(Form)
        self.import_btn.setObjectName("import_btn")
        self.verticalLayout.addWidget(self.import_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Material import and export"))
        self.label.setText(_translate("Form", "File path:"))
        self.selecet_path_btn.setText(_translate("Form", "..."))
        self.export_btn.setText(_translate("Form", "Export"))
        self.import_btn.setText(_translate("Form", "Import"))
