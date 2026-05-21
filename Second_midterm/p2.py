import warnings
warnings.filterwarnings('ignore')

from data.d2 import dataset
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

if __name__ == '__main__':
    C, N, S = int(input()), int(input()), int(input())

    dataset = [row[:-1] + [1 if row[-1] > 50 else 0] for row in dataset]

    split_idx = int(len(dataset) * 0.7)
    train_set = dataset[:split_idx]
    test_set  = dataset[split_idx:]

    train_X, train_y = [row[:-1] for row in train_set], [row[-1] for row in train_set]
    test_X, test_y = [row[:-1] for row in test_set], [row[-1] for row in test_set]

    model = MLPClassifier(
        hidden_layer_sizes=(50,),
        activation='relu',
        learning_rate_init=0.001,
        max_iter=25,
        random_state=0
    )

    # (1) original dataset
    model.fit(train_X, train_y)
    acc_1 = model.score(test_X, test_y)

    # (2) removing anomalies
    c_idx = 3
    n_idx = 4
    s_idx = 5

    train_X_out, test_X_out = [], []
    for row in train_X:
        nrow = []
        for i, el in enumerate(row):
            if i not in [c_idx, n_idx, s_idx]:
                nrow.append(el)
            elif i == c_idx:
                nrow.append(el if el <= C else C)
            elif i == n_idx:
                nrow.append(el if el <= N else N)
            elif i == s_idx:
                nrow.append(el if el <= S else S)
        train_X_out.append(nrow)

    for row in test_X:
        nrow = []
        for i, el in enumerate(row):
            if i not in [c_idx, n_idx, s_idx]:
                nrow.append(el)
            elif i == c_idx:
                nrow.append(el if el <= C else C)
            elif i == n_idx:
                nrow.append(el if el <= N else N)
            elif i == s_idx:
                nrow.append(el if el <= S else S)
        test_X_out.append(nrow)

    model.fit(train_X_out, train_y)
    acc_2 = model.score(test_X_out, test_y)

    # (3) standardize data
    scaler = StandardScaler()
    model.fit(scaler.fit_transform(train_X), train_y)
    acc_3 = model.score(scaler.transform(test_X), test_y)

    # (4) removing anomalies + standardize data
    model.fit(scaler.fit_transform(train_X_out), train_y)
    acc_4 = model.score(scaler.transform(test_X_out), test_y)

    print(f'''Accuracy with:
The original dataset: {acc_1}
Removed anomalies: {acc_2}
Scaled attributes: {acc_3}
Removed anomalies and scaled attributes: {acc_4}''')
