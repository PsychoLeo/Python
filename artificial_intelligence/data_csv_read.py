#### Part 1 ####

import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style

data = pd.read_csv ('/home/leo/Bureau/Autres/data_sets/student-mat.csv', sep = ';')

# print (data.head())
# print (data.tail())
data = data [['G1', 'G2', 'G3', 'studytime', 'absences', 'failures']]

predict = 'G3' # also known as a label
x = np.array (data.drop([predict], axis = 1)) # if 0 is specified, the lines are dropped,
# else, the columns are dropped (value can't be different from 0 or 1)
# the column 'G3' is not removed, but it is dropped into x
y = np.array (data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
# this split 0.1 (10%) of the data into x_test and y_test to test these when the model has
# been trained to see if it does well evaluating a situation it has never encountered


#### Part 2 ####

'''
Linear regression : 
- find a best-fit line that fits to the data
- find the correlation between x and y (slope of equation y = ax + b)
Sometimes, it is not the optimal solution (randomized points that don't fit into a line)
'''
# as everything is saved in pickle, it is possible to get the results from the pickle file

# creating a model and evaluating its efficiency
'''
best = 0
for _ in  range (100) :
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
    linear = linear_model.LinearRegression () # creating a model
    linear.fit (x_train, y_train) # fits the data to find a best-fit line
    accuracy = linear.score(x_test, y_test)
    print (accuracy)
    if accuracy > best :
        best = accuracy
        print ()
        print (best)
        with open ('/home/leo/Bureau/Autres/data_sets/student_model.pickle', 'wb') as file : # write binary
            pickle.dump (linear, file)
'''

pickle_in = open ('/home/leo/Bureau/Autres/data_sets/student_model.pickle', 'rb') # read binary
linear = pickle.load (pickle_in)

print (f'Linear coefficient (a values): {linear.coef_}')
# returns 5 values as there are 5 parameters (G1, G2, absences...)
print (f'Interception (b value): {linear.intercept_}')

predictions = linear.predict(x_test)
for x in range (len(predictions)) :
    print (round(predictions[x], 3), x_test[x], y_test[x], round(abs(predictions[x] - y_test[x]), 3))

#### plotting with matplotlib ####

xparam = 'failures'
yparam = 'G3'
# style.use ('ggplot')
plt.scatter (data[xparam], data[yparam])
plt.xlabel (xparam)
plt.ylabel ('Final grade')
plt.grid ()
plt.show ()
