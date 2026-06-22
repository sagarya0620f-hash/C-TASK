#include<stdio.h>

int main(){

int num[10],i;
int largest,smallest,sum=0;
int even=0,odd=0;

printf("Enter 10 numbers:\n");

for(i=0;i<10;i++)
scanf("%d",&num[i]);

largest=smallest=num[0];

for(i=0;i<10;i++){

if(num[i]>largest)
largest=num[i];

if(num[i]<smallest)
smallest=num[i];

sum+=num[i];

if(num[i]%2==0)
even++;
else
odd++;

}

printf("\nLargest Number: %d",largest);
printf("\nSmallest Number: %d",smallest);
printf("\nSum: %d",sum);
printf("\nAverage: %.2f",(float)sum/10);
printf("\nEven Numbers: %d",even);
printf("\nOdd Numbers: %d",odd);

return 0;
}