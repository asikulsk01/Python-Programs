#To print a currency conversion table from Pounds, Dollar, Euro to equivalent Indian Rupees.

currency = str(input("Choose a currency between Pound,Dollar and Euro: "))
val = eval(input("\nEnter the value of that following currency :"))

rupee = 0
if currency == "Pound":
    rupee= val*99.49
elif currency == "Dollar":
    rupee = val*75.48
elif currency == "Euro":
    rupee = val*83.76
else:
    print("\nInvalid Currency.")
    
print("\nRs Price is:",rupee)
