#Sum of Nth naturan number.
num=int(input("Enter any integer number: "))
i=0
sum=0

while(i<=num):
    sum=sum+i
    i=i+1

print("\nSum of first",num,"natural number is:",sum)
