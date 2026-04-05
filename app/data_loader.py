import random
import pandas as pd


def load_data(path: str):
    df = pd.read_csv(path)

    X = df[["wilgotnosc", "temperatura", "opady", "ph"]].values.tolist()
    y = df["decyzja"].tolist()

    return X, y


def min_max_scale(X):
    num_features = len(X[0])
    mins = [min(row[i] for row in X) for i in range(num_features)]
    maxs = [max(row[i] for row in X) for i in range(num_features)]

    X_scaled = []

    for row in X:
        scaled_row = []
        for i, value in enumerate(row):
            if maxs[i] == mins[i]:
                scaled_row.append(0.0)
            else:
                scaled_row.append((value - mins[i]) / (maxs[i] - mins[i]))
        X_scaled.append(scaled_row)

    return X_scaled


def train_test_split(X, y, train_ratio=0.8):
    data = list(zip(X, y))
    random.shuffle(data)

    split_index = int(len(data) * train_ratio)
    train_data = data[:split_index]
    test_data = data[split_index:]

    X_train = [x for x, _ in train_data]
    y_train = [label for _, label in train_data]
    X_test = [x for x, _ in test_data]
    y_test = [label for _, label in test_data]

    return X_train, X_test, y_train, y_test