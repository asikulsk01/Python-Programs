#Python script to check whether a user given number is Narcissistic number or not.
num = int(input("Enter any number for the testing: "))

#We save here the given number for a later reference
M = num
d=0
while(num > 0):
    d=d+1
    #Integer division
    num = num//10
    
string = ""
tot = 0
num = M
t = d
while(num > 0):
    r = num % 10
    tot = tot + r**d
    num = num // 10
    t = t-1

#The following 5 lines of code may be omitted by a novice programmer. It is to show: digits raised to the desired power sum up to give the given number
if(t != 0):
    #This is for concatenation
    string = string+str(r)+"**"+str(d)+"+ "

else:
    #This is also for concatenation without the plus sign for the last digit
    string = string+str(r)+"**"+str(d)
    
if(M==tot):
    print("\nIt is a Narcissistic Number")
    print("Because",M,"=",string)
    
else:
    print("\nIt is not a Narcissistic Number")
