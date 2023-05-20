import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split

def preprocess_data():
    x , y = datasets.fetch_california_housing(return_X_y=True)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)
    np.save('xtrain.npy', x_train)
    np.save('xtest.npy', x_test)
    np.save('ytrain.npy', y_train)
    np.save('ytest.npy', y_test)


if __name__ == '__main__':
     print('Preprocessing data...')
     preprocess_data()