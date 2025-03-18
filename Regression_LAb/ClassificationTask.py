from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load the Iris dataset
data = load_iris()
x , y = data.data , data.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state = 42)

#train the model
model = GaussianNB()
model.fit(X_train, y_train)
#predict 
y_pred = model.predict(X_test)
# Evaluate
print(classification_report(y_test, y_pred))

