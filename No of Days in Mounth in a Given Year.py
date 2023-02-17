#Python Script to print the number of days in each month of a given year.

year = int(input("Enter a year: "))

if((year%400==0) or ((year%100!=0) and (year%4==0))):

    print("\nJanuary: 31 Days.\nFebruary: 29 Days.\nMarch: 31 Days.\nApril: 30 Days.\nMay: 31 Days.\nJune: 30 Days.\nJuly: 31 Days.\nAugust: 31 Days.\nSeptember: 30 Days.\nOctober: 31 Days.\nNovember: 30 Days.\nDecember: 31 Days.")

else:
    print("\nJanuary: 31 Days.\nFebruary: 28 Days.\nMarch: 31 Days.\nApril: 30 Days.\nMay: 31 Days.\nJune: 30 Days.\nJuly: 31 Days.\nAugust: 31 Days.\nSeptember: 30 Days.\nOctober: 31 Days.\nNovember: 30 Days.\nDecember: 31 Days.")
