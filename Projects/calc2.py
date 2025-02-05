from sympy import sqrt, pi
from calc import *

diameter_symbol = '\u2300'

Qu = int(input("Please input the Qu in Kn.m: ")) * 10**3  # Convert Kn.m to N.mm
qu = Qu/(b*d)
qu_max = 0.7 * sqrt(Fcu/FS_Concrete)
qu_uncracked = 0.16 * sqrt(Fcu/FS_Concrete)
qu_cracked = 0.12 * sqrt(Fcu/FS_Concrete)

if qu<qu_uncracked:
    print(f'Use min stirrups 5{diameter_symbol}8')
    exit()
elif qu>qu_max:
    print(f'Increase dimensions of cross-section due to shear: {qu} > {qu_max}')
    exit()
elif qu_uncracked < qu < qu_max :
    qsu= qu-qu_cracked
s = symbols('s')
Fy=240
Astr = pi/4 * 8**2
eq_shear = Eq(qsu, (2*Astr*Fy/FS_Steel)/(b*s) )
s_solution = solve(eq_shear, s)
s_value = s_solution[0]
if s_value>200:
    print(f'Use minimum stirrups 5{diameter_symbol}8')
elif 100<s_value<200:
    S_per_meter = round(1000/s_value)
    print(f'Use stirrups {S_per_meter}{diameter_symbol}8')
elif s_value<100:
    Astr = pi / 4 * 10 ** 2
    Fy=350
    eq_shear = Eq(qsu, (2 * Astr * Fy / FS_Steel) / (b * s))
    s_solution = solve(eq_shear, s)
    s_value = s_solution[0]
    if s_value > 200:
        print(f'Use maximum spacing 5{diameter_symbol}10')
    elif 100 < s_value < 200:
        S_per_meter = round(1000 / s_value)
        print(f'Use stirrups {S_per_meter}{diameter_symbol}10')
    elif s_value<100:
        Astr = pi / 4 * 10 ** 2
        Fy=350
        eq_shear = Eq(qsu, (4 * Astr * Fy / FS_Steel) / (b * s))
        s_solution = solve(eq_shear, s)
        s_value = s_solution[0]
    elif s_value > 200:
        print(f'Use maximum spacing 5{diameter_symbol}10')
    elif 100 < s_value < 200:
        S_per_meter = round(1000 / s_value)
        print(f'Use stirrups {S_per_meter}{diameter_symbol}10')
exit()