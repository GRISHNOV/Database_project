import os
import sys
import pandas as pd
import sqlite3

# CONST BLOCK

DB_NAME = "test.db"
DB_WORK_SPACE = "db_work_dir"

FILE_NOT_EXIST = -1
FILE_EXIST = 0
DIR_NOT_EXIST = -1
DIR_EXIST = 0

MAX_SRTING_LEN_FROM_USER = 64

# END CONST BLOCK

# MAIN BLOCK

print("\n_____ЗАПУСК ПРОГРАММЫ_____\n")

if os.path.exists(DB_WORK_SPACE):
    print("Рабочая директория обнаружена")
else:
    print("Не обнаружена рабочая директория для хранения баз данных. Создать её? Y/N")
    buffer = input()
    if (buffer == "Y" or buffer == "y"):
        os.mkdir(DB_WORK_SPACE)
    elif (buffer == "N" or buffer == "n"):
        print("Если отказ создания рабочей директории")
    else:
        print("Некорректный ввод")

if os.path.exists("./" + DB_WORK_SPACE + "/" + DB_NAME):
    print("Файл базы данных обнаружен")
else:
    print("Не обнаружен файл базы данных. Будет создана новая. Продолжить? Y/N")
    buffer = input()
    if (buffer == "Y" or buffer == "y"):
        print("При открытии будет создана новая")
    elif (buffer == "N" or buffer == "n"):
        print("Отказ создания")
    else:
        print("Некорректный ввод")

print("\n@@@ sqlite3.version = ",sqlite3.version,"@@@\n")
user_input = input()
connection = sqlite3.connect("./" + DB_WORK_SPACE + "/" + DB_NAME)
fd = pd.read_sql(user_input, connection)
print(fd)

connection.close()

print("\n_____ЗАВЕРШЕНИЕ ПРОГРАММЫ_____\n")

# END MAIN BLOCK
