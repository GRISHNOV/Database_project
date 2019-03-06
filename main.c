#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <time.h>

#define DB_NAME "test.db"
#define DB_WORK_SPACE "db_work_dir"

#define FILE_NOT_EXIST -1
#define FILE_EXIST 0
#define DIR_NOT_EXIST -1
#define DIR_EXIST 0

#define MAX_SRTING_LEN_FROM_USER 64

/*int file_exists(char* file_name){

	FILE* ptr_file;

	ptr_file = fopen("test.db","r");
	if (ptr_file == NULL){
		printf("Внимание! Файл %s не существует\n", BD_NAME);
		return 0;
	}
	else{
		printf("Файл %s существует\n", BD_NAME);
		fclose(ptr_file);
	}
}*/

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

char *get_string_from_user(int max_len)
{
    char *data = (char *)malloc(MAX_SRTING_LEN_FROM_USER + 1);
    char buffer;
    int i = 0;

    buffer = getchar();
    while (buffer != '\n')
    {
        data[i] = buffer;
        i++;
        if (i > MAX_SRTING_LEN_FROM_USER)
        {
            printf("ERROR! No exception for MAX_SRTING_LEN_FROM_USER limit\n");
            // exceptions for db close()!!!
            exit(0);
        }
        buffer = getchar();
    }
    data[i] = '\0';
    //printf("\n%s\n", data);
    //free(data);

    return data;
}

/*static int callback(void *data, int argc, char **argv, char **azColName)
{
    int i;
    fprintf(stderr, "%s:", (const char *)data);
    for (i = 0; i <= argc; i++)
    {
        printf("%s = %s\n", azColName[i], argv[i]);
    }
    printf("\n");
    return 0;
}*/

static int callback(void *NotUsed, int argc, char **argv, char **azColName)
{
    int i;
    for (i = 0; i < argc; i++)
    {
        printf("%s = %s\n", azColName[i], argv[i] ? argv[i] : "NULL");
    }
    printf("\n");
    return 0;
}

int main(int argc, char *argv[], char *envp[])
{

    printf("\n_____ЗАПУСК ПРОГРАММЫ_____\n\n");

    clock_t start_time_point, end_time_point;
    double elapsed_CPU_time;

    start_time_point = clock();

    //(void)file_exists(BD_NAME);
    if (dir_exists(DB_WORK_SPACE) == DIR_NOT_EXIST)
    {
        printf("Не обнаружена рабочая директория для хранения баз данных. Создать её? Y/N\n");
        char buffer;
        scanf("%s", &buffer);
        if (buffer == 'Y' || buffer == 'y')
        {
            char temp_arg_1[32] = "mkdir ";
            char temp_arg_2[] = DB_WORK_SPACE;
            strcat(temp_arg_1, temp_arg_2);
            printf("%s\n", temp_arg_1);
            system(temp_arg_1);
        }
        else if (buffer == 'N' || buffer == 'n')
        {
            printf("Entered N! No exceptions for this!\n");
            exit(0);
        }
        else
        {
            printf("Error. Must be enter N or Y! No exceptions for this!\n");
            exit(0);
        }
    }

    if (file_exists(DB_WORK_SPACE "/" DB_NAME) == FILE_NOT_EXIST)
    {
        printf("Не обнаружен файл базы данных %s. Будет создана новая под таким именем. Продолжить? Y/N\n", DB_NAME);
        char buffer;
        scanf("%s", &buffer);
        if (buffer == 'Y' || buffer == 'y')
        {
            // nothing
        }
        else if (buffer == 'N' || buffer == 'n')
        {
            printf("Entered N! No exceptions for this!\n");
            exit(0);
        }
        else
        {
            printf("Error. Must be enter N or Y! No exceptions for this!\n");
            exit(0);
        }
    }

    sqlite3 *db;
    char *zErrMsg = NULL;
    int open_result;
    char *user_input = NULL;
    int operation_result;
    char *sql_command;
    //const char *data = "Callback function called";

    open_result = sqlite3_open(DB_WORK_SPACE "/" DB_NAME, &db);

    if (open_result != SQLITE_OK)
    {
        printf("Ошибка. Попытка открытия завершилась провалом с кодом: %s\n", sqlite3_errmsg(db));
        exit(0);
    }
    else
    {
        printf("Успешное открытие базы данных с именем %s\n\n", DB_NAME);
        printf("$$$ SQLITE_VERSION = %s $$$\n", SQLITE_VERSION);
    }

    printf("Введите команду длиной не более  MAX_SRTING_LEN_FROM_USER символов:\n");
    user_input = get_string_from_user(MAX_SRTING_LEN_FROM_USER);
    printf("Пользовательский ввод: %s\n", user_input);

    printf("\n\n");

    /* Create SQL statement */
    //sql_command = "SELECT * from books";
    //strcpy(sql_command, user_input);

    /* Execute SQL statement */
    operation_result = sqlite3_exec(db, /*sql_command*/ user_input, callback, /*(void *)data*/ NULL, &zErrMsg);
    if (operation_result != SQLITE_OK)
    {
        fprintf(stderr, "SQL error:%s\n", zErrMsg);
        sqlite3_free(zErrMsg);
    }
    else
    {
        fprintf(stdout, "Operation done successfully\n");
    }

    sqlite3_close(db);
    free(user_input);

    end_time_point = clock();
    elapsed_CPU_time = ((double)(end_time_point - start_time_point)) / CLOCKS_PER_SEC;
    printf("\n @@@ Затраченное процессорное время: %f @@@\n", elapsed_CPU_time);

    printf("\n_____ЗАВЕРШЕНИЕ ПРОГРАММЫ_____\n\n");
    return 0;
}