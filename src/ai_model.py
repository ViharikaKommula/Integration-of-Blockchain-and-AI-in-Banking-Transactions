import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Improved transaction data for better training
data = {
    'amount': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000,
              1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
    'is_fraudulent': [0, 1, 0, 0, 1, 0, 0, 1, 0, 1,
                     0, 1, 0, 0, 1, 0, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Preprocess data
X = df[['amount']]
y = df['is_fraudulent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save the model
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)