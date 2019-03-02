#include <stdio.h>
#include <stdlib.h>
#include <sqlite3.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>

#define DB_NAME "test.db"
#define DB_WORK_SPACE "db_work_dir"

#define FILE_NOT_EXIST -1
#define FILE_EXIST 0
#define DIR_NOT_EXIST -1
#define DIR_EXIST 0



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

int file_exists(char* file_path){
	if ( access(file_path,0) == 0 ){
        printf("Файл %s существует\n", file_path);
        return FILE_EXIST;
    }else{
        printf("Внимание! Файл %s не существует\n", file_path);
        return FILE_NOT_EXIST;
	}
}


int dir_exists(char* dir_path){
        if ( access(dir_path,0) == 0 ){
            printf("Директория %s существует\n", dir_path);
            return DIR_EXIST;
        }else{
            printf("Внимание! Директория %s не существует\n", dir_path);
            return DIR_NOT_EXIST;
        }
}

int main(void){

	printf("\nЗАПУСК ПРОГРАММЫ\n\n");

	//(void)file_exists(BD_NAME);
	if(dir_exists(DB_WORK_SPACE) == DIR_NOT_EXIST){
        printf("Не обнаружена рабочая директория для хранения баз данных. Создать её? Y/N\n");
        char buffer;
        scanf("%s",&buffer);
        if (buffer == 'Y' || buffer == 'y'){
            char temp_arg_1[32] = "mkdir ";
            char temp_arg_2[] = DB_WORK_SPACE;
            strcat(temp_arg_1,temp_arg_2);
            printf("%s\n",temp_arg_1);
            system(temp_arg_1);
        }
        else if (buffer == 'N' || buffer == 'n'){
            printf("Entered N! No exceptions for this!\n");
            exit(0);
        }
        else{
            printf("Error. Must be enter N or Y! No exceptions for this!\n");
            exit(0);
        }
	}

    if(file_exists(DB_WORK_SPACE"/"DB_NAME) == FILE_NOT_EXIST){
        printf("Не обнаружен файл базы данный %s. Будет создана новая под таким именем. Продолжить? Y/N\n", DB_NAME);
        char buffer;
        scanf("%s",&buffer);
        if (buffer == 'Y' || buffer == 'y'){
            // nothing
        }
        else if (buffer == 'N' || buffer == 'n'){
            printf("Entered N! No exceptions for this!\n");
            exit(0);
        }
        else{
            printf("Error. Must be enter N or Y! No exceptions for this!\n");
            exit(0);
        }
	}


	sqlite3* db;
   	char* zErrMsg = 0;
   	int open_result;

   	open_result = sqlite3_open(DB_WORK_SPACE"/"DB_NAME, &db);

   	if (open_result != SQLITE_OK) {
      		printf("Ошибка. Попытка открытия завершилась провалом с кодом: %s\n", sqlite3_errmsg (db));
      		exit(0);
   	} else {
      		printf("Успешное открытие базы данных с именем %s\n", DB_NAME);
   	}
   	sqlite3_close(db);

	printf("\nЗАВЕРШЕНИЕ ПРОГРАММЫ\n\n");
	return 0;

}
