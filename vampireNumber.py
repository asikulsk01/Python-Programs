p=int(input("Enter number test for vampire: "))

def nd(a):
    nd = 0
    while a != 0:
        d = a % 10
        if d != 0:
            nd += 1
        a = a // 10
        return nd
def DigitosPer(a):
    if nd(a)%2==0:
        return 1
    else:
        return 0
#Last digit is 0
def UltimoDigCaro(b):
    ud = 0
    ud = b % 10
    if ud==0:
        return 1
    else:
        return 0
if DigitosPer(p)==1:
    x=[]
    for i in range(int(10*(nd(p)/2-1)),int(10*(int(nd(p))/2))):
        x.append(i)
    y=x
    z=0
    posiblex=0
    posibley=0
    for ia in range(0,len(y)):
        for ib in range(0,len(x)):
            z=y[ia]*x[ib]
            if z==p and not((UltimoDigCero(x[ib])==1 and UltimoDigCero(y[ia])==1)):
                posiblex=x[ib]
                posibley=y[ia]
                print(p,"has as fangs",posiblex,posibley)
    if posiblex==0:
       print(p," a vampire Number")
else:
    print(p,"not a vampire Number")
