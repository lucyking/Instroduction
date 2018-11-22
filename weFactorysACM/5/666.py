import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import shuffle
from sklearn.feature_extraction import DictVectorizer

names = pd.read_csv('names_dataset.csv')
print(names)
print("%d names in dataset" % len(names))  # 95025 names in dataset

# Get the data out of the dataframe into a numpy matrix and keep only the name and gender columns
names = names.as_matrix()[:, 1:]
print(names)

# We're using 80% of the data for training
TRAIN_SPLIT = 0.8


def features(name):
    name = name.lower()
    return {
        'first-letter': name[0],  # First letter
        'first2-letters': name[0:2],  # First 2 letters
        'first3-letters': name[0:3],  # First 3 letters
        'last-letter': name[-1],
        'last2-letters': name[-2:],
        'last3-letters': name[-3:],
    }


print(features("John"))
# {'first2-letters': 'jo', 'last-letter': 'n', 'first-letter': 'j', 'last2-letters': 'hn', 'last3-letters': 'ohn', 'first3-letters': 'joh'}

# Vectorize the features function
features = np.vectorize(features)
print(features(["Anna", "Hannah", "Paul"]))

# [ array({'first2-letters': 'an', 'last-letter': 'a', 'first-letter': 'a', 'last2-letters': 'na', 'last3-letters': 'nna', 'first3-letters': 'ann'}, dtype=object)
#   array({'first2-letters': 'ha', 'last-letter': 'h', 'first-letter': 'h', 'last2-letters': 'ah', 'last3-letters': 'nah', 'first3-letters': 'han'}, dtype=object)
#   array({'first2-letters': 'pa', 'last-letter': 'l', 'first-letter': 'p', 'last2-letters': 'ul', 'last3-letters': 'aul', 'first3-letters': 'pau'}, dtype=object)]

# Extract the features for the whole dataset
X = features(names[:, 0])  # X contains the features
# Get the gender column
y = names[:, 1]  # y contains the targets
# Test if we built the dataset correctly
print("Name: %s, features=%s, gender=%s" % (names[0][0], X[0], y[0]))
# Name: Mary, features={'first2-letters': 'ma', 'last-letter': 'y', 'first-letter': 'm', 'last2-letters': 'ry', 'last3-letters': 'ary', 'first3-letters': 'mar'}, gender=F


X, y = shuffle(X, y)
X_train, X_test = X[:int(TRAIN_SPLIT * len(X))], X[int(TRAIN_SPLIT * len(X)):]
y_train, y_test = y[:int(TRAIN_SPLIT * len(y))], y[int(TRAIN_SPLIT * len(y)):]

# Check to see if the datasets add up
print(len(X_train), len(X_test), len(y_train), len(y_test))  # 76020 19005 76020 19005


print(features(["Mary", "John"]))
vectorizer = DictVectorizer()
vectorizer.fit(X_train)

transformed = vectorizer.transform(features(["Mary", "John"]))
print(transformed)
"""
  (0, 12)   1.0
  (0, 244)  1.0
  (0, 2722) 1.0
  (0, 4516) 1.0
  (0, 4827) 1.0
  (0, 5147) 1.0
  (1, 9)    1.0
  (1, 199)  1.0
  (1, 2263) 1.0
  (1, 4505) 1.0
  (1, 4640) 1.0
  (1, 7202) 1.0
"""

print(type(transformed))  # <class 'scipy.sparse.csr.csr_matrix'>
print(transformed.toarray()[0][12])  # 1.0
print(vectorizer.feature_names_[12])


clf = DecisionTreeClassifier()
clf.fit(vectorizer.transform(X_train), y_train)

print(clf.predict(vectorizer.transform(features(["Alex", "Emma"]))))  # ['M' 'F']

# Accuracy on training set
print(clf.score(vectorizer.transform(X_train), y_train))  # 0.988292554591 = 98.8% accurate

# Accuracy on test set
print(clf.score(vectorizer.transform(X_test), y_test))  # 0.863246514075 = 86.3% accurate