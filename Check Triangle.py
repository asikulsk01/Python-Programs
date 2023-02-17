#Python Script to categorize a triangle on the basis of its three given angles.
#The triangle may be in an 'invalid triangle', 'Equiangular', 'rightangle','acute angled' or 'obtuse angled'

angle1 = int(input("Enter First Angle: "))
angle2 = int(input("Enter Second Angle: "))
angle3 = int(input("Enter Third Angle: "))

angleSum = angle1 + angle2 + angle3

if(angleSum == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0):
    
    if(angle1 < 90 and angle2 < 90 and angle3 < 90):
        print("Triangle is: Acute-angled Triangle.")
        
    elif(angle1 == 90 or angle2 == 90 or angle3 == 90):
        print("Triangle is: Right-angled Triangle.")
        
    else:
        print("Triangle is: Obtuse-angled Triangle.")
else:
    print("\nTriangle is: Invalid.")
