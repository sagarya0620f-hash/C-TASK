#include <stdio.h>
#include <string.h>

int main() {
    char username[50];
    char password[50];

    printf("Enter username: ");
    scanf("%s", username);

    printf("Enter password: ");
    scanf("%s", password);

    if (strcmp(username, "admin") == 0 &&
        strcmp(password, "password123") == 0)
    {
        printf("Login Successful\n");
    }
    else
    {
        printf("Invalid Credentials\n");
    }

    return 0;
}