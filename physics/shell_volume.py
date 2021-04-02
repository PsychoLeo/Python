from math import pi
def vol_shell(r1, r2):
    if r2 >= r1 :
        v_shell = 4*pi*((r2-r1)**3)/3
    else :
        v_shell = 4*pi*((r1-r2)**3)/3
    return v_shell