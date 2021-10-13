# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 12:25:58 2021

@author: doguilmak

dataset: https://archive.ics.uci.edu/ml/datasets/Dry+Bean+Dataset

"""
#%%
#  1. Libraries

import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')

#%%
# 2. Data Preprocessing

# 2.1. Uploading data
start = time.time()
df = pd.read_excel('Dry_Bean_Dataset.xlsx')
print(df.head())
print(df.info())

# 2.2. Looking For Anomalies
print("{} duplicated.".format(df.duplicated().sum()))
dp = df[df.duplicated(keep=False)]
dp.head(2)
df.drop_duplicates(inplace= True)
print("{} duplicated.".format(df.duplicated().sum()))
print(df.describe().T)

# 2.3. Label Encoding 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["Class"] = le.fit_transform(df['Class'])

# 2.4. Seperate the Data Depending on Dependent and Independent Variableles
y = df["Class"]
X = df.drop("Class", axis = 1)

# 2.5. Split as Train and Test 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# 2.6. Scaling Data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#%%
# 3.1. PCA

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)  # 2 dimensional

X_train2 = pca.fit_transform(X_train)
X_test2 = pca.transform(X_test)

# 3.2. LR Transform Before PCA
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

# 3.3. LR After PCA Transform
classifier2 = LogisticRegression(random_state=0)
classifier2.fit(X_train2, y_train)

# 3.4. Predictions
y_pred = classifier.predict(X_test)
y_pred2 = classifier2.predict(X_test2)


from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# 3.5. Actual / Without PCA 
print('Actual / Without PCA')
cm1 = confusion_matrix(y_test, y_pred)
print(cm1)
print(f"Accuracy score: {accuracy_score(y_test, y_pred)}\n")
 
# 3.6. Actual / Result after PCA
print("Actual / With PCA")
cm2 = confusion_matrix(y_test, y_pred2)
print(cm2)
print(f"Accuracy score: {accuracy_score(y_test, y_pred2)}\n")

# 3.7. After PCA / Before PCA
print('Without PCA and with PCA')
cm3 = confusion_matrix(y_pred, y_pred2)
print(cm3)
print(f"Accuracy score: {accuracy_score(y_pred, y_pred2)}\n")

#%%
# 4. LDA

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda = LDA(n_components = 2)  # 2 dimensional

X_train_lda = lda.fit_transform(X_train, y_train)  # In order for LDA to learn, the y_train parameter is entered.
X_test_lda = lda.transform(X_test)

# 4.1. After LDA Transform
classifier_lda = LogisticRegression(random_state=0)
classifier_lda.fit(X_train_lda, y_train)

# 4.2. Predict LDA Datas
y_pred_lda = classifier_lda.predict(X_test_lda)

# 4.3. After LDA / Actual
print('LDA and Actual')
cm4 = confusion_matrix(y_pred, y_pred_lda)
print(cm4)
print(f"Accuracy score: {accuracy_score(y_pred, y_pred_lda)}\n")

end = time.time()
cal_time = end - start
print("\nProcess took {} seconds.".format(cal_time))
