import sqlite3 as db

conn = db.connect('/tmp/course.s3db')
  
cur = conn.cursor()

# Закрыть соединение с базой данных
conn.close()

cur.excute('SELECT *FROM courses')
result = cur.fetchall()# Выбор всей таблицы

######### Выбор нескольких строк
#cur.fetchmany()
#   while True:
#   rows = cur.fetchmany()
#   if len(rows) == 0:
#    break
#   print('Got %d rows:' %len(rows))
#   for row in rows:
#   print(row)

########## Выбор только одной строки
#cur.fetchone()
#while True:
    #row = cur.fetchone()
    #if row is NOne:
     #   break
    #print(row)

# Вставляем данные в таблицу
# Здесь запрос, похожий на sqlite3 посредством команды cur.excute (запрос)
# Сохраняем изменения
conn.commit()# Закрепить данные после измениения (вставить данные в таблицу, удалить, update)

 
