import math
n = int(input("Enter the number:"))
sq = n*n
temp=n
sum=0
a=0
b=0
c=1

while temp !=0:
    c=c*10
    temp=int(temp/10)
    a=sq%c
    b=int(sq/c)
    sum=a+b
    print(n)
    if sum==n:
        print("%d is a kaprekar number" %(n))
    else:
        print("%d is not a kaprekar number" %(n))