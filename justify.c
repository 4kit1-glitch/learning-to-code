#include<stdio.h>
#define FORTY 40

int main()
{
    int lenght;
    char word = 'a';

    lenght =  FORTY - 1;

    for(int i = 0; i <= lenght ; i++)
    {
        printf(" ");
    }
    printf("%c\n",word);

    return 0;
}