x = int(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))

sum = 0
m = 1

print("The values of the series: ")
for i in range(1,n+1) :
    fact=1
    pow=(2*i)

    for j in range(1, pow+1) :
        fact *= j

    term = x ** pow / fact

    print(term)

    sum += term * m
    m = m * -1

print("\nSum =", sum)
