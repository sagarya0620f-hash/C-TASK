#include <stdio.h>

int main() {
    FILE *fp;
    char website[50];
    char username[100];
    char password[50];
    char ch;

    printf("Enter Website Name: ");
    scanf("%s", website);

    printf("Enter Username: ");
    scanf("%s", username);

    printf("Enter Password: ");
    scanf("%s", password);

    fp = fopen("vault.txt", "a");

    fprintf(fp, "Website: %s\n", website);
    fprintf(fp, "Username: %s\n", username);
    fprintf(fp, "Password: %s\n", password);
    fprintf(fp, "------------------------------\n");

    fclose(fp);

    printf("\nRecord Saved Successfully\n");

    printf("\nSaved Records:\n\n");

    fp = fopen("vault.txt", "r");

    while((ch = fgetc(fp)) != EOF) {
        printf("%c", ch);
    }

    fclose(fp);

    return 0;
}