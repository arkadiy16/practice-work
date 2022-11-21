# Module for power line transmission calculation.

import tkinter


# We know: U(phase)=const; I2; Z12; b12.
# Need to find: U1; I12; power losses s12_l; I1.
def calculate(u2, i2, z12, b12):
    # Calculate capacity current in the end of the line.
    ic12_e = u2 * complex(0, b12) / 2
    # Current in line 12.
    i12 = i2 + ic12_e
    # Voltage in start.
    u1 = u2 + i12 * z12
    # Capacity current in start.
    ic12_s = u1 * complex(0, b12) / 2
    # Power losses in line (3 phases).
    s12_l = 3 * i12 ** 2 * z12
    return ic12_e, i12, u1, ic12_s, s12_l

def gui():
    pass

#print(calculate(5890, complex(25, 11), complex(6.23, 2.93), 1))
a = b = d = 1
print(a, b, d)