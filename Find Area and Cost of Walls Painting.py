#Python script to determine the area of the walls of a rectangular room and hence the cost of its painting on the basis of charge per square unit.

length=eval(input("Enter length of the wall: "))
width=eval(input("Enter width of the wall: "))
charge=eval(input("Enter charge for per square unit: "))

area=length*width
cost=(area/4)*charge

print("Area of the wall is: ",area,"\nCost of painting Rs: ",cost)
