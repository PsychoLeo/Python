from sympy import FiniteSet, pi


def time_period(length):
    '''input : the length of the pendulum's string
    output : the time that the pendulum takes (s) to do one oscillation'''
    return 2 * pi * ((length / 9.81)**.5)


'''if __name__ == '__main__':
    len_vals = FiniteSet(15, 18, 21, 22.5, 25)
    for i in len_vals:
        print('Length : {0} cm || Time period : {1:.3f} s' . format(float(i), float(time_period(i / 100))))'''


# adding a new variable : gravitational force,
# depending on where you stand on earth / on the moon
def oscil_period(L, g):
    return 2 * pi * ((L / g)**.5)


if __name__ == '__main__':
    len_vals = FiniteSet(2, 5, 10, 14, 18, 20, 30, 50)
    g_vals = FiniteSet(1.6, 9.81, 9.78, 9.83)
    for i in len_vals * g_vals:
        L = i[0]
        g = i[1]
        print('Length : {0} || Gravitational force : {1} || Oscillation period : {2:.3f}' .format(float(L), float(g), float(oscil_period(L, g))))
