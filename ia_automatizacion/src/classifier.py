from sklearn.naive_bayes import MultinomialNB

class TextClassifier:
    def __init__(self):
        self.model = MultinomialNB()
        self.vectorizer = None
        self.trained = False

    def train(self, X, y, vectorizer):
        self.model.fit(X, y)
        self.vectorizer = vectorizer
        self.trained = True

    def predict(self, texts):
        if not self.trained:
            raise Exception("Modelo no entrenado")
        X_new = self.vectorizer.transform(texts)
        return self.model.predict(X_new)

