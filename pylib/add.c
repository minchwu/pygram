#include <stdio.h>

double add(double x, double y)
{
    return (x + y);
}

int main()
{
    double sum = add(1, 2);
    printf("%f", sum);
    return 0;
}