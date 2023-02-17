#Python to determine to determine the net salary of an employee when it is known that the employee is eligible to
#dearness allowance (DA) of 97% of the basic pay, House Rent Allowance (HRA) of 57% of the basic pay and
#medical allowance e of Rs.150 .
#It is further known that 12% of the basic pay is deducted from the gross salary for the Employees’ Provident fund (EPF)
#and Rs. 200 is deducted from the gross pay as the professional tax.

#Taking basic pay frome the user.
basic = eval(input("Enter the basic pay of the respective customer: "))

#DA 97% of the basic pay,HRA 57%, and Medical Allowanc of Rs:150.
da = (0.97 * basic)
hra = (0.57 * basic)
med = 150

#Calculating Gross Income.
gross = basic+da+hra+med

#12%EPF of basic pay and Professional tax of Rs:200 is deducted.
deduction = (0.12 * basic)
ptax = 200

#Calculating net Income.
net = gross-deduction-ptax

print("Net pay of the Employee is: ",net)
