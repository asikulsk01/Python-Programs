#Find the divisor of a given number.
num=int(input("Enter any whole number"))
i=1

print("The divisors of the number: ",num,"are shown below:")
for i in range(1,(num//2)+1):
    if(num%i==0):
        print(i)
        
print(num)
