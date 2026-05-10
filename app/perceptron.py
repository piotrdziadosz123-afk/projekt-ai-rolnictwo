class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=50):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = []
        self.bias = 0.0

    def predict_single(self, x):
        activation = sum(w * xi for w, xi in zip(self.weights, x)) + self.bias
        return 1 if activation >= 0 else 0

    def predict(self, X):
        return [self.predict_single(x) for x in X]

    def fit(self, X, y):
        num_features = len(X[0])
        self.weights = [0.0 for _ in range(num_features)]
        self.bias = 0.0

        for _ in range(self.epochs):
            for x_i, y_true in zip(X, y):
                y_pred = self.predict_single(x_i)
                error = y_true - y_pred

                for j in range(num_features):
                    self.weights[j] += self.learning_rate * error * x_i[j]

                self.bias += self.learning_rate * error