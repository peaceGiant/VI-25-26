import csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.naive_bayes import GaussianNB


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

model = GaussianNB()
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
prec   = TP / (TP + FP)
recall = TP / (TP + FN)

print(f'Acc: {acc}, {accuracy_score(test_y, preds)}')
print(f'Prec: {prec}, {precision_score(test_y, preds)}')
print(f'Recall: {recall}, {recall_score(test_y, preds)}')


new_sample = [45.6, 90.1]

prediction = model.predict([new_sample])[0]
print(f'For sample {new_sample} the predicted class is {prediction}.')





















