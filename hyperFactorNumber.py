num = int(input("Enter a number to get hyper-factorial number: "))
val = 1
for i in range(1, num + 1):
    val = val * pow(i, i)

print(val)
