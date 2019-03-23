#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
    QWidget, QApplication,
    QGridLayout, QPushButton
)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("My first window")
        grid = QGridLayout()
        self.setLayout(grid)
        button = QPushButton("Push me!", self)
        # button.clicked.connect(
        #     lambda: print("Button was pushed")
        # )
        button.clicked.connect(self.__on_button_click)
        grid.addWidget(button, 0, 0)
        self.__counter = 0

    def __on_button_click(self):
        print("Button was pushed. Counter: %d" % self.__counter)
        # s = "Button was pushed. Counter: %d" % self.__counter
        # print(s)
        # s = f"Button was pushed. Counter: {self.__counter}"
        # print(s)
        # print(f"Button was pushed. Counter: {self.__counter}")
        self.__counter += 1


if __name__ == "__main__":
    print("_____START PROGRAM_____")
    app = QApplication(sys.argv)  # экзепляр ядра приложения
    w = Window()  # экземпляр окошка
    w.show()
    # app.exec_()
    sys.exit(app.exec_())  # код завершения отдаём sys

    print("_____END PROGRAM_____")
