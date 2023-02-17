import math

a = int(input("Enter lower Range : "))
b = int(input("Enter upper Range : "))

def checkPronic (x) :
    i = 0
    while ( i <= (int)(math.sqrt(x)) ) :
        if ( x == i * (i + 1)) :
            return True
        
        i = i + 1
        
    return False

print("\nOblong number between",a,"and",b)
for i in range(a,b+1):
  if(checkPronic(i) == True):
    print(i)


    
