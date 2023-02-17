#Python script to determine the stock value of a store of certain item on the basis of its unit cost and quantities held in the stock.

stockQty=eval(input("Enter the Quantities held in the stock: "))
pUniteCost=eval(input("Enter the per Unit Cost: "))

stockValue=stockQty*pUniteCost

print("Stock value of a store is: ",stockValue)
