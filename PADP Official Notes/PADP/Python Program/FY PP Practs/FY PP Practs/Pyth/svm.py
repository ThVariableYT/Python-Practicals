import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

bankdata = pd.read_csv("bill_authentication.csv")

#To see the rows and columns and of the data, execute the following command:
bankdata.shape

#To get a feel of how our dataset actually looks, execute the following command:
bankdata.head()

#To divide the data into attributes and labels, execute the following code:
X = bankdata.drop('Class', axis=1)  
y = bankdata['Class']

#to seamlessly divide data into training and test sets  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

#Execute the following code to train the algorithm:
svclassifier = SVC(kernel='linear')  
svclassifier.fit(X_train, y_train)

#To make predictions
y_pred = svclassifier.predict(X_test)

#Confusion matrix, precision, recall, and
#F1 measures are the most commonly used metrics for classification tasks  
print(confusion_matrix(y_test,y_pred))  
print(classification_report(y_test,y_pred))
