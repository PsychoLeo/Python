import matplotlib.pyplot as plt
import math

Cc = 8.99*(10**9) # constante de Coulomb

######################
### Particle class ###
######################

class Particle:

    def __init__(self, charge, position=(0, 0)):
        '''Initializing electrically charged particle'''
        self.charge = charge
        self.x, self.y = position


############################################
### System class to simulate environment ###
############################################

class System:

    def __init__(self, scale, size=10):
        '''Initializing system (with its size and scale)
        size : number of rows and columns
        scale : size of one graduation (in meters)'''
        self.scale = scale
        self.size = size
        self.xmin = -size//2
        self.xmax = size//2
        self.particles = []

    def addParticle(self, particle):
        '''Adds a particle to the system'''
        self.particles.append(particle)

    def ChampElectroStatique(self, xM, yM):
        '''input : coordinates of a point in space
        output : the coordinates of the vector of the electrostatic force acting on it'''
        vf = Vector (0, 0, xM, yM) # final vector (will be modified)
        xI, yI, qI = [p.x for p in self.particles], [p.y for p in self.particles], [p.charge for p in self.particles]
        for xi, yi, qi in zip (xI, yI, qI) :
            vn = Vector (xM-xi, yM-yi, xM, yM) # current vector
            coef = qi/(math.sqrt((xM-xi)**2+(yM-yi)**2)**3*(self.scale**2))
            vn *= coef
            vf += vn
        return vf*Cc

    def plotCharges (self) :
        '''Plots the charges in the system'''
        x = [p.x for p in self.particles]
        y = [p.y for p in self.particles]
        charges = [p.charge for p in self.particles]
        plt.scatter(x, y, 100, color='red', edgecolors='black')
        for i, txt in enumerate(charges):
            plt.annotate(f'{txt:.1e}', (x[i], y[i]))

    def plotQuivers(self):
        '''Plots the quivers of the electrostatic field'''
        particle_coords = [(p.x, p.y) for p in self.particles]
        coords = [(i, j) for i in range(self.xmin, self.xmax+1) for j in range(self.xmin, self.xmax+1)
                  if (i, j) not in particle_coords]
        for xM, yM in coords :
            vec = self.ChampElectroStatique(xM, yM)
            plt.quiver (vec.Ax, vec.Ay, vec.x, vec.y)

    def plot(self):
        '''Plots the system | Draws the electrostatic field surrounding the particle'''
        border = 0.5
        plt.xlim(self.xmin-border, self.xmax+border)
        plt.ylim(self.xmin-border, self.xmax+border)
        self.plotCharges()
        self.plotQuivers()
        plt.show()


######################################
### Vector Plotting and operations ###
######################################

class Vector:

    def __init__(self, x, y, Ax, Ay):
        self.x = x
        self.y = y
        self.Ax = Ax
        self.Ay = Ay

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.Ax, self.Ay)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.Ax, self.Ay)

    def __mul__(self, coef):
        return Vector(self.x*coef, self.y*coef, self.Ax, self.Ay)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'Vector({self.x:.4e}, {self.y:.4e}, {self.Ax}, {self.Ay})'

#####################
### Running test ####
#####################

scale1, scale2 = 10**(-10), 1
system1, system2 = System(scale1), System(scale2)
charge1, charge2 = 10**(-19), 1
position1, position2 = (0, 0), (2, -3)

system1.addParticle(Particle(charge1, position2))
system1.addParticle(Particle(-charge1, position1))
system1.addParticle(Particle(charge1, (4, 4)))
system1.plot()

# if __name__ == '__main__':
#     scale = eval(input('Enter the scale of your System (size of one graduation, in meters) : '))
#     system = System(scale)  # initializing system with its default size | scale parameter added
#     num_particles = int(input('Enter the number of particles : '))
#     assert num_particles > 0, 'Number of particles has to be stricly positive'
#     for i in range(num_particles):
#         charge = eval(input(f'Enter the charge of your particle n°{i+1} (Coulomb) : '))
#         position = eval(input(f'Enter the position of your particle n°{i+1} (x, y) : '))
#         print ()
#         system.addParticle(Particle(charge, position))
#     system.plot()