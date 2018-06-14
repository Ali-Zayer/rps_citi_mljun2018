# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:48:04 2018

@author: Balasubramaniam
"""
'''
the purpose is to get some prediction for the 4 following crash profiles that do not exist in the “FARS-2016-PROFILES” dataset :
According to 2016 data, we want an estimation of
1) the number of deaths in a road crash located in a completely dark (2) rural (1) 
    road of Texas (48) occurring a rainy (2) friday (6) 
    involving 2 vehicles 4 people and 1 drunk driver.
2) the number of deaths in a road crash fitting the same previous profile
    but without any drunk drivers
3) the number of deaths in a road crash located in a completely dark (2) 
    rural (1) road of California (6) occurring a rainy (2) friday (6) 
    involving 2 vehicles 5 people and 1 drunk driver.
4) the number of deaths in a road crash fitting the same previous profile 
    but without any drunk drivers
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#loading the dataset
dataset = pd.read_csv('accident.csv')
X = dataset.iloc[:,0:8].values
y = dataset.iloc[:,len(dataset.iloc[0])-1].values
#fitting the Decision Tree Regression model to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X, y)

#The following code answers to the first two questions in Texas state :

#prediction of the number of deaths in a car accident in Texas (48), a friday (6), 
#during a night without lights (2), when raining (2), on a rural road (1) 
#involving 2 vehicles 4 people and 1 drunk driver.
y_pred_TX_Drunk = regressor.predict([[48,6,2,2,1,2,4,1]])
print("Drunk Driver",y_pred_TX_Drunk )
#prediction with the same parameters but no drunk drivers (all drivers were sober).
y_pred_TX_Sober = regressor.predict([[48,6,2,2,1,2,4,0]])
print("No Drunk Driver",y_pred_TX_Sober)
'''
After running this script, we get y_pred_TX_Drunk=3 and y_pred_TX_Sober=1. Therefore, we get 
the prediction that
1) IF a road crash located in a completely dark (2) rural (1) road of Texas (48) 
    occurres during a rainy (2) friday (6) involving 2 vehicles 4 people and
    1 drunk driver THEN according to 2016 data, the estimated number of deaths is 3.
2) IF a road crash occures in the same conditions without any drunk drivers 
    THEN according to 2016 data, the estimated number of deaths is 1.
    
'''

#The following code answer to the next two questions in California state :

#prediction of the number of deaths in a car accident in California (6),
# a friday (6), during a night without lights (2), when raining (2), on a rural 
#road (1) involving 2 vehicles 5 people and 1 drunk driver.
y_pred_CA_Drunk = regressor.predict([[6,6,2,2,1,2,5,1]])
print("Drunk Driver",y_pred_CA_Drunk )
#prediction with the same parameters but no drunk drivers (all drivers were sober).
y_pred_CA_Sober = regressor.predict([[6,6,2,2,1,2,5,0]])
print("No Drunk Driver",y_pred_CA_Sober)
'''
After running this script, y_pred_CA_Drunk=2 and y_pred_CA_Sober=1. 
Therefore, we get the prediction that
1) IF a road crash located in a completely dark (2) rural (1) 
    road of California (6) occurres during a rainy (2) friday (6) 
    involving 2 vehicles 5 people and 1 drunk driver 
    THEN according to 2016 data, the estimated number of deaths is 2.
2) IF a road crash occures in the same conditions this time without any drunk 
    drivers THEN according to 2016 data, the estimated number of deaths is 1.
'''
#visualizing decision tree
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
from sklearn import tree

# Create DOT data
dot_data = tree.export_graphviz(regressor, out_file=None, max_depth=5,
filled=True, rounded=True,
special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)

graph.write_pdf("accident.pdf")