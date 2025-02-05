from sympy import symbols, Eq, solve, pi
import math
# Defining main symbols and inputs
a = symbols('a')
Mu = int(input("Please input the Mu in Kn.m: ")) * 10**6  # Convert Kn.m to N.mm
Fcu = int(input("Please input the Fcu in n/mm2: "))
Fy = int(input("Please input the Fy in n/mm2: "))
b = int(input("Please input the b in mm: "))
t = int(input("Please input the t in mm: "))
d = t - 50
FS_Steel = 1.15
FS_Concrete = 1.5

# Define the equation
eq = Eq(Mu, 0.45 * Fcu * a * b * (d - a / 2))

# Solve for 'a'
a_solution = solve(eq, a)

# Choose the lower value of 'a'
a_min = min(a_solution)
if a_min <= 0.1*d:
    a_min = 0.1*d
else:
    a_min = a_min

# Checking for safety of compression ratio
c = a_min/0.8
c_max_ratio = 0.44
if (c/d) >= c_max_ratio:
    print(f'Please change the dimensions of the cross-section; c/d ={c/d}')
    exit()
else:
    print(f'c/d is equal to {c/d} which is less than the (c/d)max and you can design ')

# Calculation of As in mm2
As = Mu * FS_Steel / (Fy * (d - a_min / 2)) #Mu=(As*Fy/Factor_Safety_Steel)*(d-a/2)
As_prime = 0.15*As
print(f'The main reinforcement should be {As} mm2 and the secondary should be {As_prime} mm2')

