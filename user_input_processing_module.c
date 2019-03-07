#define MAX_SRTING_LEN_FROM_USER 64

#include <stdlib.h>
#include <stdio.h>

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
    // free(data);

    return data;
}