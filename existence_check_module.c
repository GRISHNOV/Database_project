#define FILE_NOT_EXIST -1
#define FILE_EXIST 0
#define DIR_NOT_EXIST -1
#define DIR_EXIST 0

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int file_exists(char *file_path)
{
    if (access(file_path, 0) == 0)
    {
        printf("Файл %s существует\n", file_path);
        return FILE_EXIST;
    }
    else
    {
        printf("Внимание! Файл %s не существует\n", file_path);
        return FILE_NOT_EXIST;
    }
}

int dir_exists(char *dir_path)
{
    if (access(dir_path, 0) == 0)
    {
        printf("Директория %s существует\n", dir_path);
        return DIR_EXIST;
    }
    else
    {
        printf("Внимание! Директория %s не существует\n", dir_path);
        return DIR_NOT_EXIST;
    }
}