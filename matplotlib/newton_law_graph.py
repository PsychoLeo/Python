import matplotlib.pyplot as plt
def draw_graph (x, y) :
    plt.plot (x, y, marker ="o")
    plt.xlabel ('Distance (m)')
    plt.ylabel ('Value of the gravitational force (N)')
    plt.title ('Gravitational force and distance')
    plt.show ()
    
def generate () :
    r = range(100, 1001, 50)
    F = []
    m_a = 0.5
    m_b = 1.5
    G = 6.674*(10**(-11))
    for i in r :
        F.append ((G*m_a*m_b)/(i**2))
    draw_graph (r, F)
    
if __name__ == '__main__' :
    generate ()