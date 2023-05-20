import argparse
import joblib
import numpy as np
from sklearn.linear_model import SGDRegressor


def test_model(x_test, y_test):
    x_test_data = np.load(x_test)
    y_test_data = np.load(y_test)

    model = SGDRegressor(verbose=1)
    model.fit(x_test_data, y_test_data)

    joblib.dump(model, 'model.pkl')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x_test')
    parser.add_argument('--y_test')
    args = parser.parse_args()
    test_model(args.x_test, args.y_test)