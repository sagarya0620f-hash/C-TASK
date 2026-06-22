#include <stdio.h>
#include <string.h>

int main() {

    char employees[5][20]={"John","Alice","David","Sophia","Michael"};
    char name[20];
    int found=0;

    printf("Enter employee name: ");
    scanf("%s",name);

    for(int i=0;i<5;i++){

        if(strcmp(name,employees[i])==0){
            found=1;
            break;
        }

    }

    if(found)
        printf("Record Found");
    else
        printf("Record Not Found");

    return 0;
}