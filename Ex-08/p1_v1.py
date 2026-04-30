import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB


def read_csv(path):
    with open(path, 'r') as file:
        csv_reader = csv.reader(file)
        lines = list(csv_reader)[1:]

    return lines


data = read_csv('data/car.csv')
n = len(data)

X, y = [row[:-1] for row in data], [row[-1] for row in data]

encoder = OrdinalEncoder()
X_enc = encoder.fit_transform(X).tolist()

train_X, test_X = X_enc[:int(0.7 * n)], X_enc[int(0.7 * n):]
train_y, test_y = y[:int(0.7 * n)], y[int(0.7 * n):]

model = CategoricalNB()
model.fit(train_X, train_y)

preds_y = model.predict(test_X)

count = 0
for pred_y, gt_y in zip(preds_y, test_y):
    if pred_y == gt_y:
        count += 1

acc = count / len(test_y)
print(f'Accuracy: {acc}')

new_sample = ['high', 'low', '4', '2', 'small', 'low']
new_sample_enc = encoder.transform([new_sample])[0]

pred_y = model.predict([new_sample_enc])[0]
print(f'Predicted class: {pred_y}')

pred_probas = model.predict_proba([new_sample_enc])
print('Probability for each class:')
for proba, label in zip(pred_probas[0], model.classes_):
    print(f'\tlabel {label}: {round(proba, 5)}')
