import matplotlib.pyplot as plt
import pandas as pd

cols_list = ['Temps','X','Temps','Y','Temps','Vx','Temps','Vy','Temps','Ax','Temps',
             'Ay','Temps','Modele de X','Temps','Modele de Y','Temps','Modele de Vx']
values = pd.read_csv('/home/leo/Bureau/SPH/Terminale/Physique/coordonnees_mouvement_rectiligne.csv')
# print (values)
for i in values :
    print (i)

def plot_coordinates () :
    plt.plot (t, values['X'], t, values['Y'])
    plt.show()


# plot_coordinates()