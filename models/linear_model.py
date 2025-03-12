from sklearn.linear_model import LinearRegression
import pickle

class HousePriceModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def save_model(self, filename="models/model.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self.model, f)

    def load_model(self, filename="models/model.pkl"):
        with open(filename, "rb") as f:
            self.model = pickle.load(f)
