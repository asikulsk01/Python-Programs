x = int(input("Enter the value of x: "))
n  =int(input("Enter the number of terms: "))

sum = x
m = -1

print("The values of the series: ")
print(x)

for i in range(1,n):
    u=1
    sum1=1
    pow=(2*i+1)

    for k in range(1,i+1):
        sum1=sum1*u
        u=u+2
        l=2
        sum2=1

        for j in range(1,i+1):
            sum2=sum2*l
            l=l+2

    term = (x ** pow)*sum1 / sum2

    print(term)

    sum += term * m
    m = m * -1

print("\nSum =", sum)
