#include <stdio.h>

int main() {
    int marks[5], i;
    int highest, lowest, sum = 0;

    printf("Enter marks of 5 students:\n");

    for(i=0;i<5;i++){
        scanf("%d",&marks[i]);
    }

    highest = lowest = marks[0];

    for(i=0;i<5;i++){
        if(marks[i]>highest)
            highest=marks[i];

        if(marks[i]<lowest)
            lowest=marks[i];

        sum += marks[i];
    }

    printf("\nHighest Marks: %d",highest);
    printf("\nLowest Marks: %d",lowest);
    printf("\nAverage Marks: %.2f",(float)sum/5);

    return 0;
}