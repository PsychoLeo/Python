import pandas as pd
from matplotlib import pyplot as plt

# data = pd.read_csv('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/05-Fill_Betweens/data.csv')
# data.to_csv ('/home/leo/Bureau/Autres/data_sets/programer_salary.csv')
data = pd.read_csv ('/home/leo/Bureau/Autres/data_sets/programer_salary.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

plt.plot (ages, [overall_median for i in range (len(dev_salaries))], label = 'Average', color = 'r', lw = 2)

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries > dev_salaries),
                 interpolate=True, alpha=0.25, label='Above Avg')

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries <= dev_salaries),
                 interpolate=True, color='red', alpha=0.25, label='Below Avg')

plt.legend(loc = 'upper left')

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.savefig ('salary_programming_filling.png')
plt.show()