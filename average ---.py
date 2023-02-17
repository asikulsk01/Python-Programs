def avg_num(num1, num2):   #user-defined function
    avg = (num1 + num2) / 2   #calculate average
    return avg    #return value

# take inputs
num1 = float(input('Enter First number: '))
num2 = float(input('Enter Second number: '))

# function call
average = avg_num(num1, num2)

# display result
print('The Average of Numbers = %0.2f' %average)
