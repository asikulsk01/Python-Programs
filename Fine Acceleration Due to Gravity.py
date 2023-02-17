#Python script to to determine to determine the acceleration due to gravity on the basic of the effective length of simple pendulum.

time = eval(input("Enter the time Period: "))

length = eval(input("Enter the effective of the Pendulum: "))

pi=3.14

gravity = 4*pi**2*(length/(time*time))

print("The Acceleration Due to Gravity in a Region is: ",round(gravity,2), "sq unit")
