import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, OrdinalEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split


# 1. Simple heart disease dataset
data = {
    'age': [45, 54, 37, 62, 57, 49, 51, 60, 39, 58],
    'sex': ['M', 'M', 'F', 'M', 'F', 'M', 'M', 'F', 'F', 'M'],
    'cp': ['typical', 'atypical', 'non', 'asymp', 'typical',
           'atypical', 'non', 'asymp', 'typical', 'atypical'],
    'chol': [230, 250, 210, 280, 240, 220, 260, 300, 190, 270],
    'target': [0, 1, 0, 1, 1, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df.drop('target', axis=1)
y = df['target']


# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# 3. Preprocessing (StandardScaler + OneHot + Ordinal)

# Scale numerical features
scaler = StandardScaler()

X_train_num = scaler.fit_transform(X_train[['age', 'chol']])
X_test_num = scaler.transform(X_test[['age', 'chol']])


# One-hot encode sex
ohe = OneHotEncoder(sparse_output=False, drop='first')

X_train_sex = ohe.fit_transform(X_train[['sex']])
X_test_sex = ohe.transform(X_test[['sex']])


# Ordinal encode chest pain type
oe = OrdinalEncoder(
    categories=[['typical', 'atypical', 'non', 'asymp']]
)

X_train_cp = oe.fit_transform(X_train[['cp']])
X_test_cp = oe.transform(X_test[['cp']])


# Combine features
X_train = np.hstack([X_train_num, X_train_sex, X_train_cp])
X_test = np.hstack([X_test_num, X_test_sex, X_test_cp])


# 4. Logistic Regression
logreg = LogisticRegression(max_iter=1000)

logreg.fit(X_train, y_train)

logreg_pred = logreg.predict(X_test)

print("Logistic Regression Confusion Matrix:")
print(confusion_matrix(y_test, logreg_pred))