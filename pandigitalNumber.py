def is_pandigital_num(n):
    return len(set(str(n))) == 10

n=int(input("Enter the number to test: "))
if (is_pandigital_num(n)):
    print(n,"is pandigital.")
else:
    print(n,"is not pandigital.")

