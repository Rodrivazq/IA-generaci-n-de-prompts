from processor import load_data, preprocess_data
from classifier import TextClassifier

def main():
    print("🔧 Iniciando proceso de automatización con IA...\n")
    textos, etiquetas = load_data("../data/input.txt")
    X, vect = preprocess_data(textos)
    clf = TextClassifier()
    clf.train(X, etiquetas, vect)
    pred = clf.predict(textos)
    print("Clasificación:")
    for orig, res in zip(textos, pred):
        print(f"{orig} => {res}")

if __name__ == "__main__":
    main()

