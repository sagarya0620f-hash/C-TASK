#include <stdio.h>
#include <string.h>

struct Student {
    int id;
    char name[30], branch[20], email[40];
};

struct Student s[100];
int count = 0;
int scores[100], scoreCount = 0;

void addStudent() {
    printf("Student ID: ");
    scanf("%d", &s[count].id);
    printf("Name: ");
    scanf(" %[^\n]", s[count].name);
    printf("Branch: ");
    scanf("%s", s[count].branch);
    printf("Email: ");
    scanf("%s", s[count].email);
    count++;
    printf("Student Added Successfully!\n\n");
}

void viewStudents() {
    if (count == 0) {
        printf("No Records Found.\n\n");
        return;
    }

    for (int i = 0; i < count; i++) {
        printf("\nID: %d\n", s[i].id);
        printf("Name: %s\n", s[i].name);
        printf("Branch: %s\n", s[i].branch);
        printf("Email: %s\n", s[i].email);
    }
    printf("\n");
}

void searchStudent() {
    int id, found = 0;
    printf("Enter Student ID: ");
    scanf("%d", &id);

    for (int i = 0; i < count; i++) {
        if (s[i].id == id) {
            printf("\nRecord Found\n");
            printf("ID: %d\nName: %s\nBranch: %s\nEmail: %s\n\n",
                   s[i].id, s[i].name, s[i].branch, s[i].email);
            found = 1;
        }
    }

    if (!found)
        printf("Record Not Found\n\n");
}

void deleteStudent() {
    int id, found = 0;
    printf("Enter Student ID: ");
    scanf("%d", &id);

    for (int i = 0; i < count; i++) {
        if (s[i].id == id) {
            for (int j = i; j < count - 1; j++)
                s[j] = s[j + 1];
            count--;
            found = 1;
            break;
        }
    }

    if (found)
        printf("Student Deleted Successfully.\n\n");
    else
        printf("Record Not Found.\n\n");
}

void securityAssessment() {
    char mfa, update, antivirus;
    int pass, score = 0;

    printf("Is MFA Enabled? (y/n): ");
    scanf(" %c", &mfa);

    printf("Password Length: ");
    scanf("%d", &pass);

    printf("System Updated? (y/n): ");
    scanf(" %c", &update);

    printf("Antivirus Installed? (y/n): ");
    scanf(" %c", &antivirus);

    if (mfa == 'y' || mfa == 'Y') score += 25;
    if (pass >= 8) score += 25;
    if (update == 'y' || update == 'Y') score += 25;
    if (antivirus == 'y' || antivirus == 'Y') score += 25;

    scores[scoreCount++] = score;

    printf("\nSecurity Score: %d/100\n", score);

    if (score >= 90)
        printf("Status: Excellent\n\n");
    else if (score >= 70)
        printf("Status: Good\n\n");
    else if (score >= 50)
        printf("Status: Moderate\n\n");
    else
        printf("Status: Poor\n\n");
}

void generateReport() {
    int total = 0, poor = 0;

    for (int i = 0; i < scoreCount; i++) {
        total += scores[i];
        if (scores[i] < 50)
            poor++;
    }

    printf("\n===== REPORT =====\n");
    printf("Total Students: %d\n", count);
    printf("Average Security Score: %.2f\n",
           scoreCount ? (float) total / scoreCount : 0);
    printf("Students with Poor Rating: %d\n", poor);
    printf("==================\n\n");
}

int main() {
    int choice;

    do {
        printf("=================================\n");
        printf(" Student Security Manager\n");
        printf("=================================\n");
        printf("1. Add Student\n");
        printf("2. View Students\n");
        printf("3. Search Student\n");
        printf("4. Delete Student\n");
        printf("5. Security Assessment\n");
        printf("6. Generate Report\n");
        printf("7. Exit\n");
        printf("Enter Choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: addStudent(); break;
            case 2: viewStudents(); break;
            case 3: searchStudent(); break;
            case 4: deleteStudent(); break;
            case 5: securityAssessment(); break;
            case 6: generateReport(); break;
            case 7: printf("Thank You!\n"); break;
            default: printf("Invalid Choice!\n\n");
        }

    } while (choice != 7);

    return 0;
}