#To compute the festival bonus of the employees on the basis of the basic pay and the designation.

basic = int(input("Basic Pay: "))
designation = str(input("Designation (manager/officer): "))

bonus=0
if designation.lower() == 'manager':
    if basic<40000:
        bonus=max((0.12*basic),2500)
    if basic>=40000:
        bonus=min((0.16*basic),7500)
        
elif designation.lower() == 'officer':
    if basic<20000:
        bonus=0.14*basic
        if bonus<2500:
            bonus=2500
        if bonus>5000:
            bonus=5000
    else:
        print('wrong input.')
else:
    bonus=0.089*basic
    
if bonus>0:
    print("The Festival Bonuse is:",bonus)
