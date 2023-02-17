x = int(input("Enter the value of x: "))
n=int(input("Enter the number of terms: "))

sum = 0
m = 1

print("The values of the series: ")

for i in range(1,n+1) :
    pow=(2*i)
    term =(x ** pow) / pow
    print(term)
    sum += term * m
    m = m * -1

print("\nSum =", sum)
