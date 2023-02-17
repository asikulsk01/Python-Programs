#print the name of the starting day of any given year.

import datetime
year = int(input("Enter the year : "))

month = 1
day= datetime.datetime(year, month, 1)
print("\nThe starting day of",year,"is:",day.strftime('%A'))
