numbers=[]

print("Enter 10 numbers:")

for i in range(10):
    numbers.append(int(input()))

largest=max(numbers)
smallest=min(numbers)
total=sum(numbers)
average=total/10

even=0
odd=0

for num in numbers:
    if num%2==0:
        even+=1
    else:
        odd+=1

print("\nLargest:",largest)
print("Smallest:",smallest)
print("Sum:",total)
print("Average:",average)
print("Even Numbers:",even)
print("Odd Numbers:",odd)