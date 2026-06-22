#include<stdio.h>
#include<string.h>

int main(){

char logs[6][10]={"Success","Failed","Failed","Success","Failed","Success"};

int success=0,failed=0;

for(int i=0;i<6;i++){

if(strcmp(logs[i],"Success")==0)
success++;
else
failed++;

}

printf("Total Attempts: 6\n");
printf("Successful Logins: %d\n",success);
printf("Failed Logins: %d\n",failed);

printf("\nMonitoring failed logins helps detect suspicious login attempts and improves cybersecurity.\n");

return 0;
}