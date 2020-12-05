# -*- coding: utf-8 -*-
import sys
import os
from Qt import QtWidgets

from ui.simple_ui import Ui_Form
from material_core import give_material, export_material


class MainWindow(QtWidgets.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self._ui = Ui_Form()
        self._ui.setupUi(self)
        self._connect()
        self.__root_cwd = None   # select ma file parent dir

    def _connect(self):
        self._ui.selecet_path_btn.clicked.connect(self.set_select_path)
        self._ui.export_btn.clicked.connect(lambda : export_material(self._ui.file_path_line.text()))
        self._ui.import_btn.clicked.connect(lambda : give_material(self._ui.file_path_line.text()))

    def set_select_path(self):
        root_cwd = self.__root_cwd if self.__root_cwd else os.getenv('temp')
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, "select ma file", root_cwd, "ma file (*.ma)")
        self._ui.file_path_line.clear()
        if isinstance(file_path, tuple):
            file_path = file_path[0]
        self.__root_cwd = os.path.dirname(file_path)
        self._ui.file_path_line.setText(file_path)


def main():
    global main_win
    main_win = MainWindow()
    main_win.show()



if __name__ == "__main__":
    # app = QtWidgets.QApplication([])
    main_win = MainWindow()
    main_win.show()
    # sys.exit(app.exec_())