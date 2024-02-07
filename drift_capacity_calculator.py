# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 19:41:32 2023
Updated on Wed Feb  7 13:21:15 2024
@author: Liam Pledger - liam.pledger@pg.canterbury.ac.nz
"""

import lightgbm as lgb
import numpy as np
import pandas as pd

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
lbd = float(lines[10].strip().split(': ')[1])

input_data = np.transpose(np.array([[a], [a/d], [fyt], [s/d], [fc], [v], [s/lbd], [a/s], [ρl*fyl], [ρt*fyt]], dtype=float))


file = "RC columns updated 2.csv"

# Load data
columns_to_load = [3, 4, 9, 11, 12, 14, 15, 16, 17, 18, 21]
feature_labels = ['a', 
                  'a/d', 
                  r'$f_{yt}$',
                  's/d',       
                  r'$f_{c}$',            
                  'ALR', 
                  r'$s/d_{lb}$',
                  r'$a/s$',
                  r'$\rho_l \times f_y$',
                  r'$\rho_t \times f_{yt}$',
                  ]


data = pd.read_csv(file, skiprows=1, delimiter=",", usecols=columns_to_load)

# Extract features and labels
X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values


if units != 1:  # converting units from the database of column to imperial based on input by user. 
    X[:, 0] = X[:, 0] * 25.4  # a, aspect ratio
    X[:, 2] = X[:, 2] / 145   # fyt, yield strength of transverse reinforcement
    X[:, 4] = X[:, 4] / 145   # fc, compressive strength of concrete
    X[:, 8] = X[:, 8] / 145   # ρl*fyl
    X[:, 9] = X[:, 9] / 145   # ρt*fyt
    

# Create a LightGBM dataset for training
train_data = lgb.Dataset(X, label=Y)

# Define hyperparameters for the LightGBM model
params = {
    'boosting_type': 'gbdt',
    'metric': 'binary_logloss',
    'max_bin' : 50,
    'learning_rate': 0.0075,
    'feature_fraction': 0.4,
}

# Turn off warning messages (set logging level to 'silent')
params['verbose'] = -1  # Set verbose to -1 to suppress warnings

# Train the LightGBM model
num_round = 10000
bst = lgb.train(params, train_data, num_round)

# Make predictions on the test data
y_pred = bst.predict(input_data, num_iteration=bst.best_iteration)


print("""
            
      
      """)
print("The estimated drift capacity of the column is = " + str(np.round(y_pred[0], 1)) + " %")
