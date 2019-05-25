//db project user net interface
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <string.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char **argv)
{

    int sockfd, n, i;
    char sendline[1000], recvline[1000];
    struct sockaddr_in servaddr;
    //char close_line_command[16] = "close";
    //int close_connection_flag = 0;

    if (argc != 2)
    {
        printf("Usage: a.out <IP address>\n");
        exit(1);
    }

    bzero(sendline, 1000);
    bzero(recvline, 1000);

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(51000);

    if (inet_aton(argv[1], &servaddr.sin_addr) == 0)
    {
        printf("Invalid IP address\n");
        exit(1);
    }

    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("Can\'t create socket, errno = %d\n", errno);
        exit(1);
    }

    if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0)
    {
        printf("Can\'t connect, errno = %d\n", errno);
        close(sockfd);
        exit(1);
    }

    printf("\n*************************************************************\n");
    printf("\nCONNECTION OK. WRITE q! to exit\n");
    printf("\nSELECT <...> from <...>\n");

    while (1)
    {
        printf("COMMAND => ");
        fflush(stdin);
        fgets(sendline, 1000, stdin);

        if (sendline[0] == 'q' && sendline[1] == '!')
        {
            close(sockfd);
            break;
        }

        if ((n = write(sockfd, sendline, strlen(sendline) + 1)) < 0)
        {
            printf("Can\'t write, errno = %d\n", errno);
            close(sockfd);
            exit(1);
        }

        if ((n = read(sockfd, recvline, 1000)) < 0)
        {
            printf("Can\'t read, errno = %d\n", errno);
            close(sockfd);
            exit(1);
        }
        printf("%s", recvline);
    }
    //close(sockfd);
    return 0;
}
