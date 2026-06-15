#include <stdio.h>

int main() {

    char first[50];
    char last[50];
    int year;

    printf("Enter First Name: ");
    scanf("%s", first);

    printf("Enter Last Name: ");
    scanf("%s", last);

    printf("Enter Birth Year: ");
    scanf("%d", &year);

    printf("\nUsername Suggestions:\n");

    printf("%s%s%d\n", first, last, year);
    printf("%c.%s%d\n", first[0], last, year % 100);
    printf("%s_%s\n", last, first);
    printf("%s%d\n", first, year);
    printf("%s%d\n", last, year);

    return 0;
}