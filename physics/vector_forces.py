import matplotlib.pyplot as plt
from math import sqrt, pi, sin, cos
from time import sleep

dt = 0.05 # time interval (in seconds)
g = 9.807 # standard gravity
scale = 1/10 # scale for vector plotting
drag_coef = 0.45 # system ~= sphere
air_density = 1.292 # air density (km.m^-3)
visc_air = 18.5*10**(-6) # viscosité de l'air

###############################
### Complex Vector plotting ###
###############################

class System:

    def __init__(self, mass, radius=None, milieu='air', x0=0, y0=0, v0=10, alpha=60):
        self.mass = mass
        self.radius = radius
        self.x = x0
        self.y = y0
        self.vx = v0 * cos(alpha) * pi/180
        self.vy = v0 * sin(alpha) * pi/180
        self.milieu = milieu
        self.xcords = [x0]
        self.ycords = [y0]
        self.colors = {'b', 'g', 'r', 'c', 'm', 'y', 'k'}

    def drawVectors(self, friction=False) :
        '''input : None
        output : None --> vectors are plotted'''
        global g
        gravityVec = Vector(2, (self.x, self.y), (0, self.mass*g))
        frictionVec = Vector(2, (self.x, self.y), (-self.vx, -self.vy))
        if friction :
            plotted = (gravityVec, frictionVec)
        else :
            plotted = (gravityVec)
        for vec in plotted :
            plt.quiver (vec.Ax, vec.Ay, vec.x, vec.y, self.colors.pop(), label=vec.vec_coords,
                       angles='xy', scale_units='xy', scale=1)
        return None

    def applyForces(self):
        '''input : None
        output : None --> Forces modify the position of the system (self.x, self.y)'''
        return None

    def move(self, vectors=False):
        plt.plot(self.xcords, self.ycords)
        self.applyForces()
        self.xcords.append(self.x)
        self.ycords.append(self.y)
        self.drawVectors()

    def plot (self) :
        plt.style.use('seaborn')
        plt.xlim (left=self.x - 1)
        plt.ylim (bottom = -1)
        while self.y >= 0 :
            self.move ()
            sleep (0.02)
            plt.clf()
        plt.legend(loc='upper left')
        plt.show()


class Vector:

    def __init__(self, dimensions, vector_coords, position_coords):  # set default parameters ?
        '''input : the number of dimensions, Ax & Ay (coordinates at the basis of the vector) and x & y (coordinates
        of the vector itself
        output : initializing a Vector object'''
        assert dimensions >= 1 and dimensions <= 3 and isinstance(dimensions, int), 'Dimensions are not valid'
        ### Initializing dimensions and tuples ###
        self.dimensions = dimensions
        self.vec_coords = vector_coords
        self.pos_coords = position_coords
        ### Initializing coordinates ###
        if self.dimensions == 1:
            self.x, self.Ax = vector_coords, position_coords
        elif self.dimensions == 2:
            self.x, self.y = vector_coords
            self.Ax, self.Ay = position_coords
        else:
            self.x, self.y, self.z = vector_coords
            self.Ax, self.Ay, self.Az = position_coords

    # Dunder methods - multiply, add, substract Vector instances
    def __repr__(self):
        return f'Vector ({self.dimensions}, {self.vec_coords}, {self.pos_coords})'

    def __abs__(self):
        return round(sqrt(sum([coord ** 2 for coord in self.vec_coords])), 3)

    def __sub__(self, other):
        assert self.dimensions == other.dimensions, 'Objects must have same dimensions'
        return None # implement here

    def __add__(self, other):
        assert self.dimensions == other.dimensions, 'Objects must have same dimensions'
        return None  # implement here

    def __mul__(self, other):
        assert self.dimensions == other.dimensions, 'Objects must have same dimensions'
        # return sum([vA_coord*other.vB_coord for vA_coord in [] for ])
        return None  # implement / change here


def friction (radius, v) :
    return 0.5*air_density*pi*radius**2*drag_coef*v