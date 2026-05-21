from data.d3 import dataset

from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

class Ensemble:

    def __init__(self, M):
        self.nb = GaussianNB()
        self.dt = DecisionTreeClassifier(criterion='gini', max_depth=M, random_state=0)

    def fit(self, X, y):
        self.nb.fit(X, y)
        self.dt.fit(X, y)

    def score(self, X, y):
        preds_nb = self.nb.predict(X)
        preds_probas_nb = self.nb.predict_proba(X)

        preds_dt = self.dt.predict(X)
        preds_probas_dt = self.dt.predict_proba(X)

        count = 0
        for pred_nb, proba_nb, pred_dt, proba_dt, gt_y in zip(preds_nb, preds_probas_nb, preds_dt, preds_probas_dt, y):
            if pred_nb == pred_dt == gt_y:
                count += 1
            elif pred_nb == gt_y and max(proba_nb) > max(proba_dt):
                count += 1
            elif pred_dt == gt_y and max(proba_dt) > max(proba_nb):
                count += 1

        acc = count / len(y)

        return acc

if __name__ == '__main__':
    N, M = int(input()), int(input())

    n = len(dataset)
    split_idx_1 = n // 3
    split_idx_2 = 2 * n // 3

    S1 = dataset[:split_idx_1]
    X1, y1 = [row[:-1] for row in S1], [row[-1] for row in S1]

    S2 = dataset[split_idx_1:split_idx_2]
    X2, y2 = [row[:-1] for row in S2], [row[-1] for row in S2]

    S3 = dataset[split_idx_2:]
    X3, y3 = [row[:-1] for row in S3], [row[-1] for row in S3]

    model_1 = RandomForestClassifier(n_estimators=N, criterion='gini', random_state=0)
    model_2 = Ensemble(M=M)

    Xs = [X1, X2, X3]
    ys = [y1, y2, y3]

    accs_1 = []
    accs_2 = []
    for i in range(3):
        test_X, test_y = Xs[i], ys[i]
        train_X, train_y = [], []
        for j in range(3):
            if j == i:
                continue
            train_X.extend(Xs[j])
            train_y.extend(ys[j])

        model_1.fit(train_X, train_y)
        model_2.fit(train_X, train_y)

        acc_1 = model_1.score(test_X, test_y)
        acc_2 = model_2.score(test_X, test_y)

        accs_1.append(acc_1)
        accs_2.append(acc_2)

    avg_acc_1 = sum(accs_1) / 3
    avg_acc_2 = sum(accs_2) / 3

    print(f'''Accuracy with random forest: {avg_acc_1}
Accuracy with naive bayes and decision tree: {avg_acc_2}
''')











