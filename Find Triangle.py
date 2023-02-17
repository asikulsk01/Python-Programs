#check whether the given lengths can be valid lengths of three sides of a triangle and
#to categorize the triangle as ‘Equilateral’ or ‘Isosceles’ or ‘Scalene’ one.

print("Input lengths of the triangle sides. ")
x,y,z = int(input("Enter X: ")),int(input("Enter Y: ")),int(input("Enter Z: "))

if x == y == z:
    print("\nThis is an Equilateral triangle.")
    
elif x==y or y==z or z==x:
    print("\nThis is an Isosceles triangle.")
    
else:
    print("\nThis is a Scalene triangle.")

