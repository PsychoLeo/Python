import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

cancer = datasets.load_breast_cancer()
# print (cancer.feature_names)
# print (cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)
# print (x_train, y_train)

classes = ['malignant', 'benign']

xplt = list(range(20))
c_vals = [1, 2, 3]
kernel_vals = ['rbf', 'linear', 'poly']
colors = ['deepskyblue', 'lightsteelblue', 'navy']
line_styles = ['solid', 'dotted', 'dashed']

for kern in range(len(kernel_vals)) :
    clr = colors[kern]
    for c in range(len(c_vals)) :
        line_stl = line_styles[c]
        yplt = []
        for _ in range (len(xplt)) :
            x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)
            clf = svm.SVC(kernel = kernel_vals[kern], C = c_vals[c])
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            acc = metrics.accuracy_score(y_test, y_pred)
            yplt.append (acc)
        plt.plot (xplt, yplt, marker = None, label = kernel_vals[kern]+str(c_vals[c]), linestyle = line_stl, color = clr)
plt.ylim ([0.85, 1])
plt.xlabel ('Number of executions')
plt.ylabel ('Accuracy')
plt.title ('Support vector machine efficiency')
plt.legend (loc = 'lower left')
plt.show ()

# clf = svm.SVC(kernel = 'linear', C = 2)
# clf.fit(x_train, y_train)
# y_pred = clf.predict(x_test)
# acc = metrics.accuracy_score(y_test, y_pred)
# print (acc)

# C is the margin size, kernel is the curve to separate 2 groups
# kernel values : linear, poly, rbf, (sigmoid)