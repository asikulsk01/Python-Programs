#Python script to calculate the parking charge for the users of the area.

hrs=float(input("Parking Hours: "))
pay=0
if hrs<=8.5:
    pay=hrs*55
    
if hrs>8.5 and hrs<=23:
    pay=8.5*55+((hrs-8.5)/2)*13.75
    
if hrs>23:
    pay=8.5*55+(14.5/2)*13.75+((hrs-23)*60*5.50)
    
print("Parking Charge: ",pay)
