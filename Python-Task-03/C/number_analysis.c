#include <stdio.h>

int main() {
    int n;
    int sum = 0;
    int even = 0;
    int odd = 0;

    printf("Enter a number: ");
    scanf("%d", &n);

    for(int i = 1; i <= n; i++) {
        sum += i;

        if(i % 2 == 0)
            even++;
        else
            odd++;
    }

    printf("Sum = %d\n", sum);
    printf("Even Numbers = %d\n", even);
    printf("Odd Numbers = %d\n", odd);

    return 0;
}