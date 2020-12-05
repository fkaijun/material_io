# -*- coding: utf-8 -*-
from Qt import QtWidgets

class LineEdit(QtWidgets.QLineEdit):

    def __init__(self, parent=None):
        super(LineEdit, self).__init__()
        self.setDragEnabled(True)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if ( urls and urls[0].scheme() == 'file' ):
            self.__file_path = str(urls[0].path())[1:]
            if self.__file_path.endswith('.ma'):
                event.accept()
            else:
                event.ignore()

    def dropEvent(self, event):
        self.setText(self.__file_path)
