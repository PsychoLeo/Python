import matplotlib.pyplot as plt

plt.style.use ('fivethirtyeight')

slices = [120, 110, 80, 40, 50, 10]
names = [str(i) for i in slices]

plt.pie (slices, labels = names, wedgeprops={'edgecolor':'k'})

plt.title ('Pie chart')
plt.show ()