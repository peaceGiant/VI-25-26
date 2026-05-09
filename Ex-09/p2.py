import csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier


def read_csv(path):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        lines = list(csv_reader)[1:]

    return lines


data = read_csv('data/medical_data.csv')

# All data is initially of type string
# Convert to respective type when necessary
X, y = [list(map(float, row[:-1])) for row in data], [float(row[-1]) for row in data]

train_X, test_X, train_y, test_y = train_test_split(X, y, train_size=0.7, shuffle=False)

params_1 = {
    'criterion': 'entropy',
    'max_depth': 10,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'max_leaf_nodes': 20,
    'random_state': 0
}

# RandomForestClassifier has the same params as DecisionTreeClassifier
# Except we must also specify the number of trees in the forest with the param `n_estimators`
model = RandomForestClassifier(n_estimators=50, **params_1)

model.fit(train_X, train_y)

preds = model.predict(test_X)

TP, TN, FP, FN = 0, 0, 0, 0
for pred, gt in zip(preds, test_y):
    # if prediction is positive (P) AND prediction is true (T) -> TP
    if pred == 1 and pred == gt:
        TP += 1
    elif pred == 1 and pred != gt:
        FP += 1
    elif pred == 0 and pred == gt:
        TN += 1
    elif pred == 0 and pred != gt:
        FN += 1

acc    = (TP + TN) / (TP + TN + FP + FN)
prec   = TP / (TP + FP) if TP + FP != 0 else 0
recall = TP / (TP + FN) if TP + FN != 0 else 0

print(f'Acc: {acc}, {accuracy_score(test_y, preds)}')
print(f'Prec: {prec}, {precision_score(test_y, preds)}')
print(f'Recall: {recall}, {recall_score(test_y, preds)}')

feature_imps = model.feature_importances_.tolist()
print(f'Feature importances: {feature_imps}')

most_important_feat_index = feature_imps.index(max(feature_imps))
print(f'Most important feature: {most_important_feat_index}')

least_important_feat_index = feature_imps.index(min(feature_imps))
print(f'Least important feature: {least_important_feat_index}')
