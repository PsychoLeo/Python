import pandas as pd
import sklearn
import numpy as np
from sklearn import linear_model
import csv

x = [i for i in range (10)]
y = [i for i in range(10)]
z = [[2*x[i] + 3*y[j] - 4 for i in x] for j in y]

with open('/home/leo/Bureau/Autres/data_sets/function_graph_values.csv', 'w', newline = '') as file :
    writer = csv.writer(file)
    writer.writerow (["x", "y", "z"])
    for i in range (10) :
        for j in range (10) :
            writer.writerow ([x[i], y[j], z[j][i]])


data = pd.read_csv ('/home/leo/Bureau/Autres/data_sets/function_graph_values.csv', sep =',')
#data = data[['x', 'y', 'z']]
print (data.head())
print(data.tail())

x = np.array (data.drop(['z'], 1))
y = np.array (data['z'])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

linear = linear_model.LinearRegression () # linear model is a module
linear.fit (x_train, y_train)
acc =  linear.score(x_test, y_test)
print(acc)

predictions = linear.predict(x_test)
for i in range (len(predictions)) :
    print (predictions[i], x_test[i], y_test[i])

