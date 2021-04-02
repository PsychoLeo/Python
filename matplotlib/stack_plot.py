import matplotlib.pyplot as plt

minutes = list(range(1, 9))
p1 = [0, 1, 2, 3, 4, 4, 4, 5]
p2 = [0, 0, 1, 1, 2, 3, 4, 4]
p3 = [1, 1, 1, 2, 3, 4, 5, 6]

names = ['Player1', 'Player2', 'Player3']
col = ['b', 'g', 'r']

plt.stackplot (minutes, p1, p2, p3, labels = names, colors = col)

plt.title ('Evolution of score by time (min)')
plt.xlabel ('Time (minutes)')
plt.ylabel ('Points')
plt.legend (loc = 'upper left')
plt.show ()

# stack plots can also be useful when showing a constant value
# composed of more variables

project_time = list(range(10))

w1 = [5, 2, 4, 8, 4, 2, 3, 0, 1, 0]
w2 = [4, 7, 3, 2, 1, 3, 2, 3, 2, 2]
w3 = [1, 1, 3, 0, 5, 5, 5, 7, 7, 8]
# lists of workers that spent 10 hours per day on project

names = ['Leo', 'Jaaj', 'Mario']
cols = ['#d14c30', '#3995cb', '#559e4c']

plt.stackplot (project_time, w1, w2, w3, labels = names, colors = cols)

plt.legend ()
plt.title ('Time invested in project per programmer')
plt.ylabel ('Time')
plt.xlabel ('Days')
plt.show ()