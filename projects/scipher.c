// code ciphers a text by converting a letter to its succesive one
// c is easier than python for my why is that

#include<stdio.h>

int main()
{
    char ch;

    printf("enter a message: ");

    ch = getchar();

    while (ch != '\n')
    {
        printf("%c" , (ch + 1));

        ch = getchar();
    }
    
    printf("\n");




    return 0;
}