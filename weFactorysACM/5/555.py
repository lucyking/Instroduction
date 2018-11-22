import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier



class LogisticRegression:
    def __init__(self, lr=0.01, num_iter=100000, fit_intercept=True, verbose=False):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose

    def features(self, name):
        # name = name.lower()
        return {
            'first-letter': name[0],  # First letter
            'first2-letters': name[0:2],  # First 2 letters
            'first3-letters': name[0:3],  # First 3 letters
            'last-letter': name[-1],
            'last2-letters': name[-2:],
            'last3-letters': name[-3:],
        }

    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)

    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def __loss(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

    def fit(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        # weights initialization
        self.theta = np.zeros(X.shape[1])

        for i in range(self.num_iter):
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            gradient = np.dot(X.T, (h - y)) / y.size
            self.theta -= self.lr * gradient

            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            loss = self.__loss(h, y)

            if (self.verbose == True and i % 10000 == 0):
                print(f'loss: {loss} \t')

    def predict_prob(self, X):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        return self.__sigmoid(np.dot(X, self.theta))

    def predict(self, X):
        return self.predict_prob(X).round()

if __name__ == "__main__":
    model = LogisticRegression()

    names = pd.read_csv('simple_names_dataset.csv')
    print(names)
    print("%d names in dataset" % len(names))
    names = names.as_matrix()[:, 1:]
    print(names)
    # We're using 80% of the data for training
    TRAIN_SPLIT = 0.8
    ret = model.features("John")
    print(ret)
    from sklearn.utils import shuffle

    # Extract the features for the whole dataset
    X = model.features(names[:, 0])  # X contains the features

    # Get the gender column
    y = names[:, 1]  # y contains the targets

    X, y = shuffle(X, y)
    X_train, X_test = X[:int(TRAIN_SPLIT * len(X))], X[int(TRAIN_SPLIT * len(X)):]
    y_train, y_test = y[:int(TRAIN_SPLIT * len(y))], y[int(TRAIN_SPLIT * len(y)):]

    # Check to see if the datasets add up
    print(len(X_train), len(X_test), len(y_train), len(y_test))  # 76020 19005 76020 19005
    vectorizer = DictVectorizer()
    vectorizer.fit(X_train)
    transformed = vectorizer.transform(model.features(["Mary", "John"]))
    print(transformed)
    from sklearn.tree import DecisionTreeClassifier
    clf = DecisionTreeClassifier()
    clf.fit(vectorizer.transform(X_train), y_train)


    features = np.vectorize(model.features)
    print(features(["Anna", "Hannah", "Paul"]))
    # Extract the features for the whole dataset
    # X = features(names[:, 0])  # X contains the features
    # Get the gender column
    # y = names[:, 1]  # y contains the targets
    # Test if we built the dataset correctly
    # print("Name: %s, features=%s, gender=%s" % (names[0][0], X[0], y[0]))

    exit(0)
    # iris = datasets.load_iris()
    # print(iris)
    # X = iris.data[:, :2]
    # y = (iris.target != 0) * 1

    # plt.figure(figsize=(10, 6))
    # plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='b', label='0')
    # plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='r', label='1')
    # plt.legend()
    # plt.show()
    # model.__init__(lr=0.1, num_iter=300000)
    # model.fit(X, y)
    # preds = model.predict(X)
    # (preds == y).mean()
    # plt.figure(figsize=(10, 6))
    # plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='b', label='0')
    # plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='r', label='1')
    # plt.legend()
    # plt.show()
    # x1_min, x1_max = X[:, 0].min(), X[:, 0].max(),
    # x2_min, x2_max = X[:, 1].min(), X[:, 1].max(),
    # xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
    # grid = np.c_[xx1.ravel(), xx2.ravel()]
    # probs = model.predict_prob(grid).reshape(xx1.shape)
    # plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors='black')
    # plt.show()

