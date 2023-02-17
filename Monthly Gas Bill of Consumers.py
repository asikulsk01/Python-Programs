#Python to determine the monthly gas bill of the consumers.

gas=float(input('Enter Gas Consumed in Cubic Feet: '))

therms=gas*1.475
pay=0
if therms<=125:
    pay=therms*7.75
    
elif therms>125 and therms<=250:
    pay=therms*9.75+(0.0125*therms*9.75)
    
elif therms>250:
    pay=therms*13+(0.025*therms*13)
    
print("\nMonthly Gas Bill of The Consumers is:",pay+25)
