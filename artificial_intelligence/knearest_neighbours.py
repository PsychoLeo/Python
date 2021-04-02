import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
import matplotlib.pyplot as plt

# attrs = 'buying, maint, doors, persons, lug_boot, safety'.split (', ')

data_sets = '/home/leo/Bureau/Autres/data_sets/'
data = pd.read_csv (data_sets + 'cars_info.data')
# print (data.head())

le = preprocessing.LabelEncoder ()
buying = le.fit_transform(list(data['buying']))
maint = le.fit_transform(list(data['maint']))
door = le.fit_transform(list(data['door']))
persons = le.fit_transform(list(data['persons']))
lug_boot = le.fit_transform(list(data['lug_boot']))
safety = le.fit_transform(list(data['safety']))
cls = le.fit_transform(list(data['class']))

predict = 'class'

x = list(zip(buying, maint, door, persons, lug_boot, safety))
# creates a list of tuples of each 0th arg. of input arrays,
# 1st arg, 2nd arg etc -> [(buying[0], maint[0], ..., safety[0]), etc.]
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)
# print (x_train, y_test)
model = KNeighborsClassifier(n_neighbors=7)
model.fit (x_train, y_train)
acc = model.score (x_test, y_test)

predicted = model.predict(x_test)
names = ['unacc', 'acc', 'good', 'ygood']

diff = 0
for i in range (len(predicted)) :
    diff += abs(predicted[i] - y_test[i])
    print ('Predicted :', predicted[i], '|| Data :', x_test[i], '|| Actual :', y_test[i])
print ()
print ('Overall error per test :', diff/len(predicted))

#### Plotting efficiency with matplotlib ####
'''
xplt = list(range (1,101))
yplt = []
# plt.style.use ('seaborn')
for i in xplt :
    best = 0
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
    for _ in range (3) :
        model = KNeighborsClassifier(n_neighbors=i)
        model.fit (x_train, y_train)
        acc = model.score (x_test, y_test)
        if acc > best :
            best = acc
    yplt.append (best)
'''

# print ('Best k value for accuracy :', yplt.index(max(yplt))+1)

# plt.title ('Evolution of model accuracy in terms of nearest neighbors')
# plt.title ('Number of nearest neighbors')
# plt.ylabel ('Accuracy')
# plt.plot (xplt, yplt)
# plt.savefig ('/home/leo/Bureau/Programmation/Python/maths/plots/KNN_accuracy.png')
# plt.show ()