tempe, prs, vol = input("Enter the temperature, Pressure and Volume of the gas at Standard temperature and pressure: ").split()

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
print("Volume of the gas at user given temperature and pressure",V2,"ml")
