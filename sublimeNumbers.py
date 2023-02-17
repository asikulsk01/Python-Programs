def perfect_no(a):
  sum = 0
  for i in range(1,a):
    if(a % i == 0):
      sum += i
  if(a == sum):
    return a

def sum_of_divisors(a):
  sum = 0
  for i in range(1,a+1):
    if(a % i == 0):
      sum += i
  return (sum)

def no_of_divisors(a):
  count = 0
  for i in range(1,a+1):
    if(a % i == 0):
      count = count + 1
  return(count)
      
a = int(input("Enter a number : "))

if(sum_of_divisors(a) == perfect_no(sum_of_divisors(a)) and no_of_divisors(a) == perfect_no(no_of_divisors(a)) ):
  print(a , " is Sublime Number")
else:
  print(a ,"is not Sublime Number")
