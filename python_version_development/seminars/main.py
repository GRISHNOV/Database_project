#!/usr/bin/env python3

import sqlite3 as db

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QListWidgetItem, QFileDialog, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import Qt

FormUI, Form = uic.loadUiType("form_a.ui")

DB_PATH = "test.s3db"


class Window(Form):
    def __init__(self, parent=None):
        # Initialize UI (user interface)
        #super(Form, self).__init__()
        super(Window, self).__init__()
        self.ui = ui = FormUI()  # ui начинка окна
        ui.setupUi(self)
        # Connect handles to events
        ui.execute_button.clicked.connect(self.__execute)
        ui.db_select_button.clicked.connect(self.__select_db)
        ui.query_history.itemDoubleClicked.connect(self.__edit)
        # Connect to DB
        #self.conn = db.connect(DB_PATH)
        self.conn = db.connect(":memory:")  # Исключительно в ОЗУ

    def __del__(self):  # деструктор
        self.ui = None  # теперь будет подобрано сборщиком мусора
        # Diconnect DB
        self.conn.close()

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

        # Try to execute query
        cur = self.conn.cursor()
        try:  # две ветки
            cur.execute(query)
            self.conn.commit()  # сохраняем резальтат в базе
            result = cur.fetchall()
            error = None
        except Exception as exc:
            error = str(exc)
        cur.close()

        # Build formatted result string:

        # 1)Got some error:
        if error is not None:
            result_text = f'<span style="color: red;"><b>{error}</b></span>'
        # 2) No error and no result table
        else:
            # if len(result) == 0:  # избавимся от пустой строки от успешного запроса
            #    return
            if cur.description is None:
                result_text = f'Last inserted row id: {cur.lastrowid}'
            # 3) got some result (temporary table)
            else:
                result_text = '<table border=1>'
                result_text += '<tr>'
                for column_description in cur.description:
                    result_text += f'<td><b>{column_description[0]}</td></b>'
                result_text += '</tr>'
                for row in result:
                    result_text += '<tr>'
                    # сокращенная запись (через листкомпликейшн)
                    result_text += ''.join(f'<td>{cell}</td>' for cell in row)
                    # for cell in row:
                    #result_text += f'<td>{cell}</td>'
                    #result_text += '<td>%s</td>' % str(cell)
                    #result_text += str(cell)
                    #result_text += '</td>'
                    result_text += '</tr>'
                result_text += '</table>'
        # Create widget for the new list Item
        label = QLabel(result_text)
        list_item = QListWidgetItem()
        # Set proper dimesions for these widget
        label.resize(label.sizeHint())  # пересчёт размера
        list_item.setSizeHint(label.sizeHint())
        # Finally add element into list
        h.addItem(list_item)
        h.setItemWidget(list_item, label)

    def __select_db(self):
        # Request path for the new DB
        db_pathname, _ = QFileDialog.getOpenFileName()
        print(repr(db_pathname))
        if db_pathname is None:
            return
        # Try to connect to selected DB
        try:
            new_db_conn = db.connect(db_pathname)

        except Exception as exc:
            print("Failed to open DB:", type(exc), exc, file=sys.stderr)
        # Update UI and self.conn
        self.ui.db_path.setText(db_pathname)
        old_db_conn = self.conn
        self.conn = new_db_conn
        # Close connection to the old DB if there was one
        if old_db_conn is not None:
            return
        try:
            old_db_conn.close()
        except Exception as exc:
            print("Warning, failure while disconnecting from old DB:",
                  type(exc), exc, file=sys.stderr)

        """
        if self.conn is not None:
                self.conn.close()
            self.conn = db.connect(db_pathname)
            self.ui.db_path.setText(db_pathname)
        """

    def keyPressEvent(self, event):
        if self.ui.query_text.hasFocus():
            # if event.key() == Qt.Key_Return and self.ui.query_text.hasFocus():
                # self.__execute()
            # if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
                # self.__execute()
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):  # Работать будет последовательным сравнением
                self.__execute()


if __name__ == "__main__":
    print("_____START PROGRAM_____")
    app = QApplication(sys.argv)  # экзепляр ядра приложения
    w = Window()  # экземпляр окошка
    w.show()
    sys.exit(app.exec_())  # код завершения отдаём sys

    print("_____END PROGRAM_____")
