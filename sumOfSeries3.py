x = int(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

sum = x
m = -1

print("The values of the series: ")
print(x)

for i in range(1,n) :
    fact=1
    pow=(2*i+1)

    for j in range(1, pow+1) :
        fact *= j

    term = x ** pow / fact

    print(term)

    sum += term * m
    m = m * -1

print("\nSum =", sum)
