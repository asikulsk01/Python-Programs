#Python script to determine Sum of consecutive of odd numbers.
num=1
sum=0
count=0

while sum<=2000:
    sum = sum+num
    count = count+1
    num = num+2

print("Sum of consecutive of odd numbers: ",sum,"\nThe number of odd number added is: ",count,"\n")
