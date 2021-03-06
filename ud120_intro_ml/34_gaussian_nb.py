import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.metrics import accuracy_score
import pprint

pp = pprint.PrettyPrinter(indent=4)

def make_terrain_data(n_points=1000):
    random.seed()
    bumpy_sig = [random.uniform(0, 0.9) for i in range(n_points)]
    bumpy_bkg = [random.random() for i in range(n_points)]

    grade_sig = []
    grade_bkg = []

    for x in bumpy_sig:
        error = random.uniform(0, 0.1)
        grade_sig.append(max(0, random.uniform(0.0, (1.0 - x)) - error))

    for x in bumpy_bkg:
        error = random.uniform(0, 0.03)
        grade_bkg.append(min(1, random.uniform((1.0 - x), 1.0) - error))

    return bumpy_sig, grade_sig, bumpy_bkg, grade_bkg

def create_label(bumpy_sig, grade_sig, bumpy_bkg, grade_bkg):
    features_train_sig = np.c_[bumpy_sig, grade_sig]
    features_train_bkg = np.c_[bumpy_bkg, grade_bkg]

    features_train = np.concatenate((features_train_sig, features_train_bkg), axis=0)
    labels_train = [1]*len(bumpy_sig) + [2] * len(bumpy_bkg)

    return features_train, labels_train

def main():
    x_min, x_max = 0.0, 1.0
    y_min, y_max = 0.0, 1.0
    bumpy_sig, grade_sig, bumpy_bkg, grade_bkg = make_terrain_data(200)

    # Plot the data
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.legend()
    plt.xlabel('bumpiness')
    plt.ylabel('grade')

    # Train the data
    features_train, labels_train = create_label(bumpy_sig, grade_sig, bumpy_bkg, grade_bkg)

    print('bumpy sig')
    print(bumpy_sig)

    print('features train')
    print(features_train)
    print('features train shape')
    print(features_train.shape)
    print('labels train')
    print(labels_train)

    test_bumpy_sig, test_grade_sig, test_bumpy_bkg, test_grade_bkg = make_terrain_data(200)
    features_test, labels_test = create_label(test_bumpy_sig, test_grade_sig, test_bumpy_bkg, test_grade_bkg)

    clf = GaussianNB()
    #clf = svm.SVC()
    clf.fit(features_train, labels_train)
    #pred = clf.predict(features_test)

    # XX = np.concatenate((np.array(test_bumpy_sig), np.array(test_bumpy_bkg)))
    # XX_shape = XX.reshape(20, 20)
    # YY = np.concatenate((np.array(test_grade_sig), np.array(test_grade_bkg)))
    # YY_shape = YY.reshape(20, 20)
    # # Z = np.array(labels_test).reshape(XX.shape)
    # Z = clf.predict(features_test)

    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    XX_shape = XX
    YY_shape = YY
    # test_pred = np.c_[XX.ravel(), YY.ravel()]
    features_test2, labels_test2 = create_label(XX.ravel(), YY.ravel(), [], [])
    Z = clf.predict(features_test2)
    print('XX')
    print(XX)
    print('XX shape')
    print(XX.shape)
    print('XX_shape')
    print(XX_shape)
    print('XX_shape shape')
    print(XX_shape.shape)

    # print('features test')
    # print(features_test)
    # print('features test shape')
    # print(features_test.shape)

    print('features test 2')
    print(features_test2)
    print('features test 2 shape')
    print(features_test2.shape)

    print('Z')
    print(Z)
    print('Z shape')
    print(Z.shape)

    # print('test_pred')
    # print(test_pred)



    # score = accuracy_score(labels_test, Z)
    # print('The prediction accuracy score = {}'.format(score))

    Z = Z.reshape(XX_shape.shape)

    plt.pcolormesh(XX_shape, YY_shape, Z, cmap=plt.cm.Paired)
    # plt.scatter(XX, YY, color='k', label='mgrid')
    plt.scatter(bumpy_sig, grade_sig, color='b', label='fast')
    plt.scatter(bumpy_bkg, grade_bkg, color='r', label='slow')

    plt.show()

if __name__ == '__main__':
    main()
