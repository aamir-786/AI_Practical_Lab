import numpy as np
import pandas as pd
from sklearn.svm import LinearSVC
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

# Split the data into training (20%) and test (80%) sets
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.30, random_state=42)

# Train an SVM classifier
svm = LinearSVC(random_state=42)
svm.fit(X_train, y_train)

# Evaluate the model
y_pred = svm.predict(X_test)
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")