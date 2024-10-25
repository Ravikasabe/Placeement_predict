import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from joblib import dump


df = pd.read_csv(r'placement_predict.csv') #Import  all path od file

df['status'] = df['status'].map({'Placed': 1, 'Not Placed': 0})


df = df.dropna(subset=['status'])


X = df.drop(['ssc_b', 'hsc_b', 'hsc_s', 'degree_t', 'status', 'workex', 'etest_p', 'specialisation', 'mba_p'], axis=1)
y = df['status']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234, stratify=y)


imputer = SimpleImputer(strategy='mean') 
X_test = imputer.transform(X_test)

svm_classifier = SVC(class_weight='balanced') 
svm_classifier.fit(X_train, y_train)


y_pred = svm_classifier.predict(X_test)

print("="*40)
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy: %.2f" % (accuracy_score(y_test, y_pred) * 100))


conf_matrix = confusion_matrix(y_test, y_pred)
print("==================")
print("Confusion Matrix:\n", conf_matrix)


plt.figure(figsize=(10,7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title("Confusion Matrix")
plt.show()

dump(svm_classifier, 'model.joblib')
print("Model saved as model.joblib")
