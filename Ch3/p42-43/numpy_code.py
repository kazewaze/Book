'''
Predicting on Predictions (Chapter 3 - Pages 42-43):
  - NumPy Code (39 lines)
  - .T method "Flips the Rows and Columns of a Matrix"
'''

import numpy as np

# "Input-to-Hidden" Weights:
                    #toes %win #fans
ih_wgt = np.array([ [0.1, 0.2, -0.1],    # hid[0]
                    [-0.1, 0.1, 0.9],    # hid[1]
                    [0.1, 0.4, 0.1] ]).T # hid[2]

# "Hidden-to-Prediction" Weights:
#                 hid[0] hid[1] hid[2]
hp_wgt = np.array([ [0.3, 1.1, -0.3],    # hurt?
                    [0.1, 0.2, 0.0],     # win?
                    [0.0, 1.3, 0.1] ]).T # sad?

# Weights-Vector for Neural Network:
weights = [ih_wgt, hp_wgt]

# Data:
toes = np.array([8.5, 9.5, 9.90, 9.00])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.50, 1.0])

# Input:
input = np.array([toes[0], wlrec[0], nfans[0]])

# Neural Network:
def neural_network(input, weights):
    hid = input.dot(weights[0])
    pred = hid.dot(weights[1])

    return pred

# Prediction:
print(neural_network(input, weights))