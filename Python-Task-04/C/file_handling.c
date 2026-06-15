#include <stdio.h>

int main() {
    FILE *fp;
    char name[50];
    int roll;
    char branch[20];
    int marks;
    char ch;

    printf("Enter Name: ");
    scanf(" %[^\n]", name);

    printf("Enter Roll No: ");
    scanf("%d", &roll);

    printf("Enter Branch: ");
    scanf("%s", branch);

    printf("Enter Marks: ");
    scanf("%d", &marks);

    fp = fopen("student_data.txt", "w");

    fprintf(fp, "Name: %s\n", name);
    fprintf(fp, "Roll No: %d\n", roll);
    fprintf(fp, "Branch: %s\n", branch);
    fprintf(fp, "Marks: %d\n", marks);

    fclose(fp);

    printf("\nStudent Record Saved Successfully\n");

    printf("\nReading File...\n\n");

    fp = fopen("student_data.txt", "r");

    while((ch = fgetc(fp)) != EOF) {
        printf("%c", ch);
    }

    fclose(fp);

    return 0;
}