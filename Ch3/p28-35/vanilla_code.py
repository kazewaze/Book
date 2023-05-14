'''
Multiple Inputs (Chapter 3 - Pages 28-35):
  - Vanilla Python Code (35 lines)
'''

# Weights:
weights = [0.1, 0.2, 0.0]

# Data:
toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

# Input (First Game Data):
input = [toes[0], wlrec[0], nfans[0]]

# Weighted Sum (Dot Product):
def w_sum(a, b):
    assert(len(a) == len(b))

    output = 0

    for k in range(len(a)):
        output += (a[k] * b[k])

    return output

# Neural Network Function:
def neural_network(input, weights):
    pred = w_sum(input, weights)

    return pred

# Prediction (First Game):
print(neural_network(input, weights))