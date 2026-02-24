#include<stdio.h>

int main()
{
    char letter = 'H';
    int lenght = 5;
    int width = 4;

    for(int i = 0 ; i < lenght ; i++)
    {
        for(int j = 0; j < width; j++)
        {
            printf("%c", letter);
        }
        
        printf("\n");
    }

    return 0;
}