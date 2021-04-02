from math import sqrt
from random import random
import matplotlib.pyplot as plt

##############################
### Simple Vector plotting ###
##############################

class SimpleVectorPlotting:

    def __init__(self):
        self.vectors = []
        self.functions = []
        self.colors = {'b', 'g', 'r', 'c', 'm', 'y', 'k'}

    def addFunctions(self, functions):
        for func in functions:
            self.functions.append(func)
        return None

    def addVectors(self, vectors):
        for vec in vectors:
            self.vectors.append(vec)
        return None

    def plot(self):
        x_coords, y_coords = [vec.Ax + vec.x for vec in self.vectors], [vec.Ay + vec.y for vec in self.vectors]
        plt.xlim(min(x_coords) - 1, max(x_coords) + 1)
        plt.ylim(min(y_coords) - 1, max(y_coords) + 1)
        for vector in self.vectors:
            plt.quiver(vector.Ax, vector.Ay, vector.x, vector.y, color=self.colors.pop(), label=vector.coords,
                       angles='xy', scale_units='xy', scale=1)
        plt.legend(loc='upper left')
        plt.show()


class SimpleVector:

    def __init__(self, x, y, Ax=0, Ay=0):
        self.x = x
        self.y = y
        self.Ax = Ax
        self.Ay = Ay

    @property
    def coords(self):
        return (self.x, self.y)

    def __add__(self, other):
        return SimpleVector(self.x + other.x, self.y + other.y, self.Ax, self.Ay)

    def __sub__(self, other):
        return SimpleVector(self.x - other.x, self.y - other.y, self.Ax, self.Ay)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'SimpleVector({self.x}, {self.y}, {self.Ax}, {self.Ay})'


# if __name__ == '__main__' :
#     var = sympy.Symbol(input('Enter the name of your variable (x/t/n...) : '))
#     func = sympy.sympify(input(f'Enter your function \nf({var}) = '))

# system = System(func, var)

def applyForces(forces):
    '''input : forces acting on the system (equations)
    output : None [forces are appendend to System.forces]'''
    result = {}
    for force in forces:
        result[force] = None
    return result


def derivee(fonction, variable):
    '''input : a function NOT as a string such as 'x**2-2*x+3'
    output : the derivative form of this function'''
    return fonction.diff(variable)


def rd_color():
    return (random(), random(), random())


### Tests ###
grid = SimpleVectorPlotting()
v1, v2, v3, v4 = SimpleVector(1, 3), SimpleVector(-1, 4), SimpleVector(-4, 0), SimpleVector(3, -4)
grid.addVectors([v1, v2, v3, v4])
grid.plot()