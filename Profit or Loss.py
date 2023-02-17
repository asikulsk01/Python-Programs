#Determine Profit and Loss.
actualPrice = int(input("Enter Actual Price of the Product: "))
sellingPrice = int(input("Enter Selling Price of the Product: "))

pl = sellingPrice-actualPrice

if pl > 0:
    print("\nThe profit on sell: ",pl)
    
else:
    print("\nThe loss on sell: ",pl)
