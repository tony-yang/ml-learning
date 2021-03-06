from time import time

from data.email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score

features_train, features_test, labels_train, labels_test = preprocess()

# Linear kernel took about 3 minutes, and give an accuracy of about 98.4%. Prediction time is also around 16 seconds. Unlike the other classifier where prediction time runs in sub-second.
# The rbf kernel is much slower than the others. It took almost 18 minutes to train, 2 minutes to predict, with an accuracy of only 49%

#clf = svm.SVC(kernel='linear')
clf = svm.SVC(kernel='rbf')
training_start_time = time()
clf.fit(features_train, labels_train)
training_end_time = time()
pred = clf.predict(features_test)
test_end_time = time()

score = accuracy_score(labels_test, pred)
print('The prediction accuracy score = {}'.format(score))
print('The training time = {} and the prediction time = {}'.format(training_end_time - training_start_time, test_end_time - training_end_time))
