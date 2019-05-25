#!/bin/bash

echo
echo ДАННЫЙ СКРИПТ ВЫПОЛНИТ ПРЕДВАРИТЕЛЬНЫЕ ПРОВЕРКИ
DATE=`date '+%Y-%m-%d %H:%M:%S'`
echo $DATE

echo
echo ПРОВЕРКА СОСТОВНЫХ ЧАСТЕЙ СУБД...
FILE="main.py"
if [ -f $FILE ]; then
   echo "Файл '$FILE' существует."
else
   echo "Файл '$FILE' не найден."
   echo Дальнейшая работа невозможна. Завершение сценария
   echo
   exit
fi
echo ВСЕ ПРОВЕРКИ УСПЕШНО ПРОЙДЕНЫ!
echo

echo
echo ЗАПУСК СУБД...
python main.py
echo