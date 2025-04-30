import numpy as np
from numpy.linalg import norm


class module:
    def __init__(self, X, target):
        self.X = X
        self.target = target
        self.weights = []
        self.mean = None  # To store feature means for standardization
        self.sd = None    # To store feature standard deviations for standardization

    def fit(self):
        def gradient_descent(initial_points, derv_f, lr, pr, max_iter):
            last_theta = np.full(initial_points.shape, np.inf)
            cur_theta = initial_points.copy()

            while norm(last_theta - cur_theta) > pr and max_iter > 0:
                last_theta = cur_theta.copy()
                gr = derv_f(cur_theta)
                cur_theta -= gr * lr
                max_iter -= 1

            return cur_theta

        # Data
        X = self.X  # Features
        y = self.target

        # Standardization
        self.mean = np.mean(X, axis=0)
        self.sd = np.std(X, axis=0)
        X_standardized = (X - self.mean) / self.sd

        # Add intercept column
        X_b = np.c_[np.ones(X_standardized.shape[0]), X_standardized]

        # Initial weights
        initial_weights = np.full((X_b.shape[1],), 0, dtype=np.float64)

        # Gradient computation
        n = X_b.shape[0]

        def derv_f(weights):
            predictions = X_b.dot(weights)
            cost = predictions - y
            return (1 / n) * X_b.T.dot(cost)

        # Run gradient descent
        final_weights = gradient_descent(
            initial_points=initial_weights,
            derv_f=derv_f,
            lr=0.001,
            pr=0.0000001,
            max_iter=10000
        )

        self.weights = final_weights
        self.X = X_b
        return final_weights

    def performance(self):
        # Variables Initialization
        X_b = self.X
        y = self.target
        final_weights = self.weights

        # Make Predictions
        predictions = X_b.dot(final_weights)

        # Evaluate Performance
        mse = np.mean((predictions - y) ** 2)
        mape = np.mean(np.abs((predictions - y) / y)) * 100

        for i in np.random.randint(0, X_b.shape[0], size=(5)):
            print(f"Module Prediction: {predictions[i]:,.2f} - Real: {y[i]:,.2f}")

        print(f"MAPE: {mape.__round__(2)}% | MSE: {mse:.2f}")
        return mape.__round__(2), mse

    def predict(self, Predict: list):
        Predict = np.array(Predict).reshape((1, len(Predict)))

        # Standardize Predict using stored mean and sd
        if self.mean is not None and self.sd is not None:
            Predict = (Predict - self.mean) / self.sd
        else:
            raise Exception("Model is not fitted. Please fit the model before predicting.")

        # Add intercept
        Predict = np.c_[np.ones((Predict.shape[0], 1)), Predict]

        X = self.X
        if Predict.shape[1] != X.shape[1]:
            raise Exception(f"X vector shape isn't compatible with Features shape: {X.shape}")

        target = Predict.dot(self.weights)
        return target[0].__round__(3)

