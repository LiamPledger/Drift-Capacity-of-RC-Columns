# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 19:41:32 2023

@author: ljp70
"""

import lightgbm as lgb
import numpy as np


# Open the user_inputs.txt file for reading
with open('user_inputs.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Parse the input data from the file
units = int(lines[0].strip().split(': ')[1])
a = float(lines[1].strip().split(': ')[1])
d = float(lines[2].strip().split(': ')[1])
s = float(lines[3].strip().split(': ')[1])
fc = float(lines[4].strip().split(': ')[1])
fyl = float(lines[5].strip().split(': ')[1])
fyt = float(lines[6].strip().split(': ')[1])
ρl = float(lines[7].strip().split(': ')[1])
ρt = float(lines[8].strip().split(': ')[1])
v = float(lines[9].strip().split(': ')[1])

input_data = np.transpose(np.array([[a/d], [v], [s/a], [s/(a/d)], [fc], [ρl*fyl], [ρt*fyt]], dtype=float))


if units == 1:
    a = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 0) 
    d = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 17)
    s = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 5) 
    row_t = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 6)
    ALR = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 9)
    fyt = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 15)
    fc = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 16)
    fy = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 3)
    row_l = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 4)
    
    s_a = s / a
    s_a_d2 = s / (a/d)

else:
    a = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 0) * 25.4
    d = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 17) * 25.4
    s = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 5)  * 25.4
    row_t = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 6)
    row_l = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 4)
    fyt = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 15) / 145
    fc = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 16) / 145
    fy = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 3) / 145
    ALR = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 9)
    s_a = s / a
    s_a_d2 = s / (a/d)


Drift_Capacity = np.loadtxt("RC columns.csv", skiprows=1, delimiter = ",", usecols = 13)


X = np.stack((a/d, ALR, s_a, s_a_d2, fc, row_l * fy, row_t * fyt), axis = 1)

Y = Drift_Capacity




# Create a LightGBM dataset for training
train_data = lgb.Dataset(X, label=Y)

# Define hyperparameters for the LightGBM model
params = {
    'boosting_type': 'gbdt',
    'metric': 'binary_logloss',
    'max_bin' : 300,
    'learning_rate': 0.0075,
    'feature_fraction': 0.4,
}

# Turn off warning messages (set logging level to 'silent')
params['verbose'] = -1  # Set verbose to -1 to suppress warnings

# Train the LightGBM model
num_round = 3000
bst = lgb.train(params, train_data, num_round)

# Make predictions on the test data
y_pred = bst.predict(input_data, num_iteration=bst.best_iteration)


feature_importance = bst.feature_importance(importance_type='gain')
feature_importance = feature_importance/ sum(feature_importance)

# Print or visualize feature importances
# print("Feature Importance (gain):", np.round(feature_importance, 2))
print("""
            
      
      """)
print("The estimated drift capacity of the column is = " + str(np.round(y_pred[0], 1)) + " %")

