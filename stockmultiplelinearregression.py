# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:26:39 2018

@author: Balasubramaniam
"""
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn

dataset = pd.read_csv('MSFT.csv')
X = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 4:5].values
print(X,y)
print(X.shape)
print(y.shape)

from sklearn.linear_model import LinearRegression

lm=LinearRegression()
lm.fit(X,y)
#LinearRegression(copy_X=True, fit_intercept=True, normalize=False)
print("Estimated intercept coefficient",lm.intercept_)
print("coefficients",lm.coef_)
plt.scatter(X[:,1],y)
plt.xlabel("Open Stock")
plt.ylabel("Closing Stock")
plt.title("Relationship between Open and Close Stock")
plt.show()

#predicting stock price
print(lm.predict(X)[0:5])
plt.scatter(X[:,1],lm.predict(X))
plt.plot(X[:,1],lm.predict(X), 'k.') #color code is k or m or etc.,
plt.xlabel("Open")
plt.ylabel("Predicted Close")
plt.title("Open vs Closing Price")
plt.show()
#Mean Sqaured Error
MSE=np.mean((y-lm.predict(X))**2)
print("Mean Sqaured Error %r" %(MSE))
#Sum of Sqaured Error
SSE=np.sum((y-lm.predict(X))**2)
print("SUM of Sqaured Error %r" %(SSE))

'''
#training and test data set
from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test=sklearn.cross_validation.train_test_split(X,bos.PRICE,test_size=0.13,random_state=2)
print('X train shape','-->',X_train.shape)
print('X test shape','-->',X_test.shape)
print(Y_train.shape)
#print(Y_test.shape)
lm=LinearRegression()
lm.fit(X_train,Y_train)
pred_train=lm.predict(X_train)
pred_test=lm.predict(X_test)
print("Estimated intercept coefficient",lm.intercept_)
print("Number of coefficients",len(lm.coef_))
print ("Fit a model X_train, and calculate MSE with Y_train:" , np.mean((Y_train-lm.predict(X_train)) ** 2))
print ("Fit a model X_train, and calculate MSE with Y_test:" , np.mean((Y_test-lm.predict(X_test)) ** 2))
'''