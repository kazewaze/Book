'''
Multiple Inputs (Chapter 3 - Page 35):
  - NumPy Code (26 lines)
'''

import numpy as np

# Weights:
weights = np.array([0.1, 0.2, 0.0])

# Data:
toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

# Input (First Game Data):
input = np.array([toes[0], wlrec[0], nfans[0]])

# Neural Network Function:
def neural_network(input, weights):
    pred = input.dot(weights) # Dot Product

    return pred

# Prediction (First Game):
print(neural_network(input, weights))