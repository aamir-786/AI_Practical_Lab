import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset with error handling
try:
    df = pd.read_csv('IMDB Dataset.csv', on_bad_lines='skip', engine='python')
except pd.errors.ParserError:
    print("Dataset not found")

# Sample 500 rows
subset = df.sample(n=500, random_state=42)
print(subset.shape)
print(subset.head())

# Extract features and labels
X = subset['review']
y = subset['sentiment']

# Convert text data to numerical features using TF-IDF
vectorizer = TfidfVectorizer(max_features=10000)
X_vec = vectorizer.fit_transform(X)

# Split the data into training (80%) and test (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.20, random_state=42)

# Initialize a base SVM classifier
base_svm = LinearSVC(random_state=42)

# Initialize a Bagging classifier using the base SVM
bagging = BaggingClassifier(
    estimator=base_svm,
    n_estimators=10,  # Number of models to train
    max_samples=0.7,  # Percentage of samples to train each model on
    random_state=42       # Use all available CPU cores
)

# Train the Bagging classifier
bagging.fit(X_train, y_train)

# Evaluate the model
y_pred = bagging.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.4f}")
print(f"Predictions: {y_pred[:10]}")