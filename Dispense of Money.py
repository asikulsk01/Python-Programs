#Develop a Python script to determine the minimum number of 100,200,500 and 2000 rupee note required to dispense a given sum of money.

import sys
actual_money=int(input("Enter the amount of Money you want to be dispensed: "))

money=actual_money;

if (money%100 != 0):
    print("Please enter a amount that is perfectly divisable by 100!")
    sys.exit();
    
else:
    txt="To dispense {} unit of money you get :"
    print(txt.format(money),end="")
    while money!=0:
        if money>=2000:
            two=money//2000;
            money=money-(two*2000);
            if two>1:
                txt=" {} 2000 Notes,"
                print(txt.format(two),end="")
            else:
                txt=" {} 2000 Note,"
                print(txt.format(two),end="")
                
        elif money>=500:
            five=money//500;
            money=money-(five*500);
            if five>1:
                txt=" {} 500 Notes,"
                print(txt.format(five),end="")
            else:
                txt=" {} 500 Note,"
                print(txt.format(five),end="")
                
        elif money>=100:
            one=money//100;
            if one>1:
                txt=" {} 100 Notes."
                print(txt.format(one),end="")
            else:
                txt=" {} 100 Note,"
                print(txt.format(one),end="")
                
            money=money-(money*one);
