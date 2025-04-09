# dataset_preparation_and_model_training.py
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load the dataset
with open('healthcare_dataset.json') as f:
    dataset = json.load(f)
print("Dataset loaded succesfully!!......")
# Preprocess the data
questions = []
answers = []
for item in dataset:
    for question in item['question']:
        questions.append(question)
        answers.append(item['answer'])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Create and train the model
model = LogisticRegression()
model.fit(X, answers)

# Save the model and vectorizer
with open('chatbot_model.pkl', 'wb') as f:
    pickle.dump((vectorizer, model), f)
print("model trained succesfully!!......")

