#Python script to check whether a given year is leap year or not using ternary operator.

year  = int(input("Enter any year: "))

print("\n")
print(year,"is a leap year.") if(year%400==0 or (year%4==0)  and  (year%100!=0) ) else print(year,"is a not leap year.")
