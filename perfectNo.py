#Check whether a number is perfect or not.
num = int(input("Enter any whole number: "))

i=1
sum=0
for i in range(1,(num//2)+1):
    if(num%i==0):
        sum=sum+i

if(num==sum):
    print("\nGiven number is a perfect number.")
else:  
    print("\nGiven number is not a perfect number.")
