// computes the greatest common factor of two numbers

#include<stdio.h>

int gdc(int x, int y);

int main()
{   
    int x, y;

    printf("enter the numbers(x,y): ");
    scanf(" %d,%d", &x, &y);

    printf("the gdc is %d\n", gdc(x, y));

    return 0;
}

int gdc(int x, int y)
{
    int r; // remainder

    if(y == 0){
        return x;
    }
    else{
        r = x % y;
        return gdc(y, r);
    }
}
