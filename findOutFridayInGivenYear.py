from datetime import date

friday13 = 0
months = range(1,13)

year = int(input("Enter the year: "))

for month in months:
    if date(year, month, 13).weekday() == 4:
        friday13 +=1
        print(friday13)
