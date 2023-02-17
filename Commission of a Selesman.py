#Python script to calculate commission of a salesman.

sales=int(input("Enter the sales: "))

print("\nCommission of Region A || Commission of Region B")

print("\n\t","NIL" if sales<10000 else (sales*(65/100)) if sales<16000 else (sales*(85/100))+1500 if sales>=16000 and sales<35000 else (sales*(11/100))+4500,end="\t\t")
print("NIL" if sales<10000 else (sales*(65/100)) if sales<15000 else (sales*(85/100))+1500 if sales>=15000 and sales<25000 else (sales*(11/100))+4500)
