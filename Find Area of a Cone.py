#Python script to determine the area of a cone

radius=int(input("Enter Radius: "))
height=int(input("Enter height: "))
pi=22/7

area=pi*radius*(radius+((height**2)+(radius**2))**0.5)

print("Area is: ",area)
