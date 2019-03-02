#! /bin/bash
echo ЗАПУСК СЦЕНАРИЯ
echo Проверка рабочей директории

FILE=test.db
if [ -f $FILE ]; then
   echo "Файл '$FILE' существует."
else
   echo "Файл '$FILE' не найден."
fi

DIR=test_dir
if [ -d $DIR ]; then
   echo "Директория '$DIR' существует."
else
   echo "Директория '$DIR' не найдена."
fi

echo ЗАВЕРШЕНИЕ СЦЕНАРИЯ
