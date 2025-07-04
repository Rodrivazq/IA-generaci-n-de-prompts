from sklearn.feature_extraction.text import TfidfVectorizer

def load_data(path):
    textos, etiquetas = [], []
    with open(path, encoding="utf-8") as f:
        for linea in f:
            if '\t' not in linea:
                continue
            texto, etiqueta = linea.strip().split('\t')
            textos.append(texto)
            etiquetas.append(etiqueta)
    return textos, etiquetas

def preprocess_data(texts):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    return X, vectorizer

