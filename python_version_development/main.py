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

# MAIN FUNCTION BLOCK


def main():
    print("Для работы программы необходима дирректория " +
          DB_WORK_SPACE + " и файл " + DB_NAME)
    if os.path.exists(DB_WORK_SPACE):
        print("Рабочая директория обнаружена")

    else:
        print("Не обнаружена рабочая директория для хранения баз данных. Создать её? Y/N")
        while(1):
            buffer = input("[Y/N]: ")
            if (buffer == "Y" or buffer == "y"):
                os.mkdir(DB_WORK_SPACE)
                break
            elif (buffer == "N" or buffer == "n"):
                print("Отказ создания рабочей директории. Завершение работы")
                sys.exit(0)
            else:
                print("Некорректный ввод. Повторите")

    if os.path.exists("./" + DB_WORK_SPACE + "/" + DB_NAME):
        print("Файл базы данных обнаружен")
    else:
        print("Не обнаружен файл базы данных. Будет создана новая. Продолжить? Y/N")
        while(1):
            buffer = input("[Y/N]: ")
            if (buffer == "Y" or buffer == "y"):
                break
            elif (buffer == "N" or buffer == "n"):
                print("Отказ создания. Завершение программы")
                sys.exit(0)
            else:
                print("Некорректный ввод. Повторите")

    print("\n@@@ sqlite3.version = ", sqlite3.version, "@@@\n")
    user_input = input("Введите команду: ")
    con = sqlite3.connect("./" + DB_WORK_SPACE + "/" + DB_NAME)

    fd = pd.read_sql(user_input, con)
    print(fd)
    print("\n", type(fd), "\n")
    f = open('text.txt', 'a')
    f.write("\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    f.write("Реакция на команду пользователя: " + user_input)
    f.write("\n@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    f.write("\n$$$$$$$$$$$$$$$$$$$$$$$$$\n")
    f.write(str(fd))
    f.write("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n")
    f.close

    con.close()

    # cursorObj = con.cursor()

    # cursorObj.execute('SELECT name from sqlite_master where type= "table"')

    # print(cursorObj.fetchall())

    # cursorObj.execute(user_input)

    # rows = cursorObj.fetchall()

    # for row in rows:

    #     print(row)

    # con.close()

# END MAIN FUNCTION BLOCK


# MAIN SCRIPT OF PROGRAM
if __name__ == '__main__':
    print("\n_____ЗАПУСК ПРОГРАММЫ_____\n")
    main()
    print("\n_____ЗАВЕРШЕНИЕ ПРОГРАММЫ_____\n")
# END MAIN SCRIPT OF PROGRAM
