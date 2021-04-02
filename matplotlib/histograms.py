import matplotlib.pyplot as plt
import pprint
import pandas as pd

#### Finding plot style liked ####
# x = list(range(10))
# y = [i**2 for i in x]
#
# good = []
# pprint.pprint (plt.style.available)
# for styl in plt.style.available :
#     plt.style.use (styl)
#     plt.plot (x, y)
#     plt.show ()
#     choice = input ('Good style ? : ')
#     if choice != '' :
#         good.append (styl)
# print (good)

plt.style.use('seaborn')

data = pd.read_csv('/home/leo/Bureau/Autres/data_sets/programmer_ages.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', log=True)

median_age = 29
color = '#fc4f30'

plt.axvline(median_age, color=color, label='Age Median', linewidth=2)

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.show ()