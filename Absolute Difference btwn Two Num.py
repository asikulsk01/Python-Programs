#Determine the absolute difference between a given number.
num = eval(input("Enter the number: "))

constNum = 123

if(num>constNum):
    diff = (num-constNum)*3
else:
    diff = (constNum-num)

print("Absolute diffrence between",num,"and",constNum,"is:",diff)
