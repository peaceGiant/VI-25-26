# Reading datasets
# 1.
import csv

def read_csv(path):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        lines = list(csv_reader)[1:]

    return lines

data = read_csv('data/car.csv')

print(data[:10])


# 2.
import pandas as pd

data = pd.read_csv('data/car.csv')
data = data.values.tolist()

# print(data[:10])

# Play around with datasets from scikit-learn
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

print(X[:10], y[:10])















