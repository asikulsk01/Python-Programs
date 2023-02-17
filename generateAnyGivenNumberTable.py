#Python script to generate table of any given number.
num = int(input("Enter any Number: "))
tbl=0

print("\nBelow is the Table for ",num)
for i in range(1,11):
    tbl=num*i
    print("",num,"*",i,"=",tbl)
