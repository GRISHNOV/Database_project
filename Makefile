#all:
#	@echo "Beginning build at:"
#	@date
#	@echo "--------"

main.out: main.o user_input_processing_module.o existence_check_module.o
	gcc ./main.o ./user_input_processing_module.o ./existence_check_module.o -lsqlite3 -o ./main.out

user_input_processing_module.o: user_input_processing_module.c user_input_processing_module.h
	gcc -Wall ./user_input_processing_module.c -c -o ./user_input_processing_module.o

existence_check_module.o: existence_check_module.c existence_check_module.h
	gcc -Wall ./existence_check_module.c -c -o ./existence_check_module.o

main.o: main.c user_input_processing_module.h existence_check_module.h
	gcc -Wall ./main.c -lsqlite3 -c -o ./main.o

# -lsqlite3