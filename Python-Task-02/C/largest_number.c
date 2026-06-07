#include <stdio.h>

int main() {
    float num1, num2, num3, largest;

    printf("Enter first number: ");
    scanf("%f", &num1);

    printf("Enter second number: ");
    scanf("%f", &num2);

    printf("Enter third number: ");
    scanf("%f", &num3);

    largest = num1;

    if (num2 > largest)
        largest = num2;

    if (num3 > largest)
        largest = num3;

    printf("Largest Number = %.2f\n", largest);

    return 0;
}