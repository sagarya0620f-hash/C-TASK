#include <stdio.h>

void displayStudent(char name[], int roll, char branch[], int semester) {
    printf("\nStudent Information\n");
    printf("Name: %s\n", name);
    printf("Roll No: %d\n", roll);
    printf("Branch: %s\n", branch);
    printf("Semester: %d\n", semester);
}

int main() {
    char name[50];
    char branch[20];
    int roll;
    int semester;

    printf("Enter Name: ");
    scanf(" %[^\n]", name);

    printf("Enter Roll Number: ");
    scanf("%d", &roll);

    printf("Enter Branch: ");
    scanf("%s", branch);

    printf("Enter Semester: ");
    scanf("%d", &semester);

    displayStudent(name, roll, branch, semester);

    return 0;
}