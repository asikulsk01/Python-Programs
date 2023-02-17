#Python script to determine the simple interest on a given amount of money at a given rate of interest for a given period of time.

amount=float(input("Enter the amount: "))
rate=float(input("Enter the rate of interest: "))
p=int(input("Enter the period: "))
          
interest=0
          
for i in range(p):
    interest=interest+(amount*(rate/100))
    amount=amount-(amount*(rate/100))
          
print("Interest is: ",interest)
