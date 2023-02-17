def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

start = 2
end = 10000

for i in range(start, end):
    j = i + 2
    if(is_prime(i) and is_prime(j)):
        print("{:d} and {:d}".format(i, j))


