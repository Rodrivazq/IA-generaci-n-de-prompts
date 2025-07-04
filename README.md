### 🤖 Proyecto Final - IA: Generación de Prompts

Este proyecto demuestra cómo aplicar técnicas de Inteligencia Artificial para automatizar la clasificación de textos y generar prompts adaptados según su categoría. Se usaron herramientas de procesamiento de lenguaje natural, machine learning y la API de OpenAI para lograr una solución funcional, educativa y escalable.

---

## 📌 Descripción

El sistema:
- Clasifica textos (por ejemplo, mensajes de usuarios).
- Asigna una categoría basada en entrenamiento supervisado.
- Genera un prompt personalizado utilizando la API de OpenAI GPT.

Esto permite automatizar procesos como:
- Respuestas a clientes.
- Generación de ideas.
- Creación de contenido.

---

## 🗂️ Estructura del Proyecto

ia_automatizacion/
├── data/
│ └── input.txt
├── notebooks/
│ └── exploracion.ipynb
├── src/
│ ├── classifier.py
│ ├── processor.py
│ └── main.py
├── requirements.txt
└── README.md

---

## 🧠 Tecnologías Utilizadas

- Python 3.10
- scikit-learn
- pandas / numpy
- OpenAI API (GPT-4)
- Jupyter Notebook
- Matplotlib

---

## 🚀 Cómo Ejecutar

1. Cloná este repositorio:
   ```bash
   git clone https://github.com/Rodrivazq/IA-generacion-de-prompts.git
2. Instalá dependencias:

pip install -r requirements.txt

3. Ejecutá el script principal:

python src/main.py

El script lee los datos desde data/input.txt, entrena el modelo, clasifica nuevas entradas y genera un prompt usando la API de OpenAI (debes tener tu clave configurada en una variable de entorno).

## 📊 Resultados
Precisión del modelo: >90% (con TF-IDF + Naive Bayes)

El sistema puede adaptarse fácilmente a nuevas categorías o tipos de texto con pocos cambios.

## ✍️ Autor
Rodrigo Vázquez
Curso: Inteligencia Artificial - Coderhouse
Julio 2025

## 🛑 Licencia
Este proyecto es de uso educativo. No usar en producción sin revisión adicional.