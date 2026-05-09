import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def read_data(path):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        lines = list(csv_reader)[1:]

    return lines

data = read_data('data/car.csv')

# Let's assume the target is not in the last column of the dataset
target_index = 5

X, y = [[el for i, el in enumerate(row) if i != target_index] for row in data], [row[target_index] for row in data]

encoder = OrdinalEncoder()
X_enc = encoder.fit_transform(X)

train_X, test_X, train_y, test_y = train_test_split(X_enc, y, shuffle=False, train_size=0.75)

params_1 = {
    'criterion': 'entropy',
    'max_depth': 10,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'max_leaf_nodes': 20,
    'random_state': 0
}


dt_1 = DecisionTreeClassifier(**params_1)

dt_1.fit(train_X, train_y)

# Another way to calculate accuracy
acc_1 = dt_1.score(test_X, test_y)
# print(acc_1)

feature_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'acceptability']
feature_imps  = dt_1.feature_importances_.tolist()
# print(*zip(feature_names, feature_imps))

most_important_feat_index = feature_imps.index(max(feature_imps))
# print(most_important_feat_index)

# Now, let's create a dataset without the most important feature
X_enc_2 = [[el for i, el in enumerate(row) if i != most_important_feat_index] for row in X_enc]

train_X, test_X, train_y, test_y = train_test_split(X_enc_2, y, shuffle=False, train_size=0.75)

dt_2 = DecisionTreeClassifier(**params_1)

dt_2.fit(train_X, train_y)

preds = dt_2.predict(test_X)
acc_2 = accuracy_score(preds, test_y)
# Compare and interpret the resulting accuracies
# print(acc_1, acc_2)

# Getting the depth of the tree and the number of leaves of the built trees:
# print(dt_1.get_depth(), dt_2.get_depth())
# print(dt_1.get_n_leaves(), dt_2.get_n_leaves())

