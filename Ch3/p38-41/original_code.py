'''
Multiple Inputs & Outputs (Chapter 3 - Pages 38-41)
  - Original Code
'''

# Weights: #toes  %win  #fans
weights = [ [0.1, 0.1, -0.3], # hurt?
            [0.1, 0.2, 0.0],  # win?
            [0.0, 1.3, 0.1] ] # sad?

# Data:
toes = [8.5, 9.5, 9.90, 9.00]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.50, 1.0]

# Input:
input = [toes[0], wlrec[0], nfans[0]]

# Weighted Sum (Dot Product) Function:
def w_sum(a, b):
    assert(len(a) == len(b))

    output = 0

    for k in range(len(a)):
        output += (a[k] * b[k])

    return output

# Vector-Matrix Multiplication Function:
def vec_mat_mul(vector, matrix):
    assert(len(vector) == len(matrix))

    output = [0] * len(vector)

    for k in range(len(vector)):
        output[k] = w_sum(vector, matrix[k])

    return output

# Neural Network:
def neural_network(input, weights):
    pred = vec_mat_mul(input, weights)

    return pred

# Prediction:
print(neural_network(input, weights))