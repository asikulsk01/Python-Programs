#Python script to calculate the EMI of a loan amount.

p = eval(input("Enter the principal loan amount: "))
r = float(input("Enter the rate of interest: "))
n = eval(input("Enter the duration: "))

#Monthly rate of intrest over each rupee.
r = r/1200
#Convert the term in years into the equivalent term in months.
n = n*12

e = p*r*(((1+r)**n)/((1+r)**n-1))

print("The EMI will be Rs: ",e)
