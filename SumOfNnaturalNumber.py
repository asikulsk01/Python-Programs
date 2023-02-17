#Sum of N-th  natural number without using formula.
num=int(input("Enter any Integer Number: "))
i=0
sum=0

while(i<=num):
    sum=sum+i
    i=i+1

print("\nSum of First",num,"Natural Number is: ",sum)
