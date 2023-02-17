#Python script to find the number of digit present in a given number.
num=eval(input("Enter a number:"))
cnt=0
rem=0

while (num>0):
    rem = num%10
    cnt=cnt+1
    #Used double slash to obtain the integer quotient of the number.
    num = num//10

print("Number of digit:",cnt)
