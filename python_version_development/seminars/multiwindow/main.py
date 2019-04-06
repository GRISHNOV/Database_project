#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

UI_MainWindow, MainWindowBase = uic.loadUiType("form_main.ui")
UI_Form1, Form1Base = uic.loadUiType("form_one.ui")
UI_Form2, Form2Base = uic.loadUiType("form_two.ui")

...


class Form1(Form1Base):
    def __init__(self, parent=None):
        # super(MainWindow,self).__init__(parent)
        Form1Base.__init__(self, parent)
        self.ui = UI_Form1()
        self.ui.setupUi(self)
        self.ui.button_1.clicked.connect(
            lambda: self.parent().replace_with(Form2(self.parent()))
        )
        if parent:
            parent.setWindowTitle("Form1")

    def __del__(self):
        self.ui = None

    def form_title(self):
        return 'Form1'


class Form2(Form2Base):
    def __init__(self, parent=None):
        # super(MainWindow,self).__init__(parent)
        Form2Base.__init__(self, parent)
        self.ui = UI_Form2()
        self.ui.setupUi(self)
        self.ui.button_2.clicked.connect(
            lambda: self.parent().replace_with(Form1(self.parent()))
        )
        if parent:
            parent.setWindowTitle("Form2")

    def __del__(self):
        self.ui = None

    def form_title(self):
        return 'Form2'


class MainWindow(MainWindowBase):
    def __init__(self, parent=None):
        # super(MainWindow,self).__init__(parent)
        MainWindowBase.__init__(self, parent)
        self.ui = UI_MainWindow()
        self.ui.setupUi(self)
        # application begins from Form1 view
        self.current_form = Form1(self)
        self.setWindowTitle(self.current_form.form_title())
        self.ui.main_layout.addWidget(self.current_form)
        # self.current_form.setParent(None)
        #self.current_form = new_form
        # self.setWindowTitle(new_form.form_title())

    def __del__(self):
        self.ui = None

    def replace_with(self, new_form):
        self.ui.main_layout.replaceWidget(self.current_form, new_form)
        self.current_form.setParent(None)
        self.current_form = new_form


if __name__ == "__main__":
    # create application object
    app = QApplication(sys.argv)
    # create main window
    main_window = MainWindow()
    #main_window.setWindowTitle("Main form")
    main_window.show()
    # enter main loop
    sys.exit(app.exec_())
