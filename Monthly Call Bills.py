#Determine the monthly call bill of a subscriber.

bill=75
calls=int(input("Numbers of Calls: "))

if calls>240:
    bill+=75*0.75+90*0.65+(calls-240)*0.55
elif calls>150 and calls<=240:
    bill+=75*0.75+(calls-150)*0.65
elif calls>75 and calls<=150:
    bill+=(calls-75)*0.75

print("\nMonthly Bill will be:",bill)
