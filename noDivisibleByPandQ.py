#Python script to obtain the divisor of given number.
p=int(input("Enter p: "))
q=int(input("Enter q: "))
i=0
print("All the whole number that are divisible by p:",p)
for i in range(50):
    if(i%p==0):
        print(i)
print("All the whole number that are not divisible by q:",q)        
for i in range(50):
    if(i%p!=0):
        print(i)

