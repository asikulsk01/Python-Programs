#Python program to prepare a grocery bill.

#Empty lists.
itemNames = []
qtys = []
itemPrices = []

#No of input.
ni = int(input("Please enter the number of item: "))

for i in range(0, ni):
    item = (input("Enter the item names: "))
    #itemNames.append(input("Enter the item names:"))
    qty = int(input("Enter the item Quantity: "))
    itemPrice = float(input("Enter the item price: "))
    
    #puting item one after another.
    itemNames.append(item)
    qtys.append(qty)
    itemPrices.append(itemPrice)


for i,j in itemNames,qtys:
    print("Name:",i,"\t\t\tQty:",j)

       
