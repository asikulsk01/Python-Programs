#Python script to obtain the reversed of a given number.
num=eval(input("Enter a number:"))
rn = 0
n=0

while (num>0):
    rem = num%10
    rn = rn*10+rem
    #Used double slash to obtain the integer quotient of the number.
    num = num//10

print("The reverse no is:",rn)
