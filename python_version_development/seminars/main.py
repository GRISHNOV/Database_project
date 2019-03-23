#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
from PyQt5.QtCore import Qt

FormUI, Form = uic.loadUiType("form_a.ui")


class Window(Form):
    def __init__(self, parent=None):
        # Initialize UI (user interface)
        #super(Form, self).__init__()
        super(Window, self).__init__()
        self.ui = ui = FormUI()  # ui начинка окна
        ui.setupUi(self)
        # Connect handles to events
        ui.execute_button.clicked.connect(self.__execute)
        ui.query_history.itemDoubleClicked.connect(self.__edit)

    def __del__(self):  # деструктор
        self.ui = None  # теперь будет подобрано сборщиком мусора

    def __edit(self):
        item = self.ui.query_history.currentItem()
        if not item:
            return
        self.ui.query_text.setText(item.text())

    def __execute(self):
        # Fetch text from the edit box
        query = self.ui.query_text.text().strip()
        # Clear edit box
        self.ui.query_text.setText("")
        # Skip further steps if query is empty
        if query == "":
            return
        # Put query into history
        h = self.ui.query_history
        h.addItem(query)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return and self.ui.query_text.hasFocus():
            self.__execute()


if __name__ == "__main__":
    print("_____START PROGRAM_____")
    app = QApplication(sys.argv)  # экзепляр ядра приложения
    w = Window()  # экземпляр окошка
    w.show()
    sys.exit(app.exec_())  # код завершения отдаём sys

    print("_____END PROGRAM_____")
