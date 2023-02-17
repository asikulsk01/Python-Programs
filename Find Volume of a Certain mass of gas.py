#Python Script to to determine the volume a certain mass of gas at a given temperature and pressure when the volume is known at the normal pressure and at the absolute temperature.
tempe = input("Enter the Temperature of the gas at Standard temperature and pressure: ")
prs = input("Enter the Pressure of the gas at Standard temperature and pressure: ")
vol = input("Enter the Volume of the gas at Standard temperature and pressure: ")

T1 = 273
T2 = float(tempe)
#mm
P1 = 760
#mm
P2 = float(prs)
#Volume of thegas at Standard temperature and pressure in ml.
V1 = float(vol)
#Convert it kelvin.
T2 = T2+273

V2 = (P1*V1*T2)/(P2*T1)
print("Volume of the gas at user given temperature and pressure: ",V2,"ml")
