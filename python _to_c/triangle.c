
#include<stdio.h>

int main()
{
    char letter  = 'l';
    int rows = 5;

    for(int i = 0 ; i < rows ; i++)
    {
        for(int j = 0 ; j <= i ; j++)
        {
            printf("%c", letter);
        }
        printf("\n");
    }

    return 0;
}