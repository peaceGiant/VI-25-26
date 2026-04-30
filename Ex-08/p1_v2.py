import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score


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

train_X, test_X, train_y, test_y = train_test_split(X_enc, y, train_size=0.7, shuffle=False)

model = CategoricalNB()
model.fit(train_X, train_y)

preds_y = model.predict(test_X)

acc = accuracy_score(test_y, preds_y)
print(f'Accuracy: {acc}')

new_sample = ['high', 'low', '4', '2', 'small', 'low']
new_sample_enc = encoder.transform([new_sample])[0]

pred_y = model.predict([new_sample_enc])[0]
print(f'Predicted class: {pred_y}')

pred_probas = model.predict_proba([new_sample_enc])
print('Probability for each class:')
for proba, label in zip(pred_probas[0], model.classes_):
    print(f'\tlabel {label}: {round(proba, 5)}')
