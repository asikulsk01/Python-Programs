#Python script to find all the perfect numbers within 10000.
print("Printing all the perfect numbers upto 10000.")
print("--------------------------------------------")
for i in range(6,10001):
    tot=0
    for j in range(1,(i//2)+1):
        if(i%j==0):
            tot=tot+j
    if(i==tot):
        print(i)
