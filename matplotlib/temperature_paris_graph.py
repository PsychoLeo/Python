x_numbers = [1, 2, 3]
y_numbers = [2, 4, 6]

from pylab import plot, show, legend, title, xlabel, ylabel, axis, savefig

# plot (x_numbers, y_numbers, marker ="*")
# show ()

t_paris_2009 = [3, 6, 11, 17, 19, 21, 23, 26, 21, 16, 12, 5]
t_paris_2014 = [8, 9, 14, 16, 17, 22, 23, 21, 22, 18, 12, 7]
t_paris_2019 = [5, 11, 12, 15, 18, 24, 26, 25, 20, 16, 10, 9]
mois = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
plot (mois, t_paris_2009, mois, t_paris_2014, mois, t_paris_2019, marker = "o")
legend ([2009, 2014, 2019])
title ('Average monthly temperature in Paris')
xlabel ('Month')
ylabel ('Temperature (°C)')
axis (ymin = 0)
show ()