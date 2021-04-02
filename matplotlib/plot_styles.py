import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print (plt.style.available)
plt.style.use ('seaborn')
data = pd.read_excel ('/home/leo/Bureau/Autres/data_sets/defense_spendings.xls')
print (data.head())
# print (data.tail())

x = data ['Année']
Fra = np.array (data['France'])
Ger = np.array (data['Allemagne'])
Uk = np.array (data['Royaume-Uni'])
Esp = np.array (data['Espagne'])
Ita = np.array (data['Italie'])
Usa = np.array (data['Etats-Unis'])
# Why are there still warning messages although I changed columns
# to numpy arrays ?

plt.plot (x, Fra, 'b--', label = 'FRA')
plt.plot (x, Ger, 'y-.', label = 'GER')
plt.plot (x, Uk, 'k', label = 'UK')
plt.plot (x, Esp, 'r', label = 'SPA')
plt.plot (x, Ita, 'g:', label = 'ITA')
plt.plot(x, Usa, 'c', label = 'USA', lw = 3)

# plt.xkcd()
plt.legend ()
plt.xlabel ('Years')
plt.ylabel ('Countries')
plt.title ('Spendings per inhabitant per year for countrie\'s defense')
plt.savefig ('defense_spendings.png')
plt.show ()