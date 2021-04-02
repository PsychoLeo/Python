import matplotlib.pyplot as plt
# import numpy as np
import csv
from collections import Counter

num_languages = 15

with open ('/home/leo/Bureau/Autres/data_sets/programming_languages.csv') as file :
    csv_file = csv.DictReader (file) # iterator
    # row = next(csv_file)
    # print (row['LanguagesWorkedWith'].split(';'))
    c = Counter ()
    for i in csv_file :
        c.update (i['LanguagesWorkedWith'].split(';'))
    c = c.most_common(num_languages)
    x, y = [i[0] for i in c][::-1], [i[1] for i in c][::-1]
    # print (f'x vals : {x} & y_vals : {y}')

plt.style.use ('seaborn')
plt.barh (x, y)
plt.title ('Programming languages used (10.000 people)')
# when using barh, x and y labels should be changed
plt.xlabel ('Popularity')
# plt.ylabel ('Language')
# plt.savefig ('programming_languages.png')
plt.show ()