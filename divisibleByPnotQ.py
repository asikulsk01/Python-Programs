lower = int(input("Enter Lower Range limit: "))
upper = int(input("Enter Upper Range limit: "))
p = int(input("Enter the Value of p : "))
q = int(input("Enter the Value of q : "))
for i in range(lower, upper+1):
    if((i%p==0) & (i%q!=0)):
        print(i)
