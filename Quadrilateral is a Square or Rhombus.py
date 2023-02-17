#To determine whether a quadrilateral is a square,rhombus on the basis of only
#the lengths of all the sides and one internal angle.

print("Input two adjoined sides and the diagonal of a parallelogram (comma separated):")
a,b,c = map(int, input().split(","))

if c**2 == a**2+b**2 :
    print("\nThis is a rectangle.")
    
if a == b:
    print("\nThis is a rhombus.")
