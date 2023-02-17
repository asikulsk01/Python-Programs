from sys import stdout
def factors(n):
    rt = []
    f = 2
    if n == 1:
        rt.append(1)
    else:
        while 1:
            if 0 == ( n % f ):
                rt.append(f)
                n//= f
                if n == 1:
                    return rt
            else:
                f += 1
    return rt

def sum_digits(n):
    sum = 0
    while n > 0:
        m = n % 10
        sum += m
        n -= m
        n//= 10
    return sum
 
def add_all_digits(lst):
    sum = 0
    for i in range (len(lst)):
        sum += sum_digits(lst[i])
 
    return sum
 
abc = int(input("Enter from where to Search the Smith No : "))
cnt = int(input("Enter where to Stop : "))
def list_smith_numbers(abc,cnt):
    for i in range(abc , cnt):
        fac = factors(i)
        if len(fac) > 1:
            if sum_digits(i) == add_all_digits(fac):
                print("{0} ".format(i) )
 
# entry point
print(list_smith_numbers(abc,cnt+1))


