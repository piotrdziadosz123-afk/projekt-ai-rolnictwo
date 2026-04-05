from app.data_loader import load_data, min_max_scale, train_test_split
from app.perceptron import Perceptron
from app.metrics import accuracy_score, confusion_matrix


def run_experiment(learning_rate, epochs):
    X, y = load_data("data/crop_data.csv")
    X = min_max_scale(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_ratio=0.8)

    model = Perceptron(learning_rate=learning_rate, epochs=epochs)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    matrix = confusion_matrix(y_test, predictions)

    print("=" * 50)
    print(f"Eksperyment: learning_rate={learning_rate}, epochs={epochs}")
    print(f"Accuracy: {accuracy:.2f}")
    print("Confusion matrix:", matrix)
    print("Wagi:", model.weights)
    print("Bias:", model.bias)
    print()


def main():
    run_experiment(0.1, 10)
    run_experiment(0.1, 50)
    run_experiment(0.1, 100)
    run_experiment(0.01, 50)
    run_experiment(0.5, 50)


if __name__ == "__main__":
    main()