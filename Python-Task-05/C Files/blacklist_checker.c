#include<stdio.h>
#include<string.h>

int main(){

char blacklist[4][20]={
"192.168.1.10",
"10.0.0.5",
"172.16.1.100",
"192.168.0.50"
};

char ip[20];
int found=0;

printf("Enter IP Address: ");
scanf("%s",ip);

for(int i=0;i<4;i++){

if(strcmp(ip,blacklist[i])==0){
found=1;
break;
}

}

if(found)
printf("IP Found in Blacklist");
else
printf("IP Not Found");

return 0;
}