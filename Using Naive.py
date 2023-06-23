import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

# Step 1: Load the glass dataset
glass_data = pd.read_csv('glass.csv')

# Step 2: Split the data into features (X) and labels (y)
X = glass_data.drop('Type', axis=1)
y = glass_data['Type']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create and train the Naïve Bayes classifier
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

# Step 5: Make predictions on the testing set
y_pred = nb_classifier.predict(X_test)

# Step 6: Evaluate the model
accuracy = nb_classifier.score(X_test, y_test)
classification_report = classification_report(y_test, y_pred)

# Print the accuracy and classification report
print("Classification Report:\n", classification_report)
print("Accuracy:", accuracy)